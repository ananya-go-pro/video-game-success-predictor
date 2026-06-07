# Video Game Success Predictor
### Predicting Whether a Video Game Will Be a Commercial Hit
##### Dataset: https://www.kaggle.com/datasets/gregorut/videogamesales

---
### Project Overview

This project uses machine learning to predict whether a video game will become a commercial success based on its platform, genre, publisher, and release year.

A Random Forest Classifier was trained on historical video game sales data to classify games as either:
- Hit (1) - Global sales greater than 1 million units
- Not Hit (0) - Global sales less than or equal to 1 million units

---
### Fields in dataset include
- Rank - Ranking of overall sales
- Name - The games name
- Platform - Platform of the games release (i.e. PC,PS4, etc.)
- Year - Year of the game's release
- Genre - Genre of the game
- Publisher - Publisher of the game
- NA_Sales - Sales in North America (in millions)
- EU_Sales - Sales in Europe (in millions)
- JP_Sales - Sales in Japan (in millions)
- Other_Sales - Sales in the rest of the world (in millions)
- Global_Sales - Total worldwide sales.

---
### Data Cleaning
- Removed rows with missing values and duplicate records before model training.
- Created a binary target variable 'Hit' from Global_Sales
  
---
### Feature Selection
The following features were used for prediction:
- Platform
- Genre
- Publisher
- Year

---
### Data Preprocessing
Categorical features such as Platform, Genre, and Publisher were converted into numerical values using one-hot encoding.

The dataset was then split into:
- 80% Training Data
- 20% Testing Data

---
### Results
Model Performance:
- Accuracy: ~84%
- Precision (Hit Class): 36%
- Recall (Hit Class): 46%

Feature importance analysis showed that release year was the most influential feature in the final model.

---
### Streamlit Demo
The demo allows users to enter:
- Platform
- Genre
- Publisher
- Year

The model then predicts whether the game is likely to be commercially successful.

---
