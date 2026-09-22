from datetime import datetime


def save_result(result, sequence="", sequence_type="DNA"):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = open("results/analysis_result.txt", "a")

    file.write("\n")
    file.write("================================\n")
    file.write("        BioSeqX\n")
    file.write("        Analysis Report\n")
    file.write("================================\n")
    file.write("Date & Time: " + current_time + "\n")

    if sequence:
        file.write(sequence_type + " Sequence: " + sequence + "\n\n")

    file.write(result)
    file.write("\n")
    file.write("================================\n")

    file.close()

    print("\nResult saved successfully!")