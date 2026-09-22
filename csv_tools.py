import csv
from datetime import datetime


def save_csv(result, sequence="", sequence_type="DNA"):

    filename = "results/analysis_result.csv"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["BioSeqX"])
        writer.writerow(["Date & Time", current_time])
        writer.writerow(["Sequence Type", sequence_type])
        writer.writerow(["Sequence", sequence])

        if isinstance(result, dict):
            writer.writerow(["Analysis Summary"])

            for key, value in result.items():
                writer.writerow([key, value])

        else:
            writer.writerow(["Analysis Result", result])

        writer.writerow([])

    print("\nCSV result saved successfully!")