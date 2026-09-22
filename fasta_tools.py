def export_fasta(sequence):

    filename = "results/dna_sequence.fasta"

    file = open(filename, "w")

    file.write(">BioSeqX_DNA_Sequence\n")
    file.write(sequence + "\n")

    file.close()

    print("\nFASTA file exported successfully!")
    print("Saved as:", filename)

def read_fasta():

    filename = input("\nEnter FASTA file path: ").strip()

    try:
        file = open(filename, "r")

        lines = file.readlines()

        file.close()

        sequence = ""

        for line in lines:
            line = line.strip()

            if not line.startswith(">"):
                sequence += line

        sequence = sequence.upper()

        if not sequence:
           print("\nFASTA file does not contain a sequence!")
           return None

        result = "FASTA sequence loaded successfully!\n"
        result += "Sequence: " + sequence + "\n"
        result += "Sequence length: " + str(len(sequence))

        print("\n" + result)

        return sequence

    except FileNotFoundError:
        print("\nFASTA file not found!")
        return None