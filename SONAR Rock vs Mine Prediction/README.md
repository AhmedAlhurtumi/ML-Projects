# Rock vs Mine Prediction using Sonar Data

This project uses a Machine Learning model to classify objects as either **rock** or **mine** based on sonar signal data. The dataset contains sonar returns bounced off various surfaces, and the goal is to accurately identify the type of object using these signals.

## Dataset

Contains 208 instances with 60 numerical features representing the energy of sonar signals at different frequencies.

- Features: 60 continuous values
- Target: Rock (R) or Mine (M)

## Project Structure

- `rock_vs_mine.ipynb` – Main notebook containing data preprocessing, model training, and evaluation
- `sonar data.csv` – Dataset file
- `requirements.txt` – Python dependencies

## ML Approach

- **Model Used:** Logistic Regression (can be adjusted based on your implementation)
- **Evaluation Metrics:** Accuracy
