def add_prefix_un(word):
    return 'un' + word

def make_word_groups(vocab_words):
    word = vocab_words[0]
    remain = vocab_words[1:]
    result =[word] + [word + index for index in remain]
    return ' :: '.join(result)

def remove_suffix_ness(word):
    word.lower()
    root = word[:-4]
    if root.endswith("i"):
        return root[:-1] + "y"

    return root

def adjective_to_verb(sentence, index):
    text = sentence[:-1]
    adj= text.split()[index]
    return adj + "en"