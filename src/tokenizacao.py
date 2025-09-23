import re
import requests
from bs4 import BeautifulSoup

def sentence_tokenizer(text):
    sentence_endings = re.compile(r'(?<=[.!?])\s+(?=[A-Z])')
    sentences = sentence_endings.split(text.strip())
    return [s.strip() for s in sentences if s]

def scrape_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    paragraphs = soup.find_all('p')
    text = ' '.join(p.get_text() for p in paragraphs)
    return text

if __name__ == "__main__":
    url = "https://www.uol.com.br/esporte/futebol/colunas/casagrande/2025/09/22/bola-de-ouro-super-merecida-para-ousmane-dembele.htm"
    raw_text = scrape_text_from_url(url)

    print("=== Texto Original (trecho) ===")
    print(raw_text[:500])

    sentences = sentence_tokenizer(raw_text)

    print("\n=== Sentenças Tokenizadas ===")
    for i, sent in enumerate(sentences[:100]): 
        print(f"{i+1}. {sent}")
