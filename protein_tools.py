def protein_sequence(sequence):

    codon_table = {
        "UUU": "F", "UUC": "F",
        "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y",
        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
        "UGU": "C", "UGC": "C",
        "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I",
        "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S",
        "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    start = sequence.find("AUG")

    if start == -1:
        result = "No start codon (AUG) found."
        print("\n" + result)
        return result

    protein = ""

    for i in range(start, len(sequence) - 2, 3):

        codon = sequence[i:i + 3]

        amino_acid = codon_table.get(codon, "")

        if amino_acid == "STOP":
            break

        protein += amino_acid

    result = "Protein sequence: " + protein

    print("\n" + result)

    return result
    
def protein_validation():

    protein = input("\nEnter protein sequence: ").strip().upper()

    valid_amino_acids = "ACDEFGHIKLMNPQRSTVWY"

    if not protein:
        result = "Protein sequence cannot be empty."
        print("\n" + result)
        return result

    if not all(amino_acid in valid_amino_acids for amino_acid in protein):
        result = "Invalid protein sequence! Only standard amino acids are allowed."
        print("\n" + result)
        return result

    result = "Protein sequence is valid!\n"

    result += "Protein length: " + str(len(protein)) + "\n"

    result += "\nAmino acid counts:\n"

    for amino_acid in valid_amino_acids:
        count = protein.count(amino_acid)

        if count > 0:
            result += amino_acid + " = " + str(count) + "\n"

    result += "\nAmino acid percentages:\n"

    for amino_acid in valid_amino_acids:
        count = protein.count(amino_acid)

        if count > 0:
            percentage = (count / len(protein)) * 100

            result += (
                amino_acid + " = "
                + str(round(percentage, 2))
                + "%\n"
            )
    hydrophobic = "AVILMFWY"
    charged = "DEKR"
    polar = "STNQ"

    hydrophobic_count = sum(protein.count(aa) for aa in hydrophobic)
    charged_count = sum(protein.count(aa) for aa in charged)
    polar_count = sum(protein.count(aa) for aa in polar)

    hydrophobic_percentage = (hydrophobic_count / len(protein)) * 100
    charged_percentage = (charged_count / len(protein)) * 100
    polar_percentage = (polar_count / len(protein)) * 100

    result += "\nProtein composition:\n"
    result += "Hydrophobic amino acids: " + str(round(hydrophobic_percentage, 2)) + "%\n"
    result += "Charged amino acids: " + str(round(charged_percentage, 2)) + "%\n"
    result += "Polar amino acids: " + str(round(polar_percentage, 2)) + "%\n"

    acidic_count = protein.count("D") + protein.count("E")
    basic_count = (
        protein.count("K")
        + protein.count("R")
        + protein.count("H")
    )

    result += "\nProtein charge classification:\n"

    if acidic_count > basic_count:
        result += "Classification: Acidic protein\n"
    elif basic_count > acidic_count:
        result += "Classification: Basic protein\n"
    else:
        result += "Classification: Neutral protein\n"

        
    amino_acid_weights = {
        "A": 89.09,
        "C": 121.15,
        "D": 133.10,
        "E": 147.13,
        "F": 165.19,
        "G": 75.07,
        "H": 155.16,
        "I": 131.17,
        "K": 146.19,
        "L": 131.17,
        "M": 149.21,
        "N": 132.12,
        "P": 115.13,
        "Q": 146.15,
        "R": 174.20,
        "S": 105.09,
        "T": 119.12,
        "V": 117.15,
        "W": 204.23,
        "Y": 181.19
    }

    molecular_weight = 0

    for amino_acid in protein:
        molecular_weight += amino_acid_weights[amino_acid]

    result += "\nProtein molecular weight: " + str(
        round(molecular_weight, 2)
    ) + " Da"

    print("\n" + result)

    return result