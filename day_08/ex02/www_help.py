from urllib.parse import urlparse

def extract_domain(url):
    parsed = urlparse(url)
    return parsed.netloc