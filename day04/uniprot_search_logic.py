import requests

from pathlib import Path
import requests

# Base URLs for UniProt REST API
SEARCH_URL = "https://rest.uniprot.org/uniprotkb/search"
FASTA_BASE_URL = "https://rest.uniprot.org/uniprotkb"


def search_uniprot(keyword: str, limit: int = 10) -> list[dict]:
    """
    Search UniProt by a keyword (protein name, gene name, etc.)
    and return a list of results.

    Each result is a dict with:
        {
            "id":        UniProt accession (e.g. "P15364")
            "gene":      Primary gene name (if available)
            "name":      Protein name (recommended full name, if available)
            "organism":  Organism scientific name
        }

    :param keyword: Search keyword, e.g. "MSN2", "hemoglobin"
    :param limit:   Max number of results to return
    """
    keyword = keyword.strip()
    if not keyword:
        return []

    params = {
        "query": keyword,
        "format": "json",
        "size": limit,
        "fields": "accession,gene_primary,protein_name,organism_name",
    }

    response = requests.get(SEARCH_URL, params=params, timeout=20)
    response.raise_for_status()  # raise error if HTTP status is not OK (200)

    data = response.json()
    entries = data.get("results", [])

    results: list[dict] = []

    for entry in entries:
        # UniProt accession
        acc = entry.get("primaryAccession", "")

        # Gene name (if exists)
        gene_name = ""
        genes_list = entry.get("genes", [])
        if genes_list:
            gene_name = (
                genes_list[0]
                .get("geneName", {})
                .get("value", "")
            )

        # Protein recommended full name (if exists)
        protein_name = ""
        prot_desc = entry.get("proteinDescription", {})
        rec_name = prot_desc.get("recommendedName", {})
        full_name = rec_name.get("fullName", {})
        if isinstance(full_name, dict):
            protein_name = full_name.get("value", "")

        # Organism name
        organism = entry.get("organism", {}).get("scientificName", "")

        results.append(
            {
                "id": acc,
                "gene": gene_name,
                "name": protein_name,
                "organism": organism,
            }
        )

    return results


def download_fasta_for_id(uniprot_id: str) -> str:
    """
    Download the FASTA sequence for a single UniProt ID and
    return it as a string.

    Raises an exception if the download fails.
    """
    uniprot_id = uniprot_id.strip()
    if not uniprot_id:
        raise ValueError("Empty UniProt ID")

    url = f"{FASTA_BASE_URL}/{uniprot_id}.fasta"
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.text


def save_fasta_to_file(fasta_text: str, output_path: Path) -> None:
    """
    Save the given FASTA text to output_path.
    Creates parent folder(s) if needed.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(fasta_text, encoding="utf-8")


def download_many_fastas(uniprot_ids: list[str], out_dir: Path) -> dict:
    """
    Download FASTA files for multiple UniProt IDs and save
    each as <ID>.fasta in the given directory.

    Returns a dictionary:
        {
            "success": [list of IDs that were downloaded successfully],
            "failed":  [list of IDs that failed],
        }
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    success: list[str] = []
    failed: list[str] = []

    for uid in uniprot_ids:
        uid = uid.strip()
        if not uid:
            continue

        try:
            fasta = download_fasta_for_id(uid)
            filepath = out_dir / f"{uid}.fasta"
            save_fasta_to_file(fasta, filepath)
            success.append(uid)
        except Exception:
            failed.append(uid)

    return {"success": success, "failed": failed}