# SeaFogWatch Detection Service | 海雾检测服务

[English](./README-Detection_EN.md) | 简体中文

基于深度学习的海雾检测服务，SeaFogWatch系统的核心算法实现。本项目采用最新的MP-Former（CVPR 2023）模型架构，结合CSWin Transformer和Agent Attention机制，实现高精度的海雾检测。

## 项目简介 | Overview

本项目是SeaFogWatch海雾监测系统的检测服务部分，基于深度学习技术实现对卫星图像中海雾的自动检测。项目使用Python实现，集成了图像处理和深度学习模型，提供高精度的海雾识别能力。

### 主要功能 | Key Features

- 海雾自动检测：基于MP-Former模型的高精度海雾识别
- 卫星图像预处理：支持多光谱卫星数据处理（NetCDF格式）
- 多模型集成预测：支持模型集成以提高检测稳定性
- 检测结果后处理：包括地理编码和可视化
- 批量数据处理：支持大规模卫星图像批处理
- REST API服务：提供标准化的检测服务接口

### 模型特点 | Model Features

- 基于MP-Former架构（CVPR 2023）
- 结合CSWin Transformer和Agent Attention
- 支持多尺度特征提取
- 高效的局部-全局注意力机制
- 位置感知的特征学习

## 技术栈 | Technology Stack

- Python 3.8+
- PyTorch 1.10+
- OpenCV
- NumPy/Pandas
- FastAPI/Flask
- GDAL 3.4.1
- netCDF4

## 开发环境 | Development Environment

### 系统要求 | System Requirements

- CUDA 11.0+（推荐）
- 16GB+ RAM
- 50GB+ 磁盘空间
- Linux/Windows操作系统

### Python环境配置 | Python Environment Setup

推荐使用Anaconda管理环境：

```bash
# 创建环境
conda create -n seafog python=3.8

# 激活环境
conda activate seafog

# 安装GDAL
conda install -c conda-forge gdal=3.4.1

# 安装其他依赖
pip install -r requirements.txt
```

## 快速开始 | Quick Start

### 环境准备 | Prerequisites

1. 安装CUDA和cuDNN
2. 安装Anaconda或Miniconda
3. 下载预训练模型

### 安装步骤 | Installation Steps

1. 克隆仓库
```bash
git clone https://github.com/yourusername/SeaFogWatch-Detection.git
cd SeaFogWatch-Detection
```

2. 创建并激活环境
```bash
conda create -n seafog python=3.8
conda activate seafog
```

3. 安装依赖
```bash
conda install -c conda-forge gdal=3.4.1
pip install -r requirements.txt
```

4. 配置环境变量
```bash
cp .env.example .env
# 编辑.env文件配置必要的参数
```

### 使用方法 | Usage

1. 启动API服务
```bash
python api.py
```

2. 单次检测
```bash
python predict.py --input path/to/image.nc --output path/to/result
```

3. 批量检测
```bash
python eval_batch.py --input path/to/images --output path/to/results
```

## API文档 | API Documentation

### REST API端点

#### 1. 文件上传检测
- 端点：`POST /process_nc`
- 功能：处理上传的NetCDF文件并进行检测
- 参数：
  - `file`: NetCDF文件
  - `lon_min`, `lon_max`, `lat_min`, `lat_max`: 地理范围

#### 2. 路径检测
- 端点：`POST /process_nc_path`
- 功能：处理指定路径的NetCDF文件
- 参数：
  - `file_path`: 文件路径
  - `lon_min`, `lon_max`, `lat_min`, `lat_max`: 地理范围

#### 3. 模型检测
- 端点：`POST /detect`
- 功能：使用指定模型进行检测
- 参数：
  - `image_path`: 图像路径
  - `model_path`: 模型路径

## 模型说明 | Model Description

### 模型架构 | Architecture

- 基础网络：CSWin Transformer
- 注意力机制：Agent Attention
- 特征提取：多尺度特征融合
- 检测头：Mask-Piloted Transformer

### 训练数据 | Training Data

- 数据来源：向日葵卫星
- 数据格式：NetCDF
- 光谱波段：可见光和红外波段
- 标注类型：像素级标注

### 模型性能 | Performance

- 检测精度：AP 40.15（12轮训练）
- 处理速度：支持实时处理
- 支持分辨率：384x384 到 2560x2560

## 开发指南 | Development Guide

### 代码规范 | Code Standards

- 遵循PEP 8规范
- 使用pylint进行代码检查
- 编写单元测试

### 模型开发 | Model Development

1. 数据预处理
```python
# 示例代码
def preprocess_data(nc_file):
    # 数据预处理逻辑
    pass
```

2. 模型训练
```python
# 训练脚本示例
bash run_50ep_no_noise_all_ly.sh
```

3. 模型评估
```python
# 评估脚本示例
bash eval.sh
```

## 测试 | Testing

```bash
# 运行单元测试
pytest tests/

# 运行集成测试
pytest tests/integration/

# 检查代码质量
pylint app/
```

## 部署 | Deployment

### Docker部署 | Docker Deployment

```bash
# 构建镜像
docker build -t seafog-detection .

# 运行容器
docker run -p 8000:8000 seafog-detection
```

### 生产环境配置 | Production Configuration

- 使用gunicorn作为WSGI服务器
- 配置supervisor进行进程管理
- 设置日志记录

## 常见问题 | FAQ

1. 如何处理大型卫星图像？
   - 使用滑动窗口进行分块处理
   - 设置适当的batch size

2. 如何提高检测准确率？
   - 使用模型集成
   - 调整后处理参数
   - 增加训练数据多样性

3. 如何优化处理速度？
   - 使用GPU加速
   - 启用批处理模式
   - 优化图像预处理流程

4. 如何进行模型微调？
   - 准备领域特定数据
   - 调整学习率和训练参数
   - 使用迁移学习策略

## 参与贡献 | Contributing

我们欢迎对项目的贡献！请参阅[贡献指南](CONTRIBUTING.md)。

## 许可证 | License

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件。

## 引用 | Citation

如果您在研究中使用了本项目，请引用：

```bibtex
@inproceedings{mpformer2023,
  title={MP-Former: Mask-Piloted Transformer for Image Segmentation},
  author={Your Name},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2023}
}
```

## 联系方式 | Contact

如有问题和建议，请在GitHub仓库中提出Issue或直接联系维护者。