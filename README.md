# MLOps Project: Modular Pipeline for ML Lifecycle

This repository contains my first structured MLOps project where I took a traditional Jupyter workflow and turned it into a modular, reproducible, and scalable machine learning pipeline.

---

## 🚀 Project Overview

This project takes a dataset through the full ML lifecycle:

* Data ingestion
* Validation
* Transformation
* Model training
* Evaluation
* Deployment via Flask API

The entire pipeline is built using object-oriented programming, YAML configurations, and clearly separated modules.

---

## 📁 Project Structure

```
.
├── artifacts/                  # Stores all output from pipeline stages
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
│
├── config/
│   └── config.yaml             # Central configuration for all pipeline stages
│
├── logs/
│   └── running_logs.log        # Central log file
│
├── research/                   # Jupyter notebooks used for exploration
│
├── src/                        # Source code for all components
│   ├── components/             # Execution logic for each stage
│   ├── config/                 # ConfigurationManager class
│   ├── constants/              # Shared constants
│   ├── entity/                 # Dataclass config schemas
│   ├── pipeline/               # How components run together
│   └── utils/                  # Common helper functions
│
├── schema.yaml                 # Defines expected data schema
├── params.yaml                 # Model training hyperparameters
├── main.py                     # Runs the full pipeline
├── app.py                      # Flask API to serve model
└── template.py                 # Script to auto-generate project folders
```

---

## ⚙️ How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/NiranJosh101/mlops_basic_project.git
cd mlops_basic_project
```

### 2. Set Up Environment

```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline

```bash
python main.py
```

### 4. Serve Model via API

```bash
python app.py
```

Then open your browser or API tool and POST to `http://localhost:5000/predict`

---

## 🧠 What I Learned

* How to modularize code using OOP principles
* The value of separating config from logic (using YAML)
* How to think more like an engineer than just a data scientist
* How to lay a foundation for reusable, production-like workflows

Big thanks to [Krish Naik](https://www.youtube.com/@KrishNaik) for the helpful content and repo inspiration!

---

## 📌 TODO

* [ ] Add unit tests
* [ ] Integrate MLflow for experiment tracking
* [ ] Dockerize the API
* [ ] Add CI/CD pipeline with GitHub Actions

---

## 📬 Contact

Feel free to reach out if you have questions, suggestions, or want to collaborate!

\[Josh Niran] – \[[hello@niranjosh.pro]]

---

### ⭐ If this project helped you or inspired your own structure, feel free to star it!
