**arXiv Hybrid Literature Search (cs.CL)**



Information Retrieval course project, Princess Sumaya University for Technology.

Team: Dareen Khan, Lena Alrashid, Dana AbuSaa



**Overview**

A literature-search engine over arXiv papers in NLP cs.CL



&#x20;Phase 1 builds the corpus and a hybrid retrieval system

(BM25 + dense retrieval, fusion).





**Corpus**

**Source:** arXiv category `NLP cs.CL`

**Size:** 400 papers, 100 per sub-topic:

&#x20; machine translation, question answering, text summarization, dialogue systems



**Date range:** 2025-01-01 to 2026-10-31

**Length tiers:** short (<6 pages): 26, medium (6-9 pages): 75, long (>9 pages): 299

&#x20; (6-page as medium)

**Fields per paper:** title, arXiv ID/link, abstract, sub-topic, page count,

&#x20; length tier, full text

**Reproducibility:** the exact queries are in `Data/collection\_log.json`

&#x20; and the code is in `collect\_corpus.ipynb`



**Repository structure**



Data/

&#x20; corpus.json            paper metadata

&#x20; collection\_log.json    exact arXiv queries and date range

&#x20; texts/                 full text of each paper

src/                     retrieval engine code

ai-logs/phase1/          AI usage transcripts and index

collect\_corpus.ipynb     corpus collection notebook

requirements.txt



**How to run**



pip install -r requirements.txt

\- Rebuild the corpus: open and run `collect\_corpus.ipynb`

\- Run the search engine: \[command, to be added when the engine is ready]



**Features**

\- \[ ] BM25 retrieval

\- \[ ] Dense (embedding) retrieval

\- \[ ] Rank fusion

\- \[ ] Spelling correction, abbreviation expansion, phrase matching

\- \[ ] GUI
