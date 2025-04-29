
def get_book_text(path_to_file):
    contents = None
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def count_words(text: str):
    return len(text.split())
