from modules.dna_tools import (
    base_count,
    gc_count,
    nucleotide_percentage,
    dna_complement,
    reverse_complement,
    rna_sequence
)


from modules.protein_tools import(protein_sequence,protein_validation)


from modules.sequence_length import(sequence_length)

from modules.dna_weights import(dna_molecular_weight)

from modules.orf_tools import(find_orf)
from modules.fasta_tools import export_fasta,read_fasta
from modules.result_tools import save_result
from modules.tm_tools import melting_temperature
from modules.csv_tools import save_csv
from modules.quality_tools import sequence_quality
from modules.summary_tools import analysis_summary

print("================================")
print("       Welcome to BioSeqX")
print("================================")

sequence = input("Enter a DNA sequence: ").strip().upper()
result=""

valid_bases = "ATGC"

if not sequence:
    print("Please enter a DNA sequence.")
    print("The sequence cannot be empty.")
elif not all(base in valid_bases for base in sequence):
    print("Invalid DNA sequence!")
    print("Only A, T, G and C are allowed.")
else:

    while True:
        print("\n========== BIOLOGY ANALYSIS MENU ==========")
        print("1. DNA Base Count")
        print("2. GC Content")
        print("3. Nucleotide Percentage")
        print("4. DNA Complement")
        print("5. Reverse Complement")
        print("6. DNA to RNA Transcription")
        print("7. RNA to Protein Translation")
        print("8. Sequence Length")
        print("9. Protein Sequence Analysis")
        print("10. DNA molecular weights")
        print("11. ORF analysis")
        print("12. Export DNA as FASTA")
        print("13. Import FASTA File")
        print("14.DNA melting Temperature")
        print("15.Export analysis as CSV")
        print("16.sequence quality summary")
        print("17.Analysis summary")
        print("18.Exit")
        print("============================================")
        choice = input("\nEnter your choice (1-18): ").strip()
        if choice == "1":
              result = base_count(sequence)
              save_result(result,sequence)

        elif choice == "2":
                result = gc_count(sequence)
                save_result(result,sequence)

        elif choice == "3":
                result = nucleotide_percentage(sequence)
                save_result(result,sequence)

        elif choice == "4":
                result=dna_complement(sequence)
                save_result(result,sequence)
        elif choice == "5":
                result=reverse_complement(sequence)
                save_result(result,sequence)
        elif choice == "6":
                result=  rna_sequence(sequence)
                save_result(result,sequence)

        elif choice == "7":
            rna = rna_sequence(sequence)
            result = protein_sequence(rna)
            save_result(result, sequence)

        elif choice == "8":
                result= sequence_length(sequence)
                save_result(result,sequence)
        elif choice == "9":
                result=protein_validation()
                save_result(result,"","Protein")

        elif choice == "10":
                result=dna_molecular_weight(sequence)
                save_result(result,sequence)
        elif choice == "11":
                result=find_orf(sequence)
                save_result(result,sequence)
        elif choice == "12":
                print("Option 12 detected!")
                export_fasta(sequence)
        elif choice == "13":
           fasta_sequence = read_fasta()

           if fasta_sequence:
            sequence = fasta_sequence
           print("\nFASTA sequence loaded successfully!")
           print("Current DNA sequence updated.")
           print("You can now use Options 1-12 to analyze this sequence.")

        elif choice == "14":
            result = melting_temperature(sequence)
            save_result(result, sequence)

        elif choice == "15":
             save_csv(result, sequence)
        elif choice == "16":
             result = sequence_quality(sequence)
             save_result(result, sequence)
        elif choice == "17":
            result = analysis_summary(sequence)
            print("\n========== ANALYSIS SUMMARY ==========")

            for key, value in result.items():
              print(f"{key}: {value}")
            
        elif choice == "18":
           print("\nThank you for using BioSeqX!")
           break

       

        else:
            print("\nInvalid choice. Please select 1-18.")