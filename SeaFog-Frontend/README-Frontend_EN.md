# SeaFogWatch Frontend

[简体中文](./README-Frontend.md) | English

Frontend application for SeaFogWatch system, providing visualization interface for sea fog monitoring and analysis.

## Overview

This is the frontend part of the SeaFogWatch sea fog detection system, built with Vue.js and Element Plus. It provides an intuitive user interface for sea fog data visualization, real-time monitoring, and historical data analysis.

### Key Features

- Sea Fog Image Management
  - Support automatic/manual collection of sea fog satellite images
  - True color and false color image preview
  - Image metadata management (coordinates, capture time, etc.)
  
- Sea Fog Detection
  - Support single/batch image detection
  - Real-time detection progress display
  - Detection result visualization

- Data Analysis
  - Historical data query and analysis
  - Data visualization and charts
  - Detection result statistics

- System Management
  - User permission and role management
  - System parameter configuration
  - Operation log recording

## Technology Stack

- Vue 3.x - Progressive JavaScript Framework
- Vite - Next Generation Frontend Build Tool
- Element Plus - Vue 3 Based Component Library
- Pinia - Vue 3 State Management Solution
- Vue Router - Official Router
- Axios - HTTP Client
- ECharts - Data Visualization Library
- STOMP + SockJS - WebSocket Communication

## Development Environment

- Node.js >= 16
- npm >= 7 or yarn >= 1.22
- VSCode (Recommended)

## Quick Start

### Prerequisites

```bash
# Check Node.js version
node -v

# Check npm version
npm -v
```

### Installation and Running

1. Clone repository
```bash
git clone https://github.com/yourusername/SeaFogWatch-Frontend.git
cd SeaFogWatch-Frontend
```

2. Install dependencies
```bash
npm install
# or use yarn
yarn install
```

3. Configure environment variables
```bash
# Copy environment template
cp .env.development .env.local

# Edit configuration
vim .env.local
```

4. Start development server
```bash
npm run dev
# or use yarn
yarn dev
```

5. Build for production
```bash
npm run build
# or use yarn
yarn build
```

## Project Structure

```
SeaFogWatch-Frontend/
├── public/              # Static assets
├── src/
│   ├── api/            # API interface definitions
│   │   ├── detection/  # Detection related APIs
│   │   └── system/     # System management APIs
│   ├── assets/         # Project assets
│   ├── components/     # Common components
│   ├── hooks/          # Composition functions
│   ├── layout/         # Layout components
│   ├── router/         # Route configurations
│   ├── store/          # State management
│   ├── styles/         # Global styles
│   ├── utils/          # Utility functions
│   ├── views/          # Page components
│   │   ├── detection/  # Detection related pages
│   │   └── system/     # System management pages
│   ├── App.vue         # Root component
│   └── main.js         # Entry file
├── .env.development    # Development environment config
├── .env.production     # Production environment config
├── package.json        # Project configuration
└── vite.config.js      # Vite configuration
```

## Development Guide

### Coding Standards

- Use ESLint + Prettier for code standardization and formatting
- Follow Vue 3 Composition API best practices
- Use type declarations for components and functions
- Maintain code simplicity and maintainability

### Commit Standards

Commit message format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- style: Formatting
- refactor: Code refactoring
- test: Testing
- chore: Build process or auxiliary tool changes

### Branch Management

- main: Main branch for production
- develop: Development branch
- feature/*: Feature branches
- hotfix/*: Emergency fix branches

## Deployment Guide

### Build for Production

```bash
# Build production version
npm run build

# Preview production build
npm run preview
```

### Nginx Configuration Example

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        root /path/to/dist;
        index index.html;
        try_files $uri $uri/ /index.html;
    }

    # WebSocket proxy configuration
    location /ws {
        proxy_pass http://backend-server;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

## FAQ

1. How to configure backend API address?
   - Set VITE_APP_BASE_API variable in .env.local file

2. How to handle WebSocket connection issues?
   - Check WebSocket proxy configuration
   - Ensure backend service is running
   - Check browser console for error messages

3. How to customize theme?
   - Modify src/styles/variables.scss file
   - Use Element Plus theme configuration features

4. What to do when image upload fails?
   - Check if file size exceeds limit
   - Verify supported file formats
   - Check network request status

## Contributing

1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [SeaFogWatch-Backend](https://github.com/yourusername/SeaFogWatch-Backend) - Backend service
- [SeaFogWatch-Detection](https://github.com/yourusername/SeaFogWatch-Detection) - Detection service

## Contact

For questions and suggestions, please open an issue in the GitHub repository or contact the maintainers directly. 