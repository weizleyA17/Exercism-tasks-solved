def classify(number):
      aliquot_sum = sum([i for i in range(1, number) if number % i == 0])
      if number < 1 :
            raise ValueError("Classification is only possible for positive integers.")
      elif aliquot_sum == number:
            return "perfect"
      elif aliquot_sum < number:
            return "deficient"
      else:            
            return "abundant"
      
