import nltk
import numpy as np

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


def text_summarization(text):
    # Preprocess the text
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(text)
    processed_sentences = []

    for sentence in sentences:
        words = [
            word.lower()
            for word in sentence.split()
            if word.lower() not in stop_words
        ]
        processed_sentences.append(' '.join(words))

    # Calculate sentence importance using TF-IDF
    vectorizer = TfidfVectorizer()
    sentence_tfidf = vectorizer.fit_transform(processed_sentences)
    sentence_scores = np.array(sentence_tfidf.sum(axis=1)).ravel()

    # Select top sentences based on importance scores
    num_sentences = max(1, int(0.2 * len(sentences)))

    top_indices = sentence_scores.argsort()[-num_sentences:]

    top_sentences = [sentences[i] for i in top_indices]

    # Generate the summary
    summary = ' '.join(top_sentences)

    return summary


# Example usage
text = "The quick brown fox jumps over the lazy dog. The dog barks at the fox. The fox runs away."

summary = text_summarization(text)

print(summary)

# run "python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"