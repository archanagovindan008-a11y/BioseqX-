def dna_molecular_weight(sequence):

    base_weights = {
        "A": 313.2,
        "T": 304.2,
        "G": 329.2,
        "C": 289.2
    }

    molecular_weight = 0

    for base in sequence:
        molecular_weight += base_weights[base]

    result = "DNA molecular weight: " + str(round(molecular_weight, 2)) + " Da"

    print("\n" + result)

    return result