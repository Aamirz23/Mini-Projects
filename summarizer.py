import nltk
from nltk.tokenize import sent_tokenize , word_tokenize
from nltk.corpus import stopwords
from string import punctuation

#ddownload the nltk data

nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")

def summarize(text, num_sentences = 3):
    stop_words = set(stopwords.words("english") + list(punctuation))
    words = word_tokenize(text.lower())

#frequency of each word

    freq = {}
    for word in words:
        if word not in stop_words:
            freq[word] = freq.get(word, 0) + 1


    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get , reverse=True)[:num_sentences]
    summary = ' '.join(summary_sentences)
    return summary

if __name__ == "__main__":
    input_text = input("Paste your text here:\n")
    summary = summarize(input_text)
    print("\n---summary---\n")
    print(summary)
        

