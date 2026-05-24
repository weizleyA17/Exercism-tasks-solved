def is_pangram(sentence):
      sentence = sentence.lower() 
      seen = []
      for char in sentence:
            if char in "abcdefghijklmnopqrstuvxwyz":
                  if char in seen:
                        pass
                  else:
                        seen.append(char)
      if len(seen) == 26:
            return True
      else:
            return False