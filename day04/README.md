# 🧬 Day 04 – UniProt Protein Search & FASTA Downloader

## 📌 Overview

This program allows the user to search for proteins in the **UniProt** database using a **simple keyword** (gene name, protein name, function, etc.) without requiring prior knowledge of the UniProt accession ID.

After searching, the program displays a numbered list of matches, and the user can select which entries to download. The corresponding **FASTA sequences** are then retrieved and saved locally.

---

## 🧠 How It Works

### User Input:
- A keyword for searching UniProt (e.g. `MSN2`, `p53`, `hemoglobin`)
- The number of search results to display
- Which entries to download (by index number or `all`)
- Where to save the downloaded files

### Output:
- FASTA files for each selected protein

Example output files:

data/P15364.fasta

data/O59764.fasta

This project uses the official UniProt REST API:

Main site: https://www.uniprot.org/

Search endpoint: https://rest.uniprot.org/uniprotkb/search

FASTA download example:
https://rest.uniprot.org/uniprotkb/P15364.fasta

This API is fully public and does not require authentication.

## Interaction with AI

I used ChatGPT (GPT-5.1 Thinking on ChatGPT) to help:

- **Prompt:** “I need a simple but useful biological dataset-based program.”  
  **AI solution:** Recommended using UniProt FASTA downloading as a real-world useful tool.

- **Prompt:** “But what if the user doesn’t know the UniProt ID?”  
  **AI solution:** Redesigned UI flow to allow search by protein/gene keyword and selection by numbered index.


- **Prompt:** “I ran the file but got no output.”  
  **AI solution:** Added debugging prints and final `input()` pause to keep console open for visibility.

- **Prompt:** “Help me write the README file.”  
  **AI solution:** Generated this README in Markdown format and project documentation structure.
