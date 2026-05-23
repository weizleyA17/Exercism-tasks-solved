def get_rounds(number):
      result = [number]
      result.append(number + 1)
      result.append(number + 2)
      return result
def concatenate_rounds(rounds_1, rounds_2):
      return rounds_1 + rounds_2
def list_contains_round(rounds, number):
      return number in rounds
def card_average(hand):
      return sum(hand) / len(hand)

def approx_average_is_average(hand):
      first_last_avg = (hand[0] + hand[-1]) / 2
      middle_value = hand[len(hand) // 2]
      actual_avg = card_average(hand)
      return actual_avg == first_last_avg or actual_avg == middle_value
def average_even_is_average_odd(hand):
      even = []
      odd = []
      for index, item in enumerate(hand):
            if index % 2 == 0:
                  even.append(item)
            else:
                  odd.append(item) 
      return card_average(even) == card_average(odd)

def maybe_double_last(hand):
      last = hand[-1]
      if last == 11:
             hand[-1]= last*2
             return hand
      else :
            return hand           