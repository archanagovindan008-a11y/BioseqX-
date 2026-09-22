from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.protein_tools import protein_sequence
from modules.orf_tools import find_orf
from modules.tm_tools import melting_temperature

from modules.dna_tools import (
    base_count,
    gc_count,
    nucleotide_percentage,
    dna_complement,
    reverse_complement,
    rna_sequence
)


app = FastAPI(title="BioSeqX")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# --------------------------------
# Home
# --------------------------------

@app.get("/")
def home():

    return {
        "message": "BioSeqX API is running successfully!"
    }


# --------------------------------
# Basic DNA Analysis
# --------------------------------

@app.get("/analyze/{sequence}")
def analyze_sequence(sequence: str):

    sequence = sequence.upper()

    if not sequence:

        return {
            "valid": False,
            "message": "DNA sequence cannot be empty."
        }

    valid_bases = "ATGC"

    for base in sequence:

        if base not in valid_bases:

            return {
                "valid": False,
                "message": "Invalid DNA sequence"
            }

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    gc_content = ((g + c) / length) * 100

    return {
        "valid": True,
        "sequence": sequence,
        "length": length,
        "A": a,
        "T": t,
        "G": g,
        "C": c,
        "GC Content": round(gc_content, 2)
    }


# --------------------------------
# Full DNA Analysis
# --------------------------------

@app.get("/dna-analysis/{sequence}")
def dna_analysis(sequence: str):

    sequence = sequence.upper()

    valid_bases = "ATGC"

    if not sequence:

        return {
            "valid": False,
            "message": "DNA sequence cannot be empty."
        }

    for base in sequence:

        if base not in valid_bases:

            return {
                "valid": False,
                "message":
                    "Invalid DNA sequence. Use only A, T, G and C."
            }

    return {

        "valid": True,

        "base_count": base_count(sequence),

        "gc_content": gc_count(sequence),

        "nucleotide_percentage":
            nucleotide_percentage(sequence),

        "complement":
            dna_complement(sequence),

        "reverse_complement":
            reverse_complement(sequence),

        "rna":
            rna_sequence(sequence)
    }


# --------------------------------
# Protein Analysis
# --------------------------------

@app.get("/protein-analysis/{sequence}")
def protein_analysis(sequence: str):

    sequence = sequence.upper()

    valid_amino_acids = "ACDEFGHIKLMNPQRSTVWY"

    if not sequence:

        return {
            "valid": False,
            "message": "Protein sequence cannot be empty."
        }

    for amino_acid in sequence:

        if amino_acid not in valid_amino_acids:

            return {
                "valid": False,
                "message":
                    "Invalid protein sequence! "
                    "Only standard amino acids are allowed."
            }

    protein_length = len(sequence)

    amino_acid_counts = {}

    for amino_acid in valid_amino_acids:

        count = sequence.count(amino_acid)

        if count > 0:

            amino_acid_counts[amino_acid] = count


    hydrophobic = "AVILMFWY"
    charged = "DEKR"
    polar = "STNQ"


    hydrophobic_count = sum(
        sequence.count(aa)
        for aa in hydrophobic
    )

    charged_count = sum(
        sequence.count(aa)
        for aa in charged
    )

    polar_count = sum(
        sequence.count(aa)
        for aa in polar
    )


    hydrophobic_percentage = (
        hydrophobic_count / protein_length
    ) * 100

    charged_percentage = (
        charged_count / protein_length
    ) * 100

    polar_percentage = (
        polar_count / protein_length
    ) * 100


    acidic_count = (
        sequence.count("D")
        + sequence.count("E")
    )


    basic_count = (
        sequence.count("K")
        + sequence.count("R")
        + sequence.count("H")
    )


    if acidic_count > basic_count:

        classification = "Acidic protein"

    elif basic_count > acidic_count:

        classification = "Basic protein"

    else:

        classification = "Neutral protein"


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

    for amino_acid in sequence:

        molecular_weight += (
            amino_acid_weights[amino_acid]
        )


    return {

        "valid": True,

        "sequence": sequence,

        "length": protein_length,

        "counts": amino_acid_counts,

        "hydrophobic_percentage":
            round(hydrophobic_percentage, 2),

        "charged_percentage":
            round(charged_percentage, 2),

        "polar_percentage":
            round(polar_percentage, 2),

        "classification":
            classification,

        "molecular_weight":
            round(molecular_weight, 2)
    }


# --------------------------------
# DNA → RNA → Protein Translation
# --------------------------------

@app.get("/translate/{sequence}")
def translate_sequence(sequence: str):

    sequence = sequence.upper()

    valid_bases = "ATGC"


    if not sequence:

        return {
            "valid": False,
            "message": "DNA sequence cannot be empty."
        }


    for base in sequence:

        if base not in valid_bases:

            return {
                "valid": False,
                "message":
                    "Invalid DNA sequence. "
                    "Use only A, T, G and C."
            }


    # DNA → RNA

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


    # RNA → Protein

    protein = protein_sequence(rna)


    return {

        "valid": True,

        "dna": sequence,

        "rna": rna,

        "protein": protein
    }


# --------------------------------
# ORF Analysis
# --------------------------------

@app.get("/orf-analysis/{sequence}")
def orf_analysis(sequence: str):

    sequence = sequence.upper()

    valid_bases = "ATGC"


    if not sequence:

        return {
            "valid": False,
            "message": "DNA sequence cannot be empty."
        }


    for base in sequence:

        if base not in valid_bases:

            return {
                "valid": False,
                "message":
                    "Invalid DNA sequence. "
                    "Use only A, T, G and C."
            }


    result = find_orf(sequence)


    return {

        "valid": True,

        "sequence": sequence,

        "orf_result": result
    }


# --------------------------------
# DNA Melting Temperature Analysis
# --------------------------------

@app.get("/tm-analysis/{sequence}")
def tm_analysis(sequence: str):

    sequence = sequence.upper()

    valid_bases = "ATGC"


    if not sequence:

        return {
            "valid": False,
            "message": "DNA sequence cannot be empty."
        }


    for base in sequence:

        if base not in valid_bases:

            return {
                "valid": False,
                "message":
                    "Invalid DNA sequence. "
                    "Use only A, T, G and C."
            }


    tm_result = melting_temperature(sequence)


    return {

        "valid": True,

        "sequence": sequence,

        "tm": tm_result
    }