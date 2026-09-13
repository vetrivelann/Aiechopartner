# 🤖 AI Echo – Sentiment Analysis Dashboard

AI Echo is a **Machine Learning and Natural Language Processing (NLP) based sentiment analysis application** developed using **Python and Streamlit**.

The application analyzes customer reviews and predicts their sentiment using a trained **Naive Bayes machine learning model** with **TF-IDF vectorization**.

Along with live sentiment prediction, the application provides different analytical views to understand customer sentiment based on:

- Sentiment
- Ratings
- Platform
- Verified Purchase

---

## 📌 Problem Statement

Customer reviews contain valuable information about customer opinions, experiences, and satisfaction.

However, when a large number of reviews are available, manually analyzing each review becomes difficult, time-consuming, and inefficient.

There is a need for an automated system that can:

- Analyze customer review text.
- Identify whether a review is Positive or Negative.
- Provide an easy way to perform sentiment prediction.
- Understand the overall sentiment distribution of reviews.
- Analyze the relationship between ratings and sentiment.
- Compare sentiment across different platforms.
- Analyze sentiment based on verified purchases.

AI Echo addresses this problem by using **Natural Language Processing and Machine Learning** to automatically analyze customer reviews.

---

## 💡 Proposed Solution

AI Echo provides an interactive sentiment analysis dashboard built using **Streamlit**.

The system uses a trained **Naive Bayes classifier** and **TF-IDF vectorizer** to process review text and predict its sentiment.

The application also uses a cleaned review dataset to provide different analytical views through an interactive sidebar.

The system contains the following major components:

1. Review text preprocessing
2. TF-IDF feature transformation
3. Naive Bayes sentiment prediction
4. Sentiment distribution analysis
5. Rating distribution analysis
6. Platform-wise sentiment analysis
7. Verified purchase sentiment analysis

---

## ✨ Features

### 🔍 1. Live Sentiment Prediction

Users can enter a review into the application.

The system:

1. Accepts the review text.
2. Cleans the text.
3. Converts the text into TF-IDF features.
4. Passes the features to the trained Naive Bayes model.
5. Predicts the sentiment.

The predicted result is displayed as:

- Positive
- Negative
- Other/unknown result if applicable

---

### 📊 2. Sentiment Distribution

This module displays the distribution of sentiments present in the review dataset.

It provides:

- Sentiment counts
- Bar chart visualization
- Data table containing sentiment counts

This helps understand the overall sentiment pattern in the dataset.

---

### ⭐ 3. Rating Distribution

The application analyzes the distribution of customer ratings.

It provides:

- Rating-wise counts
- Bar chart visualization
- Rating distribution table

This helps understand how customers have rated the products or services.

---

### 💻 4. Platform Analysis

The application compares platforms with customer sentiment.

It uses a cross-tabulation between:

- Platform
- Sentiment

The result is displayed using:

- Bar chart
- Data table

This helps identify sentiment patterns across different platforms.

---

### ✅ 5. Verified Purchase Analysis

The application analyzes sentiment based on verified purchase information.

It compares:

- Verified purchase status
- Sentiment

The result is displayed using a bar chart and data table.

---

### 📥 6. Dataset Download

Users can download the cleaned review dataset directly from the Streamlit sidebar.

The downloaded file is:

```text
clean_reviews.csv
