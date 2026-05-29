def to_rna(dna_strand: str):
    result = ""
    for char in dna_strand:
        if char == "G":
            result += "C"
        elif char == "C":
            result += "G"
        elif char == "T":
            result += "A"
        elif char == "A":
            result += 'U'
    return result