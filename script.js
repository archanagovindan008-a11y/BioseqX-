// -----------------------------------------
// Get HTML Elements
// -----------------------------------------

const analyzeButton = document.getElementById("analyzeButton");
const clearButton = document.getElementById("clearButton");
const dnaAnalysisButton = document.getElementById("dnaAnalysisButton");
const proteinAnalysisButton = document.getElementById("proteinAnalysisButton");
const translateButton = document.getElementById("translateButton");
const orfAnalysisButton = document.getElementById("orfAnalysisButton");

const dnaSequence = document.getElementById("dnaSequence");
const results = document.getElementById("results");


// -----------------------------------------
// FastAPI Server
// -----------------------------------------

const API_URL = "http://127.0.0.1:8001";


// -----------------------------------------
// Basic DNA Analysis
// -----------------------------------------

analyzeButton.addEventListener("click", async function () {

    const sequence = dnaSequence.value.trim().toUpperCase();

    if (sequence === "") {

        results.innerHTML = `
            <h2>DNA Analysis</h2>
            <p>Please enter a DNA sequence.</p>
        `;

        return;
    }

    results.innerHTML = `
        <h2>DNA Analysis</h2>
        <p>Analyzing sequence...</p>
    `;

    try {

        const response = await fetch(
            `${API_URL}/analyze/${sequence}`
        );

        const data = await response.json();

        if (!data.valid) {

            results.innerHTML = `
                <h2>DNA Analysis</h2>
                <p>${data.message}</p>
            `;

            return;
        }

        results.innerHTML = `

            <h2>DNA Analysis Results</h2>

            <div class="result-cards">

                <div class="result-card">
                    <h3>Sequence</h3>
                    <p>${data.sequence}</p>
                </div>

                <div class="result-card">
                    <h3>Length</h3>
                    <p>${data.length}</p>
                </div>

                <div class="result-card">
                    <h3>A</h3>
                    <p>${data.A}</p>
                </div>

                <div class="result-card">
                    <h3>T</h3>
                    <p>${data.T}</p>
                </div>

                <div class="result-card">
                    <h3>G</h3>
                    <p>${data.G}</p>
                </div>

                <div class="result-card">
                    <h3>C</h3>
                    <p>${data.C}</p>
                </div>

                <div class="result-card">
                    <h3>GC Content</h3>
                    <p>${data["GC Content"]}%</p>
                </div>

            </div>

        `;

    } catch (error) {

        results.innerHTML = `
            <h2>Connection Error</h2>
            <p>Unable to connect to BioSeqX server.</p>
            <p>Make sure FastAPI is running on port 8001.</p>
        `;
    }

});


// -----------------------------------------
// Full DNA Analysis
// -----------------------------------------

dnaAnalysisButton.addEventListener("click", async function () {

    const sequence = dnaSequence.value.trim().toUpperCase();

    if (sequence === "") {

        results.innerHTML = `
            <h2>DNA Analysis</h2>
            <p>Please enter a DNA sequence.</p>
        `;

        return;
    }

    results.innerHTML = `
        <h2>DNA Analysis</h2>
        <p>Analyzing DNA sequence...</p>
    `;

    try {

        const response = await fetch(
            `${API_URL}/dna-analysis/${sequence}`
        );

        const data = await response.json();

        if (!data.valid) {

            results.innerHTML = `
                <h2>DNA Analysis</h2>
                <p>${data.message}</p>
            `;

            return;
        }

        results.innerHTML = `

            <h2>DNA Analysis Results</h2>

            <div class="result-cards">

                <div class="result-card">
                    <h3>Base Count</h3>
                    <p>${data.base_count.replace(/\n/g, "<br>")}</p>
                </div>

                <div class="result-card">
                    <h3>GC Content</h3>
                    <p>${data.gc_content}</p>
                </div>

                <div class="result-card">
                    <h3>Nucleotide Percentage</h3>
                    <p>
                        ${data.nucleotide_percentage.replace(/\n/g, "<br>")}
                    </p>
                </div>

                <div class="result-card">
                    <h3>DNA Complement</h3>
                    <p>${data.complement}</p>
                </div>

                <div class="result-card">
                    <h3>Reverse Complement</h3>
                    <p>${data.reverse_complement}</p>
                </div>

                <div class="result-card">
                    <h3>RNA Sequence</h3>
                    <p>${data.rna}</p>
                </div>

            </div>

        `;

    } catch (error) {

        results.innerHTML = `
            <h2>Connection Error</h2>
            <p>Unable to connect to BioSeqX server.</p>
            <p>Make sure FastAPI is running on port 8001.</p>
        `;
    }

});


