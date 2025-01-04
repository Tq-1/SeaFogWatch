# SeaFogWatch Frontend | 海雾监测系统前端

[English](./README-Frontend_EN.md) | 简体中文

SeaFogWatch系统的前端应用，提供海雾监测和分析的可视化界面。

## 项目简介

本项目是SeaFogWatch海雾监测系统的前端部分，基于Vue.js和Element Plus构建。提供直观的用户界面，实现海雾数据的可视化展示、实时监控和历史数据分析等功能。

### 主要功能

- 海雾图像管理
  - 支持自动/手动采集海雾卫星图像
  - 提供真彩色和伪彩色图像预览
  - 图像元数据管理（经纬度、采集时间等）
  
- 海雾检测
  - 支持单张/批量图像检测
  - 实时检测进度展示
  - 检测结果可视化

- 数据分析
  - 历史数据查询和分析
  - 数据可视化和图表展示
  - 检测结果统计分析

- 系统管理
  - 用户权限和角色管理
  - 系统参数配置
  - 操作日志记录

## 技术栈

- Vue 3.x - 渐进式JavaScript框架
- Vite - 新一代前端构建工具
- Element Plus - 基于Vue 3的组件库
- Pinia - Vue 3的状态管理方案
- Vue Router - 官方路由管理器
- Axios - HTTP 客户端
- ECharts - 数据可视化图表库
- STOMP + SockJS - WebSocket通信

## 开发环境要求

- Node.js >= 16
- npm >= 7 或 yarn >= 1.22
- VSCode (推荐)

## 快速开始

### 环境准备

```bash
# 检查Node.js版本
node -v

# 检查npm版本
npm -v
```

### 安装和运行

1. 克隆仓库
```bash
git clone https://github.com/yourusername/SeaFogWatch-Frontend.git
cd SeaFogWatch-Frontend
```

2. 安装依赖
```bash
npm install
# 或使用yarn
yarn install
```

3. 配置环境变量
```bash
# 复制环境变量模板
cp .env.development .env.local

# 编辑配置文件
vim .env.local
```

4. 启动开发服务器
```bash
npm run dev
# 或使用yarn
yarn dev
```

5. 构建生产版本
```bash
npm run build
# 或使用yarn
yarn build
```

## 项目结构

```
SeaFogWatch-Frontend/
├── public/              # 静态资源
├── src/
│   ├── api/            # API接口定义
│   │   ├── detection/  # 检测相关接口
│   │   └── system/     # 系统管理接口
│   ├── assets/         # 项目资源文件
│   ├── components/     # 通用组件
│   ├── hooks/          # 组合式函数
│   ├── layout/         # 布局组件
│   ├── router/         # 路由配置
│   ├── store/          # 状态管理
│   ├── styles/         # 全局样式
│   ├── utils/          # 工具函数
│   ├── views/          # 页面组件
│   │   ├── detection/  # 检测相关页面
│   │   └── system/     # 系统管理页面
│   ├── App.vue         # 根组件
│   └── main.js         # 入口文件
├── .env.development    # 开发环境配置
├── .env.production     # 生产环境配置
├── package.json        # 项目配置
└── vite.config.js      # Vite配置
```

## 开发指南

### 编码规范

- 使用ESLint + Prettier进行代码规范和格式化
- 遵循Vue 3组合式API最佳实践
- 组件和函数使用类型声明
- 保持代码简洁和可维护性

### 提交规范

提交信息格式：
```
<type>(<scope>): <subject>

<body>

<footer>
```

类型（type）：
- feat: 新功能
- fix: 修复
- docs: 文档
- style: 格式
- refactor: 重构
- test: 测试
- chore: 构建过程或辅助工具的变动

### 分支管理

- main: 主分支，用于生产环境
- develop: 开发分支
- feature/*: 功能分支
- hotfix/*: 紧急修复分支

## 部署指南

### 构建生产版本

```bash
# 构建生产版本
npm run build

# 预览生产构建
npm run preview
```

### Nginx配置示例

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        root /path/to/dist;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # WebSocket代理配置
    location /ws {
        proxy_pass http://backend-server;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

## 常见问题

1. 如何配置后端API地址？
   - 在.env.local文件中设置VITE_APP_BASE_API变量

2. 如何处理WebSocket连接问题？
   - 检查WebSocket代理配置
   - 确保后端服务正常运行
   - 查看浏览器控制台错误信息

3. 如何自定义主题？
   - 修改src/styles/variables.scss文件
   - 使用Element Plus的主题配置功能

4. 图像上传失败怎么办？
   - 检查文件大小是否超出限制
   - 确认文件格式是否支持
   - 查看网络请求状态

## 参与贡献

1. Fork 项目
2. 创建功能分支 (git checkout -b feature/AmazingFeature)
3. 提交更改 (git commit -m 'Add some AmazingFeature')
4. 推送到分支 (git push origin feature/AmazingFeature)
5. 创建Pull Request

## 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 相关项目

- [SeaFogWatch-Backend](https://github.com/yourusername/SeaFogWatch-Backend) - 后端服务
- [SeaFogWatch-Detection](https://github.com/yourusername/SeaFogWatch-Detection) - 检测服务

## 联系方式

如有问题和建议，请在GitHub仓库中提出Issue或直接联系维护者。 