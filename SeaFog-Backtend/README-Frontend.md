# SeaFogWatch Frontend | 海雾监测系统前端

[English](./README_EN.md) | 简体中文

SeaFogWatch系统的前端应用，提供海雾监测和分析的可视化界面。

The frontend application for SeaFogWatch system, providing visualization interface for sea fog monitoring and analysis.

<p align="center">
  <!-- 在此处添加项目截图 | Add project screenshot here -->
</p>

## 项目简介 | Overview

本项目是SeaFogWatch海雾监测系统的前端部分，基于Vue.js和Element UI构建。提供直观的用户界面，实现海雾数据的可视化展示、实时监控和历史数据分析等功能。

This is the frontend part of the SeaFogWatch sea fog detection system, built with Vue.js and Element UI. It provides an intuitive user interface for sea fog data visualization, real-time monitoring, and historical data analysis.

### 主要功能 | Key Features

- 实时海雾监测展示 | Real-time sea fog monitoring display
- 卫星图像浏览和对比 | Satellite image browsing and comparison
- 历史数据查询和分析 | Historical data query and analysis
- 数据可视化和图表展示 | Data visualization and charts
- 系统管理和配置界面 | System management and configuration interface
- 用户权限和角色管理 | User permission and role management

## 技术栈 | Technology Stack

- Vue.js 3.x
- Element Plus
- ECharts 5.x
- Vue Router
- Vuex/Pinia
- Axios
- WebSocket
- TypeScript

## 开发环境 | Development Environment

- Node.js 14+
- npm 6+ 或 yarn 1.22+
- VSCode (推荐 | Recommended)

## 快速开始 | Quick Start

### 环境准备 | Prerequisites

```bash
# 检查Node.js版本 | Check Node.js version
node -v

# 检查npm版本 | Check npm version
npm -v
```

### 安装和运行 | Installation and Running

1. 克隆仓库 | Clone the repository
```bash
git clone https://github.com/yourusername/SeaFogWatch-Frontend.git
cd SeaFogWatch-Frontend
```

2. 安装依赖 | Install dependencies
```bash
npm install
# 或使用 yarn | or use yarn
yarn install
```

3. 配置环境变量 | Configure environment variables
```bash
# 复制环境变量模板 | Copy environment template
cp .env.example .env.local

# 编辑配置文件 | Edit configuration
vim .env.local
```

4. 启动开发服务器 | Start development server
```bash
npm run dev
# 或使用 yarn | or use yarn
yarn dev
```

5. 构建生产版本 | Build for production
```bash
npm run build
# 或使用 yarn | or use yarn
yarn build
```

## 项目结构 | Project Structure

```
SeaFogWatch-Frontend/
├── public/              # 静态资源 | Static assets
├── src/
│   ├── api/            # API接口定义 | API interface definitions
│   ├── assets/         # 项目资源文件 | Project assets
│   ├── components/     # 通用组件 | Common components
│   ├── layouts/        # 布局组件 | Layout components
│   ├── router/         # 路由配置 | Route configurations
│   ├── store/          # 状态管理 | State management
│   ├── styles/         # 全局样式 | Global styles
│   ├── utils/          # 工具函数 | Utility functions
│   ├── views/          # 页面组件 | Page components
│   ├── App.vue         # 根组件 | Root component
│   └── main.ts         # 入口文件 | Entry file
├── tests/              # 测试文件 | Test files
├── .env.example        # 环境变量模板 | Environment template
├── package.json        # 项目配置 | Project configuration
└── vite.config.ts      # Vite配置 | Vite configuration
```

## 开发指南 | Development Guide

### 编码规范 | Coding Standards

- 使用TypeScript编写代码 | Use TypeScript for coding
- 遵循ESLint配置的代码规范 | Follow ESLint code standards
- 使用Prettier进行代码格式化 | Use Prettier for code formatting

### 组件开发 | Component Development

- 遵循Vue3组合式API规范 | Follow Vue 3 Composition API standards
- 确保组件的可复用性 | Ensure component reusability
- 编写组件文档和示例 | Write component documentation and examples

### 提交规范 | Commit Standards

- 使用约定式提交规范 | Use conventional commits
- 提交前进行代码检查 | Run code checks before commit
- 保持提交信息清晰简洁 | Keep commit messages clear and concise

## 测试 | Testing

```bash
# 运行单元测试 | Run unit tests
npm run test:unit

# 运行端到端测试 | Run end-to-end tests
npm run test:e2e
```

## 部署 | Deployment

### 构建生产版本 | Build for Production

```bash
# 构建生产版本 | Build production version
npm run build

# 预览生产构建 | Preview production build
npm run preview
```

### Nginx配置示例 | Nginx Configuration Example

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        root /path/to/dist;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
}
```

## 常见问题 | FAQ

1. 如何配置API地址？| How to configure API address?
2. 如何处理跨域问题？| How to handle CORS issues?
3. 如何自定义主题？| How to customize theme?
4. 如何集成新的图表库？| How to integrate new chart libraries?

## 参与贡献 | Contributing

我们欢迎对项目的贡献！请参阅贡献指南。

We welcome contributions! Please see the contributing guidelines.

## 许可证 | License

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 相关项目 | Related Projects

- [SeaFogWatch-Backend](https://github.com/yourusername/SeaFogWatch-Backend) - 后端服务 | Backend service
- [SeaFogWatch-Detection](https://github.com/yourusername/SeaFogWatch-Detection) - 检测服务 | Detection service

## 联系方式 | Contact

如有问题和建议，请在GitHub仓库中提出Issue或直接联系维护者。

For questions and support, please open an issue in the GitHub repository or contact the maintainers directly. 