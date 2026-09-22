def find_orf(sequence):

    start = sequence.find("ATG")

    if start == -1:
        result = "No start codon (ATG) found."
        print("\n" + result)
        return result

    stop_codons = ["TAA", "TAG", "TGA"]

    for i in range(start + 3, len(sequence) - 2, 3):

        codon = sequence[i:i + 3]

        if codon in stop_codons:

            orf = sequence[start:i + 3]

            result = (
                "ORF found!\n"
                "Start position: " + str(start + 1) + "\n"
                "Stop position: " + str(i + 3) + "\n"
                "ORF sequence: " + orf + "\n"
                "ORF length: " + str(len(orf)) + " bases"
            )

            print("\n" + result)

            return result

    result = "No in-frame stop codon found."

    print("\n" + result)

    return result