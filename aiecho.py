import streamlit as st
import pandas as pd
import joblib
import re
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Echo — Sentiment Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Echo — Sentiment Analysis Dashboard")

# -----------------------------
# SAFE FILE LOADING
# -----------------------------
st.write("Loading project files...")

required_files = [
    "sentiment_nb_model.pkl",
    "tfidf_vectorizer.pkl",
    "clean_reviews.csv"
]

for f in required_files:
    if not os.path.exists(f):
        st.error(f"Missing file: {f}")
        st.stop()

model = joblib.load("sentiment_nb_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")
df = pd.read_csv("clean_reviews.csv")

st.success("All files loaded successfully ✅")

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "🔍 Live Sentiment Predictor",
        "📊 Sentiment Distribution",
        "⭐ Rating Distribution",
        "💻 Platform Analysis",
        "✅ Verified Purchase Analysis"
    ]
)

# -----------------------------
# SIDEBAR DOWNLOAD BUTTON
# -----------------------------
st.sidebar.header("Download Data")

csv_data = df.to_csv(index=False).encode("utf-8")

st.sidebar.download_button(
    label="📥 Download Clean Reviews",
    data=csv_data,
    file_name="clean_reviews.csv",
    mime="text/csv"
)

# -----------------------------
# TEXT CLEAN FUNCTION (same as training)
# -----------------------------
def clean_text(text):
    text = str(text)

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # 3. Remove numbers
    text = re.sub(r'\d+', '', text)

    # 4. Remove special characters & symbols
    text = re.sub(r'[^a-z\s]', '', text)

    # 5. Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# =====================================================
# PAGE 1 — LIVE SENTIMENT PREDICTOR
# =====================================================
if menu == "🔍 Live Sentiment Predictor":

    st.header("Enter Review Text")

    user_input = st.text_area("Type a review here")

    if st.button("Predict Sentiment"):

        if user_input.strip() == "":
            st.warning("Please enter text")
        else:
            cleaned = clean_text(user_input)
            vec = tfidf.transform([cleaned])
            pred = model.predict(vec)[0]

            if pred == "Positive":
                st.success(f"Predicted Sentiment: {pred}")
            elif pred == "Negative":
                st.error(f"Predicted Sentiment: {pred}")
            else:
                st.warning(f"Predicted Sentiment: {pred}")


# =====================================================
# PAGE 2 — SENTIMENT DISTRIBUTION
# =====================================================
elif menu == "📊 Sentiment Distribution":

    st.header("Sentiment Distribution")

    counts = df["sentiment"].value_counts()

    st.bar_chart(counts)
    st.dataframe(counts)


# =====================================================
# PAGE 3 — RATING DISTRIBUTION
# =====================================================
elif menu == "⭐ Rating Distribution":

    st.header("Rating Distribution")

    rating_counts = df["rating"].value_counts().sort_index()

    st.bar_chart(rating_counts)
    st.dataframe(rating_counts)


# =====================================================
# PAGE 4 — PLATFORM ANALYSIS
# =====================================================
elif menu == "💻 Platform Analysis":

    st.header("Platform vs Sentiment")

    cross = pd.crosstab(df["platform"], df["sentiment"])

    st.bar_chart(cross)
    st.dataframe(cross)


# =====================================================
# PAGE 5 — VERIFIED PURCHASE ANALYSIS
# =====================================================
elif menu == "✅ Verified Purchase Analysis":

    st.header("Verified Purchase vs Sentiment")

    cross = pd.crosstab(df["verified_purchase"], df["sentiment"])

    st.bar_chart(cross)
    st.dataframe(cross)
