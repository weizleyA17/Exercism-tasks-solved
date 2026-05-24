def is_valid(isbn):
    text = isbn.replace('-', '')
    result = 0
    
    if len(text) != 10:
        return False
        
    if not text[:9].isdigit():
        return False
        
    # Corrigido aqui: mudamos 'cahr' para 'char'
    values = [int(char) for char in text[:9]]
    
    last = text[-1]
    if last.isdigit():
        values.append(int(last))
    elif last == 'X':
        values.append(10)
    else:
        return False
      
    for index, value in enumerate(values):
        weight = 10 - index
        result += value * weight
        
    return result % 11 == 0