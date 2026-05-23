def score(x,y):
      rad = (x**2 + y**2)**0.5
      if rad <= 1:
            return 10
      elif rad <= 5:
            return 5
      elif rad <= 10:
            return 1
      else:
            return 0