# SeaFogWatch Detection Service

[简体中文](./README-Detection.md) | English

A deep learning-based sea fog detection service, the core algorithm implementation of the SeaFogWatch system. This project utilizes the state-of-the-art MP-Former (CVPR 2023) model architecture, combining CSWin Transformer and Agent Attention mechanisms to achieve high-precision sea fog detection.

## Overview

This project is the detection service component of the SeaFogWatch system, implementing automatic sea fog detection in satellite imagery using deep learning technology. Built with Python, it integrates image processing and deep learning models to provide high-accuracy sea fog recognition capabilities.

### Key Features

- Sea Fog Detection: High-precision recognition based on MP-Former model
- Satellite Image Preprocessing: Support for multi-spectral satellite data (NetCDF format)
- Multi-Model Ensemble Prediction: Model ensemble support for improved stability
- Detection Result Post-processing: Including geocoding and visualization
- Batch Data Processing: Support for large-scale satellite image batch processing
- REST API Service: Standardized detection service interface

### Model Features

- Based on MP-Former architecture (CVPR 2023)
- Integration of CSWin Transformer and Agent Attention
- Multi-scale feature extraction support
- Efficient local-global attention mechanism
- Position-aware feature learning

## Technology Stack

- Python 3.8+
- PyTorch 1.10+
- OpenCV
- NumPy/Pandas
- FastAPI/Flask
- GDAL 3.4.1
- netCDF4

## Development Environment

### System Requirements

- CUDA 11.0+ (Recommended)
- 16GB+ RAM
- 50GB+ Disk Space
- Linux/Windows OS

### Python Environment Setup

Recommended to use Anaconda for environment management:

```bash
# Create environment
conda create -n seafog python=3.8

# Activate environment
conda activate seafog

# Install GDAL
conda install -c conda-forge gdal=3.4.1

# Install other dependencies
pip install -r requirements.txt
```

## Quick Start

### Prerequisites

1. Install CUDA and cuDNN
2. Install Anaconda or Miniconda
3. Download pre-trained models

### Installation Steps

1. Clone repository
```bash
git clone https://github.com/yourusername/SeaFogWatch-Detection.git
cd SeaFogWatch-Detection
```

2. Create and activate environment
```bash
conda create -n seafog python=3.8
conda activate seafog
```

3. Install dependencies
```bash
conda install -c conda-forge gdal=3.4.1
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env file to configure necessary parameters
```

### Usage

1. Start API service
```bash
python api.py
```

2. Single detection
```bash
python predict.py --input path/to/image.nc --output path/to/result
```

3. Batch detection
```bash
python eval_batch.py --input path/to/images --output path/to/results
```

## API Documentation

### REST API Endpoints

#### 1. File Upload Detection
- Endpoint: `POST /process_nc`
- Function: Process uploaded NetCDF file and perform detection
- Parameters:
  - `file`: NetCDF file
  - `lon_min`, `lon_max`, `lat_min`, `lat_max`: Geographic range

#### 2. Path Detection
- Endpoint: `POST /process_nc_path`
- Function: Process NetCDF file at specified path
- Parameters:
  - `file_path`: File path
  - `lon_min`, `lon_max`, `lat_min`, `lat_max`: Geographic range

#### 3. Model Detection
- Endpoint: `POST /detect`
- Function: Perform detection using specified model
- Parameters:
  - `image_path`: Image path
  - `model_path`: Model path

## Model Description

### Architecture

- Base Network: CSWin Transformer
- Attention Mechanism: Agent Attention
- Feature Extraction: Multi-scale feature fusion
- Detection Head: Mask-Piloted Transformer

### Training Data

- Data Source: Himawari Satellite
- Data Format: NetCDF
- Spectral Bands: Visible and infrared bands
- Annotation Type: Pixel-level annotation

### Performance

- Detection Accuracy: AP 40.15 (12 epochs)
- Processing Speed: Supports real-time processing
- Supported Resolution: 384x384 to 2560x2560

## Development Guide

### Code Standards

- Follow PEP 8 standards
- Use pylint for code checking
- Write unit tests

### Model Development

1. Data Preprocessing
```python
# Example code
def preprocess_data(nc_file):
    # Data preprocessing logic
    pass
```

2. Model Training
```python
# Training script example
bash run_50ep_no_noise_all_ly.sh
```

3. Model Evaluation
```python
# Evaluation script example
bash eval.sh
```

## Testing

```bash
# Run unit tests
pytest tests/

# Run integration tests
pytest tests/integration/

# Check code quality
pylint app/
```

## Deployment

### Docker Deployment

```bash
# Build image
docker build -t seafog-detection .

# Run container
docker run -p 8000:8000 seafog-detection
```

### Production Configuration

- Use gunicorn as WSGI server
- Configure supervisor for process management
- Set up logging

## FAQ

1. How to handle large satellite images?
   - Use sliding window for block processing
   - Set appropriate batch size

2. How to improve detection accuracy?
   - Use model ensemble
   - Adjust post-processing parameters
   - Increase training data diversity

3. How to optimize processing speed?
   - Use GPU acceleration
   - Enable batch processing mode
   - Optimize image preprocessing pipeline

4. How to fine-tune models?
   - Prepare domain-specific data
   - Adjust learning rate and training parameters
   - Use transfer learning strategies

## Contributing

We welcome contributions! Please see the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this project in your research, please cite:

```bibtex
@inproceedings{mpformer2023,
  title={MP-Former: Mask-Piloted Transformer for Image Segmentation},
  author={Your Name},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2023}
}
```

## Contact

For questions and support, please open an issue in the GitHub repository or contact the maintainers directly. 