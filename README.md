# Drug Recommendation System using DVC

A machine learning project that implements a drug recommendation system using Data Version Control (DVC) for better experiment tracking and reproducibility.

## 📋 Project Overview

This project implements a machine learning pipeline for drug recommendation using a Random Forest Classifier. The system processes medical data, trains a model, and provides drug recommendations based on patient characteristics.

## 🚀 Features

- Data ingestion and preprocessing pipeline
- Automated data versioning using DVC
- Random Forest Classifier for drug recommendations
- Comprehensive logging system
- Model evaluation metrics tracking
- Reproducible experiments

## 🛠️ Tech Stack

- Python 3.x
- DVC (Data Version Control)
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Drug-Recomendation-using-DVC.git
cd Drug-Recomendation-using-DVC
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
Drug-Recomendation-using-DVC/
├── data/
│   ├── Raw/              # Raw data files
│   ├── clean_data/       # Cleaned data
│   └── interim/          # Processed data
├── models/               # Trained models
├── reports/             # Evaluation metrics
├── logs/                # Log files
├── src/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── model_building.py
│   └── model_evaluation.py
├── dvc.yaml            # DVC pipeline configuration
├── requirements.txt    # Project dependencies
└── README.md
```

## 🔄 Pipeline Stages

The project follows a DVC pipeline with the following stages:

1. **Data Ingestion**
   - Loads raw data
   - Splits into train and test sets
   - Saves cleaned data

2. **Data Preprocessing**
   - Handles categorical features
   - Removes duplicates
   - Performs feature encoding

3. **Model Building**
   - Trains Random Forest Classifier
   - Saves trained model

4. **Model Evaluation**
   - Evaluates model performance
   - Generates metrics report

## 🏃‍♂️ Usage

1. Run the complete pipeline:
```bash
dvc repro
```

2. Run individual stages:
```bash
dvc repro data_ingestion
dvc repro data_preprocessing
dvc repro model_building
dvc repro model_evaluation
```

## 📊 Model Performance

The model is evaluated using the following metrics:
- Accuracy
- Precision
- Recall
- AUC-ROC

Detailed metrics can be found in `reports/metrics.json`.

## 📝 Logging

The project implements comprehensive logging:
- Log files are stored in the `logs/` directory
- Each stage has its own log file
- Logs include timestamps, log levels, and detailed messages

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- ZAIN - Initial work

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Special thanks to the DVC team for their excellent tool
