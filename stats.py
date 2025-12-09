def count_words(text: str) -> int:
    return len(text.split())

def count_char(text: str) -> dict:
    text = text.lower()
    count_dict = {}

    for char in text:
        if not char.isalpha():
            continue

        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def dict_to_list(dic: dict) -> list:
    dict_list = []
    for key,value in dic.items():
        dict_list.append({"char": key, "num": value})

    return dict_list    


