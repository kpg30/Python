def find_repeat_words(text):
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    repeat_words = [word for word, count in word_count.items() if count > 1]
    return repeat_words


input_txt = "next time there wont be a next time"
result = find_repeat_words(input_txt)
print(result)
