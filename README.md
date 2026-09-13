# 🤖 AI Echo – Sentiment Analysis Dashboard

AI Echo is a **Machine Learning and Natural Language Processing (NLP) based sentiment analysis application** developed using Python and Streamlit.

The application analyzes customer reviews and predicts their sentiment using a trained **Naive Bayes machine learning model** with **TF-IDF vectorization**.

Along with live sentiment prediction, the application provides different analytical views to understand sentiment distribution, ratings, platforms, and verified purchases.

---

## 📌 Problem Statement

Customer reviews contain valuable information about customer opinions and experiences. However, when a large number of reviews are available, manually analyzing every review becomes difficult and time-consuming.

The objective of this project is to develop an interactive machine learning application that can automatically analyze customer review text and provide sentiment predictions.

The system also provides data analysis features that help understand customer sentiment based on:

- Sentiment
- Rating
- Platform
- Verified Purchase

---

## 🎯 Objectives

The main objectives of the AI Echo project are:

- To preprocess customer review text.
- To clean unnecessary characters and information from reviews.
- To convert text data into numerical features using TF-IDF.
- To use a trained Naive Bayes model for sentiment prediction.
- To predict the sentiment of a new review.
- To visualize the distribution of sentiments.
- To analyze customer ratings.
- To analyze sentiment across different platforms.
- To analyze sentiment based on verified purchases.
- To provide all these features through an interactive Streamlit dashboard.

---

# 🚀 Features

## 🔍 1. Live Sentiment Predictor

The Live Sentiment Predictor allows the user to enter a customer review and obtain a predicted sentiment.

### Workflow

```text
User enters review
        ↓
Text preprocessing
        ↓
TF-IDF transformation
        ↓
Naive Bayes model
        ↓
Predicted sentiment
