 # SeaFogWatch Detection Service | 海雾检测服务

[English](./README_EN.md) | 简体中文

基于深度学习的海雾检测服务，SeaFogWatch系统的核心算法实现。

Deep learning-based sea fog detection service, the core algorithm implementation of the SeaFogWatch system.

<p align="center">
  <!-- 在此处添加检测效果图 | Add detection result image here -->
</p>

## 项目简介 | Overview

本项目是SeaFogWatch海雾监测系统的检测服务部分，基于深度学习技术实现对卫星图像中海雾的自动检测。项目使用Python实现，集成了图像处理和深度学习模型，提供高精度的海雾识别能力。

This project is the detection service component of the SeaFogWatch system, implementing automatic sea fog detection in satellite imagery using deep learning technology. Built with Python, it integrates image processing and deep learning models to provide high-accuracy sea fog recognition capabilities.

### 主要功能 | Key Features

- 海雾自动检测 | Automatic sea fog detection
- 卫星图像预处理 | Satellite image preprocessing
- 多模型集成预测 | Multi-model ensemble prediction
- 检测结果后处理 | Detection result post-processing
- 批量数据处理 | Batch data processing
- REST API服务 | REST API service

## 技术栈 | Technology Stack

- Python 3.8+
- PyTorch/TensorFlow
- OpenCV
- NumPy/Pandas
- FastAPI
- scikit-learn
- netCDF4
- GDAL

## 开发环境 | Development Environment

### 系统要求 | System Requirements

- CUDA 11.0+ (推荐 | Recommended)
- 16GB+ RAM
- 50GB+ 磁盘空间 | Disk space

### Python环境 | Python Environment

推荐使用Anaconda管理环境：

```bash
# 创建环境 | Create environment
conda create -n seafog python=3.8

# 激活环境 | Activate environment
conda activate seafog

# 安装依赖 | Install dependencies
pip install -r requirements.txt
```

## 快速开始 | Quick Start

### 环境准备 | Prerequisites

1. 安装CUDA和cuDNN（用于GPU加速）| Install CUDA and cuDNN (for GPU acceleration)
2. 安装Anaconda或Miniconda | Install Anaconda or Miniconda
3. 准备预训练模型 | Prepare pre-trained models

### 安装和配置 | Installation and Configuration

1. 克隆仓库 | Clone the repository
```bash
git clone https://github.com/yourusername/SeaFogWatch-Detection.git
cd SeaFogWatch-Detection
```

2. 创建并激活环境 | Create and activate environment
```bash
conda create -n seafog python=3.8
conda activate seafog
```

3. 安装依赖 | Install dependencies
```bash
pip install -r requirements.txt
```

4. 配置环境变量 | Configure environment variables
```bash
cp .env.example .env
# 编辑.env文件配置必要的参数 | Edit .env file to configure necessary parameters
```

5. 下载预训练模型 | Download pre-trained models
```bash
python scripts/download_models.py
```

### 运行服务 | Run Service

1. 启动API服务 | Start API service
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

2. 运行单次检测 | Run single detection
```bash
python scripts/detect.py --input path/to/image.nc --output path/to/result
```

3. 运行批量检测 | Run batch detection
```bash
python scripts/batch_detect.py --input path/to/images --output path/to/results
```

## 项目结构 | Project Structure

```
SeaFogWatch-Detection/
├── app/                 # API服务 | API service
│   ├── api/            # API路由 | API routes
│   ├── core/           # 核心功能 | Core functionality
│   ├── models/         # 数据模型 | Data models
│   └── main.py         # 主程序 | Main program
├── models/             # 模型文件 | Model files
│   ├── weights/        # 模型权重 | Model weights
│   └── configs/        # 模型配置 | Model configs
├── scripts/            # 工具脚本 | Utility scripts
├── tests/              # 测试文件 | Test files
├── data/               # 数据目录 | Data directory
│   ├── raw/           # 原始数据 | Raw data
│   └── processed/     # 处理后数据 | Processed data
└── notebooks/         # Jupyter notebooks
```

## 模型说明 | Model Description

### 模型架构 | Model Architecture

- 基础网络：ResNet50/EfficientNet | Base network: ResNet50/EfficientNet
- 特征提取：FPN | Feature extraction: FPN
- 检测头：自适应特征融合 | Detection head: Adaptive feature fusion

### 训练数据 | Training Data

- 数据来源：向日葵卫星 | Data source: Himawari satellite
- 数据格式：NetCDF | Data format: NetCDF
- 数据量：XXXX样本 | Data volume: XXXX samples

### 模型性能 | Model Performance

- 准确率 | Accuracy: XX%
- 召回率 | Recall: XX%
- 处理速度 | Processing speed: XX images/s

## API文档 | API Documentation

### REST API

- POST `/api/v1/detect` - 单图像检测 | Single image detection
- POST `/api/v1/batch_detect` - 批量检测 | Batch detection
- GET `/api/v1/models` - 获取可用模型 | Get available models

详细API文档访问 | Detailed API documentation at: `http://localhost:8000/docs`

## 开发指南 | Development Guide

### 代码规范 | Code Standards

- 遵循PEP 8规范 | Follow PEP 8 standards
- 使用pylint进行代码检查 | Use pylint for code checking
- 编写单元测试 | Write unit tests

### 模型开发 | Model Development

- 模型训练流程 | Model training process
- 模型评估方法 | Model evaluation methods
- 模型部署步骤 | Model deployment steps

## 测试 | Testing

```bash
# 运行单元测试 | Run unit tests
pytest tests/

# 运行集成测试 | Run integration tests
pytest tests/integration/

# 检查代码质量 | Check code quality
pylint app/
```

## 部署 | Deployment

### Docker部署 | Docker Deployment

```bash
# 构建镜像 | Build image
docker build -t seafog-detection .

# 运行容器 | Run container
docker run -p 8000:8000 seafog-detection
```

### 生产环境配置 | Production Configuration

- 使用gunicorn作为WSGI服务器 | Use gunicorn as WSGI server
- 配置supervisor进行进程管理 | Configure supervisor for process management
- 设置日志记录 | Set up logging

## 常见问题 | FAQ

1. 如何处理大型卫星图像？| How to handle large satellite images?
2. 如何提高检测准确率？| How to improve detection accuracy?
3. 如何优化处理速度？| How to optimize processing speed?
4. 如何进行模型微调？| How to fine-tune models?

## 参与贡献 | Contributing

我们欢迎对项目的贡献！请参阅贡献指南。

We welcome contributions! Please see the contributing guidelines.

## 许可证 | License

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 相关项目 | Related Projects

- [SeaFogWatch-Backend](https://github.com/yourusername/SeaFogWatch-Backend) - 后端服务 | Backend service
- [SeaFogWatch-Frontend](https://github.com/yourusername/SeaFogWatch-Frontend) - 前端应用 | Frontend application

## 引用 | Citation

如果您在研究中使用了本项目，请引用：

If you use this project in your research, please cite:

```bibtex
@article{seafogwatch2024,
  title={SeaFogWatch: A Deep Learning Approach for Sea Fog Detection},
  author={Your Name},
  journal={Your Journal},
  year={2024}
}
```

## 联系方式 | Contact

如有问题和建议，请在GitHub仓库中提出Issue或直接联系维护者。

For questions and support, please open an issue in the GitHub repository or contact the maintainers directly.