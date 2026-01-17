import re


def parse_sentences(sentence):
    pattern = r"[A-Za-z0-9]+[!?]?|\+"  # words/numbers optionally ending with ! or ?, or standalone +
    result = re.findall(pattern, sentence)  # find all tokens
    return result


# should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("Hello! How are you doing?"))
# should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("what a beautiful day it is"))
# should return ['2', '+', '2', 'is', 'definitely', '4!']
print(parse_sentences("2 + 2 is definitely 4!"))
