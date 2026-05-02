import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.punctuation = string.punctuation

    def clean_text(self, text):
        """
        Cleans the input text by:
        1. Lowercasing
        2. Removing URLs
        3. Removing HTML tags
        4. Removing mentions (@user) and hashtags (#)
        5. Removing punctuation
        6. Removing numbers
        """
        if not isinstance(text, str):
            return ""
        
        # Lowercase
        text = text.lower()
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)
        # Remove user mentions and hashtags
        text = re.sub(r'\@\w+|\#','', text)
        # Remove punctuation
        text = text.translate(str.maketrans('', '', self.punctuation))
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        # Remove extra whitespace
        text = text.strip()
        
        return text

    def preprocess(self, text):
        """
        Full preprocessing pipeline:
        1. Clean text
        2. Tokenize and remove stopwords
        3. Lemmatization
        """
        cleaned = self.clean_text(text)
        tokens = cleaned.split()
        # Remove stopwords and lemmatize
        processed_tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word not in self.stop_words]
        
        return " ".join(processed_tokens)

if __name__ == "__main__":
    preprocessor = TextPreprocessor()
    sample = "@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer. You shoulda got David Carr of Third Day to do it. ;D"
    print(f"Original: {sample}")
    print(f"Cleaned: {preprocessor.clean_text(sample)}")
    print(f"Processed: {preprocessor.preprocess(sample)}")
