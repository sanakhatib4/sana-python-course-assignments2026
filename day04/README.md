# Day 04 – Downloading protein data from UniProt

## What the program does

This program downloads protein information from the [UniProt](https://www.uniprot.org/) database using its public REST API.

The user provides:

- a **keyword** (for example: `kinase`, `transcription factor`, `zinc finger`)
- an **organism name** (for example: `Homo sapiens`, `Saccharomyces cerevisiae`)
- a **maximum number of results**

The program sends a query to the UniProt API and saves the results as a TSV (tab-separated values) file in the `data/` folder:

- `data/uniprot_results.tsv`

The file contains the following columns for each protein:

- UniProt accession
- primary gene name
- protein name
- organism name
- sequence length

The program uses a command-line interface (CLI) as its UI.

## Code structure

- `uniprot_logic.py` – **business logic**  
  Contains the functions that:
  - build the UniProt query
  - contact the UniProt REST API
  - save the downloaded TSV data to a local file

- `main.py` – **user interface**  
  Handles the interaction with the user (input and print), and calls the
  functions in `uniprot_logic.py`.

- `data/` – output directory where the TSV file is saved.

## Secrets / configuration

The UniProt REST API does not require an email address or API key for this kind of simple query, so no secrets file is needed.  
If I used a service that required an email or API key, I would put it in a separate file (for example `config.py`) and add that filename to `.gitignore` so it would not be committed to git.

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
