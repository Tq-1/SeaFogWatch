from flask import Flask, request, jsonify
import numpy as np
from osgeo import gdal
import base64
import io
from PIL import Image
import tempfile
import os
import logging

app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 设置最大上传大小为1GB
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024

def normalize(array):
    min_val = np.percentile(array, 2)
    max_val = np.percentile(array, 98)
    return np.clip((array - min_val) * (255.0 / (max_val - min_val)), 0, 255).astype('uint8')

def geo_to_pixel(lon, lat, geotransform):
    x = int((lon - geotransform[0]) / geotransform[1])
    y = int((geotransform[3] - lat) / abs(geotransform[5]))
    return x, y

def validate_pixel_coordinates(x, y, max_width, max_height):
    x = max(0, min(x, max_width - 1))
    y = max(0, min(y, max_height - 1))
    return x, y

def process_nc_file(filename, lon_min, lon_max, lat_min, lat_max):
    logger.debug(f"处理文件: {filename}")
    logger.debug(f"坐标范围: lon_min={lon_min}, lon_max={lon_max}, lat_min={lat_min}, lat_max={lat_max}")

    gdal.AllRegister()
    gdal.SetConfigOption('GDAL_NETCDF_VARS_CONVENTIONS', 'CF')
    gdal.SetConfigOption('NETCDF_IGNORE_MULTI_DIMS', 'YES')

    dataset = gdal.Open(f'NETCDF:"{filename}":tbb_14')
    if dataset is None:
        raise Exception("无法打开文件")

    geotransform = dataset.GetGeoTransform()
    x_min, y_max = geo_to_pixel(lon_min, lat_max, geotransform)
    x_max, y_min = geo_to_pixel(lon_max, lat_min, geotransform)
    x_min, y_max = validate_pixel_coordinates(x_min, y_max, dataset.RasterXSize, dataset.RasterYSize)
    x_max, y_min = validate_pixel_coordinates(x_max, y_min, dataset.RasterXSize, dataset.RasterYSize)
    
    # Ensure x_min is less than x_max and y_min is less than y_max
    x_min, x_max = min(x_min, x_max), max(x_min, x_max)
    y_min, y_max = min(y_min, y_max), max(y_min, y_max)
    
    width = x_max - x_min + 1
    height = y_max - y_min + 1

    logger.debug(f"像素范围: x_min={x_min}, x_max={x_max}, y_min={y_min}, y_max={y_max}")
    
    band14 = dataset.ReadAsArray(x_min, y_min, width, height)
    dataset = gdal.Open(f'NETCDF:"{filename}":albedo_01')
    band01 = dataset.ReadAsArray(x_min, y_min, width, height)
    dataset = gdal.Open(f'NETCDF:"{filename}":albedo_02')
    band02 = dataset.ReadAsArray(x_min, y_min, width, height)
    dataset = gdal.Open(f'NETCDF:"{filename}":albedo_04')
    band04 = dataset.ReadAsArray(x_min, y_min, width, height)
    dataset = gdal.Open(f'NETCDF:"{filename}":albedo_03')
    band03 = dataset.ReadAsArray(x_min, y_min, width, height)

    true_color = np.dstack([normalize(band) for band in [band01, band02, band03]])
    false_color = np.dstack([normalize(band) for band in [band14, band04, band03]])

    return true_color, false_color

def image_to_base64(image_array):
    try:
        if image_array is None:
            logger.error("输入图像数组为None")
            return None
            
        if not isinstance(image_array, np.ndarray):
            logger.error(f"输入不是numpy数组，而是: {type(image_array)}")
            return None
            
        logger.debug(f"图像数组形状: {image_array.shape}, 类型: {image_array.dtype}")
        
        # 确保图像数据类型正确
        if image_array.dtype != np.uint8:
            logger.debug("转换图像数据类型为uint8")
            image_array = image_array.astype(np.uint8)
        
        # 创建PIL图像
        image = Image.fromarray(image_array)
        logger.debug(f"PIL图像大小: {image.size}, 模式: {image.mode}")
        
        # 保存为bytes
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        
        # 转换为base64
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        logger.debug(f"生成的base64字符串长度: {len(img_str)}")
        
        return img_str
        
    except Exception as e:
        logger.error(f"图像转base64失败: {str(e)}", exc_info=True)
        return None

