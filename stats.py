def get_num_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def get_character_count(file_contents):
    result = {}
    contents = file_contents.lower()
    for char in contents:
        if(char in result):
            result[char] += 1
        else:
            result[char] = 1    
    return result

def sort_on(items):
    return items["num"]

def sort_list(word_list):
    result = []
    temp = {}
    for x, y in word_list.items():
        if x.isalpha():
            temp = {
                'char': x,
                'num': y
            }
            result.append(temp)
    result.sort(reverse=True, key=sort_on)
    return result
