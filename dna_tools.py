def base_count(sequence):
    result = ""

    result += "A = " + str(sequence.count("A")) + "\n"
    result += "T = " + str(sequence.count("T")) + "\n"
    result += "G = " + str(sequence.count("G")) + "\n"
    result += "C = " + str(sequence.count("C")) + "\n"

    print(result)

    return result


def gc_count(sequence):
   
    gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100

    result = "GC percentage: " + str(round(gc, 2)) + "%"

    print("\n" + result)

    return result


def nucleotide_percentage(sequence):
    a = sequence.count("A") / len(sequence) * 100
    t = sequence.count("T") / len(sequence) * 100
    g = sequence.count("G") / len(sequence) * 100
    c = sequence.count("C") / len(sequence) * 100

    result = (
        "A percentage: " + str(round(a, 2)) + "%\n"
        "T percentage: " + str(round(t, 2)) + "%\n"
        "G percentage: " + str(round(g, 2)) + "%\n"
        "C percentage: " + str(round(c, 2)) + "%"
    )

    print("\n" + result)

    return result

def dna_complement(sequence):
    complement = ""

    for base in sequence:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"


    result='DNA Complement'+ complement
    print("\n" + result)

    return result


def reverse_complement(sequence):
    complement = ""

    for base in sequence:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    reverse = complement[::-1]

    result='Reverse Complement:'+ reverse
    print('\n'+result)
    return result


def rna_sequence(sequence):
    rna = ""

    for base in sequence:
        if base == "A":
            rna += "U"
        elif base == "T":
            rna += "A"
        elif base == "G":
            rna += "C"
        elif base == "C":
            rna += "G"

    result="RNA sequencing:"+rna
    print('\n'+result)
    return result