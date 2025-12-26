def get_num_words(text):
    num_words = len(text.lower().split())
    return num_words

def get_num_characters(text):
    counts = dict()
    for c in text.lower():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def sorted_list_of_dict(num_chars_dict):
    characters = []
    for char, count in num_chars_dict.items():
        characters.append({
            "char": char,
            "num": count
            })
    characters.sort(reverse=True, key=lambda d: d["num"])
    return characters
