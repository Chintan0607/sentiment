# Review Sentiment Analyzer 🎯

This is a simple **Sentiment Analysis Web App** built with [Streamlit](https://streamlit.io/) and [Hugging Face Transformers](https://huggingface.co/transformers/). The app uses a pre-trained sentiment analysis model to predict the sentiment of customer reviews from platforms like Zomato, Swiggy, or any e-commerce platform.

## Features
- Analyze customer reviews to predict their sentiment.
- Leverages the `nlptown/bert-base-multilingual-uncased-sentiment` model from Hugging Face.
- Provides a confidence score for the prediction.

## How to Use
1. Enter a customer review in the text area.
2. Click on the **Predict Sentiment** button.


## Installation

### Prerequisites
- Python 3.8 or later
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Chintan0607/sentiment.git
   cd sentiment
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`.

## File Structure
- `app.py`: Main application file containing the Streamlit code.
- `requirements.txt`: List of dependencies for the project.
- `README.md`: Project documentation.

## Dependencies
- `streamlit`: Web framework for building the UI.
- `transformers`: Hugging Face library for NLP models.

Install the dependencies using:
```bash
pip install streamlit transformers
```

## Model Details
The app uses the `nlptown/bert-base-multilingual-uncased-sentiment` model from Hugging Face. This model is fine-tuned for sentiment analysis and supports multiple languages.


## Contributing
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
```
