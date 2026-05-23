def translate_word(word):
    
    word = word.lower()
    
    
    if word[0] in 'aeiou' or word.startswith('xr') or word.startswith('yt'):
        return word + 'ay'

    
    if 'qu' in word:
        qu_pos = word.index('qu')
        if all(char not in 'aeiou' for char in word[:qu_pos]):
            return word[qu_pos + 2:] + word[:qu_pos + 2] + 'ay'

    if 'y' in word and word[0] not in 'aeiou':
        y_pos = word.index('y')
        if y_pos > 0 and all(char not in 'aeiou' for char in word[:y_pos]):
            return word[y_pos:] + word[:y_pos] + 'ay'

    for i in range(len(word)):
        if word[i] in 'aeiou':
            return word[i:] + word[:i] + 'ay'
            
    return word + 'ay'


def translate(text):
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)