// -----------------------------------------
// Protein Analysis
// -----------------------------------------

proteinAnalysisButton.addEventListener("click", async function () {

    const sequence = dnaSequence.value.trim().toUpperCase();

    if (sequence === "") {

        results.innerHTML = `
            <h2>Protein Analysis</h2>
            <p>Please enter a protein sequence.</p>
        `;

        return;
    }

    results.innerHTML = `
        <h2>Protein Analysis</h2>
        <p>Analyzing protein sequence...</p>
    `;

    try {

        const response = await fetch(
            `${API_URL}/protein-analysis/${sequence}`
        );

        const data = await response.json();

        if (!data.valid) {

            results.innerHTML = `
                <h2>Protein Analysis</h2>
                <p>${data.message}</p>
            `;

            return;
        }

        let counts = "";

        for (const aminoAcid in data.counts) {

            counts += `
                ${aminoAcid} = ${data.counts[aminoAcid]}<br>
            `;
        }

        results.innerHTML = `

            <h2>Protein Analysis Results</h2>

            <div class="result-cards">

                <div class="result-card">
                    <h3>Protein Sequence</h3>
                    <p>${data.sequence}</p>
                </div>

                <div class="result-card">
                    <h3>Length</h3>
                    <p>${data.length}</p>
                </div>

                <div class="result-card">
                    <h3>Amino Acid Counts</h3>
                    <p>${counts}</p>
                </div>

                <div class="result-card">
                    <h3>Hydrophobic</h3>
                    <p>${data.hydrophobic_percentage}%</p>
                </div>

                <div class="result-card">
                    <h3>Charged</h3>
                    <p>${data.charged_percentage}%</p>
                </div>

                <div class="result-card">
                    <h3>Polar</h3>
                    <p>${data.polar_percentage}%</p>
                </div>

                <div class="result-card">
                    <h3>Classification</h3>
                    <p>${data.classification}</p>
                </div>

                <div class="result-card">
                    <h3>Molecular Weight</h3>
                    <p>${data.molecular_weight} Da</p>
                </div>

            </div>

        `;

    } catch (error) {

        results.innerHTML = `
            <h2>Connection Error</h2>
            <p>Unable to connect to BioSeqX server.</p>
            <p>Make sure FastAPI is running on port 8001.</p>
        `;
    }

});


// -----------------------------------------
// DNA → RNA → Protein Translation
// -----------------------------------------

translateButton.addEventListener("click", async function () {

    const sequence = dnaSequence.value.trim().toUpperCase();

    if (sequence === "") {

        results.innerHTML = `
            <h2>DNA → Protein Translation</h2>
            <p>Please enter a DNA sequence.</p>
        `;

        return;
    }

    results.innerHTML = `
        <h2>DNA → Protein Translation</h2>
        <p>Translating sequence...</p>
    `;

    try {

        const response = await fetch(
            `${API_URL}/translate/${sequence}`
        );

        const data = await response.json();

        if (!data.valid) {

            results.innerHTML = `
                <h2>DNA → Protein Translation</h2>
                <p>${data.message}</p>
            `;

            return;
        }

        let translationStatus;

        if (data.protein.includes("No start codon")) {

            translationStatus = "No AUG start codon found";

        } else {

            translationStatus = "Protein translation completed";

        }

        results.innerHTML = `

            <h2>Translation Results</h2>

            <div class="result-cards">

                <div class="result-card">
                    <h3>DNA Sequence</h3>
                    <p>${data.dna}</p>
                </div>

                <div class="result-card">
                    <h3>RNA Sequence</h3>
                    <p>${data.rna}</p>
                </div>

                <div class="result-card">
                    <h3>Protein Sequence</h3>
                    <p>${data.protein}</p>
                </div>

                <div class="result-card">
                    <h3>Translation Status</h3>
                    <p>${translationStatus}</p>
                </div>

            </div>

        `;

    } catch (error) {

        results.innerHTML = `
            <h2>Connection Error</h2>
            <p>Unable to connect to BioSeqX server.</p>
            <p>Make sure FastAPI is running on port 8001.</p>
        `;
    }

});


