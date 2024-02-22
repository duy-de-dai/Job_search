import unicodedata
import re
from collections import Counter
from underthesea import word_tokenize
import string


def remove_accents(text):
    # https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
    no_accents_text = ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
    return no_accents_text.replace('đ', 'd')


def clean_text(text):
    pattern = re.compile(r'[^áàảãạâấầẩẫậăẵẳắằặđéèẻẽẹêếềểễệíìịỉĩóòõỏọôốồổộỗơớờởỡợúùũủụưứừửữựýỳỷỹỵ\sa-z_]')
    cleaned_text = re.sub(pattern, ' ', text)
    
    # Loại bỏ dấu câu
    cleaned_text = re.sub(r'[{}]'.format(re.escape(string.punctuation)), '', cleaned_text)

    # Loại bỏ các dấu cách dư thừa, chỉ giữ lại một dấu cách
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text.lower()

def remove_stopwords(text, stopwords_set):
    tokens = [token for token in text.split() if token not in stopwords_set]
    return tokens


def preprocess_text(text, stopwords_set):
    processed_text = clean_text(text.lower())
    processed_text = word_tokenize(processed_text, format='text')
    processed_text = processed_text.lower()
    
    tokens = remove_stopwords(processed_text, stopwords_set)
    # tokens = [token for token in tokens]
    return tokens