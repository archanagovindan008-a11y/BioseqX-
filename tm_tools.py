def melting_temperature(sequence):

    if not sequence:
        result = "DNA sequence cannot be empty."
        print("\n" + result)
        return result

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    tm = (2 * (a + t)) + (4 * (g + c))

    result = "DNA melting temperature (Tm): " + str(tm) + " °C"

    print("\n" + result)

    return result