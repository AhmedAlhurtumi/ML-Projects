# Diabetes Prediction using SVM

This project uses a Support Vector Machine (SVM) model to predict whether a person is likely to have diabetes based on various health-related attributes. The goal is to build an accurate classifier that can assist in early detection of diabetes.

## Dataset

The dataset used is the **Pima Indians Diabetes Dataset**, which contains medical data of female patients of Pima Indian heritage.

- Total Instances: 768
- Features include:
  - Number of pregnancies
  - Glucose level
  - Blood pressure
  - Skin thickness
  - Insulin level
  - BMI
  - Diabetes pedigree function
  - Age
- Target: 1 (Diabetic) or 0 (Non-diabetic)

## Project Structure

- `diabetes_prediction.ipynb` – Main notebook containing data exploration, preprocessing, model training, and evaluation
- `diabetes.csv` – Dataset file
- `requirements.txt` – Python dependencies

## ML Approach

- **Model Used:** Support Vector Machine (SVM)
- **Evaluation Metrics:** Accuracy, Confusion Matrix, Precision, Recall, F1-Score

