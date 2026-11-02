
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   
DATA_DIR = ROOT / "Data"                        


def load_corpus():
    """Return a list of paper dicts; each gets an extra 'text' field (full text)."""
    with open(DATA_DIR / "corpus.json", encoding="utf-8") as f:
        papers = json.load(f)
    for p in papers:
        text_path = DATA_DIR / p["text_file"]
        p["text"] = text_path.read_text(encoding="utf-8") if text_path.exists() else ""
    return papers


if __name__ == "__main__":
    papers = load_corpus()
    missing = [p["arxiv_id"] for p in papers if not p["text"]]
    print(f"{len(papers)} papers loaded, {len(missing)} missing text files")
    print("example:", papers[0]["title"], "|", papers[0]["subtopic"], "|", len(papers[0]["text"]), "chars")
