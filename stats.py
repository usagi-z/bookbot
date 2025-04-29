
def get_book_text(path_to_file):
    contents = None
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def count_words(text: str):
    return len(text.split())

def char_count(text: str):
    counts = dict()
    for c in text:
        c = c.lower()
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def sorted_char_counts(char_counts: dict):
    r = list()
    for char, num in char_counts.items():
        r.append({"char": char, "num": num})
    def sort_on(d):
        return d["num"]
    r.sort(reverse=True, key=sort_on)
    return r
