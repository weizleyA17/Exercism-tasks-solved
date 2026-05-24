import string
def is_pangram(sentence):
      sentence_letters = set(sentence.lower())
      alphabet = set(string.ascii_lowercase)
      return alphabet.issubset(sentence_letters)