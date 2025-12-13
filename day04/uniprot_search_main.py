from pathlib import Path
print("RUNNING FROM:", Path.cwd())

from uniprot_search_logic import search_uniprot
from uniprot_search_logic import download_many_fastas
from pathlib import Path

def main():
    print("=== UniProt search + FASTA download ===")

    keyword = input("Enter protein or gene name: ").strip()
    results = search_uniprot(keyword)

    if not results:
        print("No matches found.")
        return

    print("\nSearch results:\n")
    for i, r in enumerate(results, start=1):
        print(f"[{i}] {r['id']} — {r['gene']} — {r['name']} — {r['organism']}")

    choices = input("\nEnter numbers of entries to download (comma-separated): ")
    chosen_indexes = [int(x.strip()) - 1 for x in choices.split(",")]

    selected_ids = [results[i]["id"] for i in chosen_indexes]

    print("\nDownloading...\n")
    result = download_many_fastas(selected_ids, Path("data"))

    print("Finished!")
    print("Downloaded:", ", ".join(result["success"]))

if __name__ == "__main__":
    main()
