# TEXT SUMMARIZATION USING SML

**SML (Statistical Machine Learning)** based extractive text summarization using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

## Overview

This project implements a lightweight text summarization system that identifies and extracts the most important sentences from a given text.

Instead of generating new sentences, the system ranks the original sentences according to their statistical importance and produces a concise summary.

## Key Features

- Statistical Machine Learning approach
- TF-IDF-based sentence scoring
- NLTK sentence tokenization
- English stop-word removal
- Configurable summary length
- No external API or pretrained language model required
- Simple and easy to run locally

## How It Works

The summarizer follows these steps:

1. **Sentence Tokenization** – Splits the input text into individual sentences.
2. **Preprocessing** – Converts words to lowercase and removes common English stop words.
3. **TF-IDF Calculation** – Calculates the importance of terms across the sentences.
4. **Sentence Scoring** – Combines TF-IDF values to assign an importance score to each sentence.
5. **Sentence Selection** – Selects the highest-scoring sentences.
6. **Summary Generation** – Combines the selected original sentences into the final summary.

> **Approach:** This is an **extractive summarization** technique. The system selects important sentences from the original text rather than generating new text.

## Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **NLTK** | Sentence tokenization and stop-word removal |
| **NumPy** | Numerical operations and score processing |
| **scikit-learn** | TF-IDF vectorization |

## Project Structure

```text
TEXT-SUMMARIZATION-USING-SML/
│
├── summarizer.py
├── requirements.txt
└── README.md
```

## Requirements

- Python **3.8 or later**
- `nltk`
- `numpy`
- `scikit-learn`

## Installation

### 1. Clone the repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd TEXT-SUMMARIZATION-USING-SML
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download required NLTK data

```bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"
```

## Run the Project

Execute:

```bash
python summarizer.py
```

The program will process the text defined in the script and print the generated summary.

## Example

### Input

```text
The quick brown fox jumps over the lazy dog.
The dog barks at the fox.
The fox runs away.
```

### Output

The program returns the sentence or sentences with the highest calculated importance scores.

The exact output depends on the TF-IDF scores of the input sentences.

## Summary Length

The number of selected sentences is controlled by:

```python
num_sentences = max(1, int(0.2 * len(sentences)))
```

The `0.2` value represents approximately **20% of the original sentences**.

For example:

```python
0.3
```

would select approximately 30% of the sentences.

## Limitations

- TF-IDF measures statistical importance, not true semantic meaning.
- The system does not understand context in the way modern language models do.
- Results can vary depending on the vocabulary and structure of the input.
- Very short texts may provide limited summarization benefits.

## Future Improvements

Possible extensions include:

- Incorporating sentence-position and length features
- Using cosine similarity or graph-based ranking
- Adding a graphical or web interface
- Supporting multiple languages
- Comparing TF-IDF with other statistical summarization techniques

