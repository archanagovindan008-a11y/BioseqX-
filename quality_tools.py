def sequence_quality(sequence):

    length = len(sequence)

    gc = (sequence.count("G") + sequence.count("C")) / length * 100
    at = (sequence.count("A") + sequence.count("T")) / length * 100

    if gc > 60:
        classification = "GC-rich"
    elif gc < 40:
        classification = "AT-rich"
    else:
        classification = "Balanced GC/AT content"

    result = "DNA Sequence Quality Summary\n"
    result += "Sequence length: " + str(length) + " bases\n"
    result += "GC content: " + str(round(gc, 2)) + "%\n"
    result += "AT content: " + str(round(at, 2)) + "%\n"
    result += "Classification: " + classification

    print("\n" + result)

    return result