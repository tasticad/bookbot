def get_book_text(f_path):
    with open(f_path) as f:
        contents = f.read()
    return contents

def get_num_words(f_path):
    num_words = 0
    words = get_book_text(f_path).split()
    for word in words:
        num_words += 1
    return num_words

def get_num_chars(f_path):
    num_chars = {}
    text = get_book_text(f_path).lower()
    for char in text:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def dict_list(f_path):
    chars_dict = get_num_chars(f_path)
    chars_list = []
    for key, value in chars_dict.items():
        # Create a new dictionary for each key-value pair
        new_dict = {"char": key, "count": value}
        chars_list.append(new_dict)
    return chars_list

def sorted_dict_list(f_path):
    chars_list = dict_list(f_path)
    sorted_list = sorted(chars_list, key=lambda x: x["count"], reverse=True)
    return sorted_list
