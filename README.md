# SeaFogWatch 海雾监测系统 | Sea Fog Detection System

[English](./README_EN.md) | 简体中文

基于卫星图像分析和深度学习的综合海雾监测与预警系统。

<p align="center">
  <!-- 在此处添加项目logo或截图 | Add project logo or screenshot here -->
</p>

## 项目简介 | Overview

SeaFogWatch是一个集成的海雾监测系统，利用向日葵卫星数据，通过先进的深度学习算法实现实时海雾检测和分析。本系统采用前后端分离架构，结合深度学习模型，提供全方位的海雾监测解决方案。

### 主要功能 | Key Features

- 基于卫星图像的实时海雾检测 | Real-time sea fog detection using satellite imagery
- 向日葵卫星数据自动采集 | Automated Himawari satellite data collection
- 支持真彩色和假彩色图像处理 | Support for both true color and false color image processing
- 检测结果可视化展示 | Interactive visualization of detection results
- 历史数据分析和趋势追踪 | Historical data analysis and trend tracking
- 完整的RESTful API接口 | Complete RESTful API interface

## 系统架构 | System Architecture

系统由三个主要组件构成 | The system consists of three main components:

### 1. 后端服务 (当前仓库) | Backend Service (Current Repository)

- 基于Spring Boot构建 | Built with Spring Boot
- 处理数据管理和系统操作 | Handles data management and system operations
- 提供RESTful API接口 | Provides RESTful APIs
- 用户认证和授权管理 | User authentication and authorization
- 与检测服务协调 | Coordinates with detection service

技术栈 | Technology Stack:
- Java 8+
- Spring Boot
- MyBatis
- WebSocket
- Redis
- MySQL

### 2. 前端应用| Frontend Application

- 系统交互界面 | User interface
- 实时检测结果展示 | Real-time detection results display
- 管理员控制面板 | Admin dashboard
- 数据分析工具 | Data analysis tools

技术栈 | Technology Stack:
- Vue.js
- Element UI
- ECharts
- WebSocket客户端 | WebSocket client

### 3. 海雾检测服务  | Sea Fog Detection Service

- 卫星图像处理 | Satellite image processing
- 机器学习模型实现 | Machine learning model implementation
- 海雾检测算法 | Sea fog detection algorithms
- 分析结果生成 | Analysis results generation

技术栈 | Technology Stack:
- Python
- 深度学习框架 | Deep Learning frameworks
- 图像处理库 | Image processing libraries
- 科学计算工具 | Scientific computing tools

## 快速开始 | Quick Start

### 环境要求 | Prerequisites

- JDK 1.8+
- Maven 3.6+
- MySQL 5.7+
- Redis
- Python 3.8+ (检测服务 | Detection service)
- Node.js 14+ (前端 | Frontend)

### 后端部署 | Backend Setup

1. 克隆仓库 | Clone the repository
```bash
git clone https://github.com/yourusername/SeaFogWatch.git
cd SeaFogWatch
```

2. 配置数据库 | Configure database
```bash
# 修改 application.yml 中的数据库配置
# Update database settings in application.yml
```

3. 构建运行 | Build and run
```bash
mvn clean install
java -jar seafog-admin/target/seafog-admin.jar
```

### 前端部署  | Frontend Setup 

前端应用的部署说明在[SeaFogWatch-Frontend](./README-Frontend.md)

### 检测服务部署 | Detection Service Setup

海雾检测服务的部署说明在[SeaFogWatch-Detection](./README-Detection.md)

## API文档 | API Documentation

后端服务提供以下主要API接口 | The backend service provides the following main API endpoints:

- `/api/detection/image/*` - 图像管理接口 | Image management endpoints
- `/api/detection/collect/*` - 数据采集接口 | Data collection endpoints
- `/api/detection/analysis/*` - 分析结果接口 | Analysis result endpoints

详细的API文档可通过Swagger UI访问 | Detailed API documentation is available through Swagger UI:
`http://localhost:8080/swagger-ui.html`

## 项目结构 | Project Structure

```
SeaFogWatch/
├── seafog-admin/        # 系统管理模块 | System administration module
├── seafog-framework/    # 框架核心 | Framework core
├── seafog-system/      # 系统功能 | System management
├── seafog-quartz/      # 任务调度 | Task scheduling
├── seafog-generator/   # 代码生成 | Code generation
├── seafog-common/      # 公共工具 | Common utilities
└── seafog-detection/   # 海雾检测模块 | Sea fog detection module
```

## 参与贡献 | Contributing

我们欢迎对SeaFogWatch项目的贡献！在提交Pull Request之前，请阅读我们的贡献指南。

1. Fork本仓库 | Fork the repository
2. 创建特性分支 | Create your feature branch
3. 提交更改 | Commit your changes
4. 推送到分支 | Push to the branch
5. 创建Pull Request | Create a Pull Request

## 许可证 | License

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢 | Acknowledgments

- RuoYi Vue框架
- 向日葵卫星数据服务
- 项目贡献者和支持者

## 联系方式

如有问题和建议，请在GitHub仓库中提出Issue或直接联系维护者。