// -----------------------------------------
// ORF Analysis
// -----------------------------------------

orfAnalysisButton.addEventListener("click", async function () {

    const sequence = dnaSequence.value.trim().toUpperCase();

    if (sequence === "") {

        results.innerHTML = `
            <h2>ORF Analysis</h2>
            <p>Please enter a DNA sequence.</p>
        `;

        return;
    }

    results.innerHTML = `
        <h2>ORF Analysis</h2>
        <p>Finding Open Reading Frames...</p>
    `;

    try {

        const response = await fetch(
            `${API_URL}/orf-analysis/${sequence}`
        );

        const data = await response.json();

        if (!data.valid) {

            results.innerHTML = `
                <h2>ORF Analysis</h2>
                <p>${data.message}</p>
            `;

            return;
        }

        results.innerHTML = `

            <h2>ORF Analysis Results</h2>

            <div class="result-cards">

                <div class="result-card">
                    <h3>DNA Sequence</h3>
                    <p>${data.sequence}</p>
                </div>

                <div class="result-card">
                    <h3>ORF Result</h3>
                    <p>${data.orf_result}</p>
                </div>

            </div>

        `;

    } catch (error) {

        results.innerHTML = `
            <h2>Connection Error</h2>
            <p>Unable to connect to BioSeqX server.</p>
            <p>Make sure FastAPI is running on port 8001.</p>
        `;
    }

});

// -----------------------------------------
// DNA Melting Temperature Analysis
// -----------------------------------------

tmAnalysisButton.addEventListener("click", async function () {

    const sequence = dnaSequence.value.trim().toUpperCase();

    if (sequence === "") {

        results.innerHTML = `
            <h2>Tm Analysis</h2>
            <p>Please enter a DNA sequence.</p>
        `;

        return;
    }

    results.innerHTML = `
        <h2>Tm Analysis</h2>
        <p>Calculating melting temperature...</p>
    `;

    try {

        const response = await fetch(
            `${API_URL}/tm-analysis/${sequence}`
        );

        const data = await response.json();

        if (!data.valid) {

            results.innerHTML = `
                <h2>Tm Analysis</h2>
                <p>${data.message}</p>
            `;

            return;
        }

        results.innerHTML = `

            <h2>DNA Melting Temperature</h2>

            <div class="result-cards">

                <div class="result-card">
                    <h3>DNA Sequence</h3>
                    <p>${data.sequence}</p>
                </div>

                <div class="result-card">
                    <h3>Melting Temperature</h3>
                    <p>${data.tm}</p>
                </div>

            </div>

        `;

    } catch (error) {

        results.innerHTML = `
            <h2>Connection Error</h2>
            <p>Unable to connect to BioSeqX server.</p>
            <p>Make sure FastAPI is running on port 8001.</p>
        `;
    }

});

// -----------------------------------------
// Clear / Reset
// -----------------------------------------

clearButton.addEventListener("click", function () {

    dnaSequence.value = "";

    results.innerHTML = `
        <h2>BioSeqX</h2>
        <p>Enter a DNA or protein sequence to begin analysis.</p>
    `;

});