import marshal
import re
import sys
import types

# Define a more comprehensive URL pattern including common domain names
URL_PATTERN = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
)

# List of common domain name extensions
COMMON_DOMAINS = [
    'com', 'org', 'net', 'int', 'edu', 'gov', 'mil', 'io', 'co', 'biz', 'info',
    'me', 'name', 'ly', 'in', 'us', 'uk', 'site', 'online', 'tech', 'app', 'dev',
    'store', 'xyz', 'ai', 'club', 'news', 'blog', 'design', 'space', 'agency',
    'solutions', 'world'
]

# Pattern to match common domain names (e.g., example.com)
DOMAIN_PATTERN = re.compile(
    rf'(?:[a-zA-Z0-9-]+\.)+(?:{"|".join(COMMON_DOMAINS)})'
)

def extract_urls_and_domains(text):
    """Extract URLs and domain names from the given text."""
    urls = URL_PATTERN.findall(text)
    domains = DOMAIN_PATTERN.findall(text)
    return set(urls + domains)

def extract_code_objects(co):
    """Recursively extract all code objects from a given code object."""
    code_objects = [co]
    for const in co.co_consts:
        if isinstance(const, types.CodeType):
            code_objects.extend(extract_code_objects(const))
    return code_objects

def extract_urls_from_code_object(co):
    """Extract URLs and domain names from the given code object."""
    urls = set()
    for const in co.co_consts:
        if isinstance(const, str):
            urls.update(extract_urls_and_domains(const))
    return urls

def extract_urls_from_pyc(filename):
    """Extract URLs and domain names from the given .pyc file."""
    with open(filename, 'rb') as f:
        try:
            co = marshal.load(f)
        except Exception as e:
            print(f"Error loading marshal data: {e}")
            return set()
        
        code_objects = extract_code_objects(co)
        urls = set()
        for code_object in code_objects:
            urls.update(extract_urls_from_code_object(code_object))
        return urls

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: xurl.py <file.pyc>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        urls = extract_urls_from_pyc(filename)
        if urls:
            print("Found URLs and Domain Names:")
            for url in urls:
                print(url)
        else:
            print("No URLs or Domain Names found.")
    except Exception as e:
        print(f"Error: {e}")
