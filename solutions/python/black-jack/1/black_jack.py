def value_of_card(card):
    match card.upper():
        case 'J' | 'Q' | 'K':
            return 10
        case 'A':
              return 1
        case _:
              return int(card)
      
def higher_card(card_one, card_two):
      
      if value_of_card(card_one) > value_of_card(card_two) :
            return card_one.upper()
      elif value_of_card(card_one) < value_of_card(card_two) :
            return card_two.upper()
      else :
            return card_one.upper(),card_two.upper()
      
def value_of_ace(card_one, card_two):
    current_value = value_of_card(card_one) + value_of_card(card_two)
    
    if card_one.upper() == 'A' or card_two.upper() == 'A':
        return 1
        
    if (current_value + 11) > 21:
        return 1
    else:
        return 11
      
def is_blackjack(card_one, card_two) :
      
      ten_cards = {'10', 'Q', 'J', 'K'}
      c1 = card_one.upper()
      c2 = card_two.upper()
      if c1 == 'A' and c2 in ten_cards:
            return True
      if c2 == 'A' and c1 in ten_cards:
            return True
      else:
            return False
      
def can_split_pairs(card_one, card_two):
      letters = {'J', 'Q', 'K'}
      if card_one in letters and card_two in letters:
        return True    
      if card_one.upper() == card_two.upper():
            return True
      else:
            return False      
def can_double_down(card_one, card_two):
      if value_of_card(card_one) + value_of_card(card_two) in (9, 10, 11):
            return True
      else:
            return False