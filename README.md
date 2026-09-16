# 🤖 AI Echo – Sentiment Analysis Dashboard

AI Echo is a **Machine Learning and Natural Language Processing (NLP) based sentiment analysis application** developed using **Python and Streamlit**.

The application analyzes customer reviews and predicts their sentiment using **TF-IDF feature extraction and a trained Logistic Regression model**.

The dashboard also provides analytical views for **Sentiment, Rating Distribution, Platform Analysis, and Verified Purchase Analysis**, along with an option to download the processed dataset.

---

# ✨ Features

## 🔍 Live Sentiment Prediction

AI Echo allows users to enter a customer review and predict its sentiment in real time.

### Process

1. User enters a review.
2. The review text is cleaned.
3. The text is transformed into TF-IDF features.
4. The trained machine learning model processes the features.
5. The predicted sentiment is displayed.

### Sentiment Classes

- 🟢 Positive
- 🔴 Negative
- 🟡 Neutral

---

## 📊 Sentiment Distribution

The Sentiment Distribution module provides an overview of the sentiment present in the dataset.

It displays:

- Sentiment counts
- Bar chart visualization
- Sentiment summary table

This helps understand the overall sentiment pattern of the available customer reviews.

---

## ⭐ Rating Distribution

The Rating Distribution module analyzes the number of reviews for each customer rating.

It provides:

- Rating-wise counts
- Bar chart visualization
- Rating distribution table

This helps understand how customer ratings are distributed across the dataset.

---

## 💻 Platform Analysis

The Platform Analysis module compares customer sentiment across different platforms.

It uses a cross-tabulation between:

- Platform
- Sentiment

The results are displayed using:

- Bar chart visualization
- Data table

This helps identify sentiment patterns across different platforms.

---

## ✅ Verified Purchase Analysis

The Verified Purchase Analysis module compares customer sentiment based on verified purchase status.

It analyzes:

- Verified Purchase Status
- Sentiment

The results are displayed using:

- Bar chart visualization
- Data table

This helps understand sentiment patterns among verified and non-verified purchases.

---

## 📥 Dataset Download

AI Echo provides an option to download the cleaned and processed review dataset directly from the Streamlit sidebar.

The downloadable dataset is:

```text
clean_reviews.csv
