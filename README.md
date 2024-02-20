Apple Quality Prediction using Support Vector Classifier
This repository contains code for predicting the quality of apples using Support Vector Classifier (SVC). The steps performed in this project are as follows:

Data Collection: The dataset was fetched from Kaggle notebook.

Exploratory Data Analysis (EDA): EDA was performed on the dataset to understand its structure and characteristics. This involved handling missing values, converting object data types to integer data types, and converting the "Quality" column to integer type by mapping "Good quality" to 0 and "Bad quality" to 1.

Data Splitting: The dataset was split into independent and dependent features. Independent features include Size, Weight, Sweetness, Crunchiness, Juiciness, Ripeness, and Acidity, while the dependent feature is Quality.

Data Splitting: The dataset was further split into training and testing data.

Model Training: Support Vector Classifier (SVC) was used for model training with a linear kernel. An accuracy score of 75% was achieved.

Hyperparameter Tuning: Hyperparameter tuning was performed, and the best parameters were found to be C = 10, gamma = 0.1, and kernel: rbf.

Model Training with Best Parameters: The model was trained with the best parameters, and an accuracy of 91% was achieved.

Model Serialization: The trained model was serialized and stored in a pickle file.

Streamlit Web App: A Streamlit web app was created to provide a user interface for predicting apple quality using the trained model stored in the pickle file. The user can input features through the web app, and the predicted quality is displayed.

Deployment: The web app was deployed on Streamlit Cloud.
