def analysis_summary(sequence):
    length = len(sequence)

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / length) * 100

    summary = {
        "Sequence": sequence,
        "Length": length,
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "GC Content (%)": round(gc_content, 2)
    }

    return summary