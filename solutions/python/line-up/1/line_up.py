def line_up(name, number):
    if number in range(1,999):
            text = str(number)
            if not(text.endswith("11")) and text.endswith("1") :
                  return name + ", you are the " + text + "st customer we serve today. Thank you!"
            elif text.endswith("2") and not(text.endswith("12")):
                  return name + ", you are the " + text + "nd customer we serve today. Thank you!"
            elif text.endswith("3") and not(text.endswith("13")):
                  return name + ", you are the " + text + "rd customer we serve today. Thank you!"
            else:
                  return name + ", you are the " + text + "th customer we serve today. Thank you!"
