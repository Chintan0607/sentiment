
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Sentiment Analyzer", page_icon="🎯")

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment"
    )

sentiment_pipeline = load_model()

st.title(" Review Sentiment Analyzer")

st.write("Enter a customer review from Zomato, Swiggy, or any e-commerce platform to predict its sentiment.")

user_review = st.text_area("Enter the review here:", height=150)

if st.button("Predict Sentiment"):
    if user_review.strip() == "":
        st.warning("Please enter a review to analyze!")
    else:
        with st.spinner('Analyzing...'):
            result = sentiment_pipeline(user_review)[0]
            label = result['label']
            score = round(result['score'], 2)

        # Show result
        st.success(f"**Sentiment:** {label}")
        st.info(f"**Confidence:** {score}")