@app.route('/process_nc', methods=['POST'])
def process_nc():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    temp_file = None

    try:
        # 获取参数
        lon_min = float(request.form.get('lon_min'))
        lon_max = float(request.form.get('lon_max'))
        lat_min = float(request.form.get('lat_min'))
        lat_max = float(request.form.get('lat_max'))

        logger.info(f"接收到文件: {file.filename}")
        logger.debug(f"坐标参数: lon_min={lon_min}, lon_max={lon_max}, lat_min={lat_min}, lat_max={lat_max}")

        # 保存到临时文件
        temp_fd, temp_path = tempfile.mkstemp(suffix='.nc')
        os.close(temp_fd)
        file.save(temp_path)
        
        logger.debug(f"临时文件保存到: {temp_path}")

        # 处理文件
        true_color, false_color = process_nc_file(temp_path, lon_min, lon_max, lat_min, lat_max)
        
        # 转换为base64
        true_color_base64 = image_to_base64(true_color)
        false_color_base64 = image_to_base64(false_color)

        logger.info("文件处理成功")
        
        return jsonify({
            "true_color": true_color_base64,
            "false_color": false_color_base64
        })

    except Exception as e:
        logger.error(f"处理失败: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

    finally:
        # 清理临时文件
        if temp_file and os.path.exists(temp_file):
            try:
                os.remove(temp_file)
                logger.debug(f"临时文件已删除: {temp_file}")
            except Exception as e:
                logger.warning(f"无法删除临时文件: {temp_file}, 错误: {str(e)}")

@app.route('/process_nc_path', methods=['POST'])
def process_nc_path():
    try:
        # 从请求中获取参数
        data = request.get_json()
        if not data:
            logger.error("没有收到JSON数据")
            return jsonify({"error": "No JSON data received"}), 400
            
        logger.debug(f"收到的请求数据: {data}")
        
        file_path = data.get('file_path')
        if not file_path:
            logger.error("未提供文件路径")
            return jsonify({"error": "No file path provided"}), 400

        try:
            lon_min = float(data.get('lon_min'))
            lon_max = float(data.get('lon_max'))
            lat_min = float(data.get('lat_min'))
            lat_max = float(data.get('lat_max'))
        except (TypeError, ValueError) as e:
            logger.error(f"坐标参数转换失败: {str(e)}")
            return jsonify({"error": f"Invalid coordinate values: {str(e)}"}), 400

        logger.info(f"处理文件路径: {file_path}")
        logger.debug(f"坐标参数: lon_min={lon_min}, lon_max={lon_max}, lat_min={lat_min}, lat_max={lat_max}")

        # 检查文件是否存在
        if not os.path.exists(file_path):
            logger.error(f"文件不存在: {file_path}")
            return jsonify({"error": f"File not found: {file_path}"}), 404

        # 检查文件是否可读
        if not os.access(file_path, os.R_OK):
            logger.error(f"文件无法读取: {file_path}")
            return jsonify({"error": f"File not readable: {file_path}"}), 403

        # 处理文件
        try:
            true_color, false_color = process_nc_file(file_path, lon_min, lon_max, lat_min, lat_max)
            logger.debug("成功生成图像数组")
            logger.debug(f"真彩色图像形状: {true_color.shape}")
            logger.debug(f"伪彩色图像形状: {false_color.shape}")
        except Exception as e:
            logger.error(f"处理NC文件失败: {str(e)}", exc_info=True)
            return jsonify({"error": f"Failed to process NC file: {str(e)}"}), 500
        
        # 转换为base64
        try:
            true_color_base64 = image_to_base64(true_color)
            false_color_base64 = image_to_base64(false_color)
            logger.debug(f"真彩色base64长度: {len(true_color_base64) if true_color_base64 else 0}")
            logger.debug(f"伪彩色base64长度: {len(false_color_base64) if false_color_base64 else 0}")
        except Exception as e:
            logger.error(f"图像转换base64失败: {str(e)}", exc_info=True)
            return jsonify({"error": f"Failed to convert images to base64: {str(e)}"}), 500

        if not true_color_base64 or not false_color_base64:
            logger.error("生成的base64图像数据为空")
            return jsonify({"error": "Generated base64 image data is empty"}), 500

        response_data = {
            "trueColor": true_color_base64,
            "falseColor": false_color_base64,
            "error": None
        }
        logger.info("文件处理成功")
        logger.debug(f"响应数据键: {list(response_data.keys())}")
        
        return jsonify(response_data)

    except Exception as e:
        logger.error(f"处理失败: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 