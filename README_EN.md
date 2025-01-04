# SeaFogWatch - Sea Fog Detection System

[简体中文](./README.md) | English

A comprehensive sea fog detection and monitoring system based on satellite imagery analysis and machine learning.

<p align="center">
  <!-- Add project logo or screenshot here -->
</p>

## Overview

SeaFogWatch is an integrated system for monitoring and detecting sea fog using Himawari satellite data. The system processes satellite imagery through advanced machine learning algorithms to provide real-time sea fog detection and analysis. Built with a microservices architecture, it combines Python deep learning models with a robust backend and frontend to provide a complete sea fog monitoring solution.

### Key Features

- Real-time sea fog detection using satellite imagery
- Automated Himawari satellite data collection
- Support for both true color and false color image processing
- Interactive visualization of detection results
- Historical data analysis and trend tracking
- Complete RESTful API interface

## System Architecture

The system consists of three main components:

### 1. Backend Service (Current Repository)

- Built with Spring Boot
- Handles data management and system operations
- Provides RESTful APIs
- Manages user authentication and authorization
- Coordinates with detection service

Technology Stack:
- Java 8+
- Spring Boot
- MyBatis
- WebSocket
- Redis
- MySQL

### 2. Frontend Application (To be implemented)

- User interface
- Real-time detection results display
- Admin dashboard
- Data analysis tools

Technology Stack:
- Vue.js
- Element UI
- ECharts
- WebSocket client

### 3. Sea Fog Detection Service (To be implemented)

- Satellite image processing
- Machine learning model implementation
- Sea fog detection algorithms
- Analysis results generation

Technology Stack:
- Python
- Deep Learning frameworks
- Image processing libraries
- Scientific computing tools

## Getting Started

### Prerequisites

- JDK 1.8+
- Maven 3.6+
- MySQL 5.7+
- Redis
- Python 3.8+ (for detection service)
- Node.js 14+ (for frontend)

### Backend Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/SeaFogWatch.git
cd SeaFogWatch
```

2. Configure database
```bash
# Update database settings in application.yml
```

3. Build and run
```bash
mvn clean install
java -jar seafog-admin/target/seafog-admin.jar
```

### Frontend Setup (Coming Soon)

Frontend deployment instructions will be provided in the frontend repository.

### Detection Service Setup (Coming Soon)

Detection service deployment instructions will be provided in the detection service repository.

## API Documentation

The backend service provides the following main API endpoints:

- `/api/detection/image/*` - Image management endpoints
- `/api/detection/collect/*` - Data collection endpoints
- `/api/detection/analysis/*` - Analysis result endpoints

Detailed API documentation is available through Swagger UI at `http://localhost:8080/swagger-ui.html`

## Project Structure

```
SeaFogWatch/
├── seafog-admin/        # System administration module
├── seafog-framework/    # Framework core
├── seafog-system/      # System management
├── seafog-quartz/      # Task scheduling
├── seafog-generator/   # Code generation
├── seafog-common/      # Common utilities
└── seafog-detection/   # Sea fog detection module
```

## Contributing

We welcome contributions to SeaFogWatch! Please read our contributing guidelines before submitting pull requests.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- RuoYi Vue framework
- Himawari Satellite data service
- Contributors and supporters

## Contact

For questions and support, please open an issue in the GitHub repository or contact the maintainers directly.

---

**Note:** This is the backend service repository. For the frontend application and detection service, please refer to their respective repositories (links to be added). 