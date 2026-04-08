# ⚠️ **MLOps Pipeline Notice**

> **Note:** This project is actively maintained for Azure MLOps demonstrations. For production use, please ensure you have proper Azure subscription and permissions.

---

# Azure MLOps Pipeline

## CI/CD Status

[![GitHub Actions Workflow Status](https://img.shields.io/badge/GitHub%20Actions-Repo%20not%20found-lightgrey)](https://github.com/yourusername/azure-mlops-pipeline/actions)
[![Azure ML Deployment](https://img.shields.io/badge/Azure%20ML-Deployed-success)](https://ml.azure.com)
[![Python Version](https://img.shields.io/badge/python-3.10-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

**Azure Portal** · [Documentation](#) · [Report Issue](#) · [Examples](#)

---

## 📋 Overview

This project demonstrates a **production-ready MLOps pipeline** using:

- **Azure Machine Learning** – model training, registration, and deployment
- **GitHub Actions** – CI/CD automation
- **scikit-learn** – model development
- **Python 3.10** – core language

The pipeline handles:

- ✅ Automated testing on PR
- ✅ Model training on Azure ML compute
- ✅ Model versioning and registry
- ✅ Deployment to ACI/AKS endpoints
- ✅ Monitoring and data drift detection

---

## 🚀 Quick Start

### Prerequisites

- Azure subscription ([free trial](https://azure.microsoft.com/free/))
- GitHub account
- Python 3.10+

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/azure-mlops-pipeline.git
cd azure-mlops-pipeline

# Install dependencies
pip install -r requirements.txt

# Configure Azure CLI
az login
az account set --subscription "your-subscription-id"

# Run training locally (with sample data)
python src/train.py --data_path data/sample_data.csv