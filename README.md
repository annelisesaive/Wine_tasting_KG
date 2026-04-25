# Wine Tasting Knowledge Graph

Knowledge graph and price-quality analysis on ~130k wine reviews from Wine
Enthusiast. 
Powers [QualitySip](https://wine-search.streamlit.app/), a
Streamlit app that surfaces wines scoring higher than their price suggests.

## Writeups

- [Do expensive wines really taste better?](https://annelisesaive.substack.com/p/do-expensive-wines-really-taste-better) an analysis of the price-rating relationship across 130k reviews.
- [Introducing QualitySip](https://annelisesaive.substack.com/p/introducing-qualitysip-your-guide) the deployed app and how it works.

## Overview

The dataset comes from the Wine Enthusiast Kaggle release (~130k reviews) and
includes country, province, variety, winery, points, price, and free-text
tasting descriptions. After cleaning and deduplicating (removing missing
rows, merging entries for the same wine rated by multiple reviewers), the
notebooks extract tasting descriptors and relationships to construct a graph
linking wines, descriptive terms, and geographical origins.

## Data

The raw data is available from the Kaggle "Wine Reviews" dataset. To
reproduce, download `wine_tasting.csv` and place it in the `data_kaggle/`
folder. The repository does not include the raw dataset for licensing
reasons.

### Key variables

- `country`, `province`, `winery` — geographic and producer metadata
- `variety` — grape variety
- `description` — free-text tasting note
- `points` — Wine Enthusiast score
- `price` — price in USD
- Additional fields (vintage, taster name) may be present depending on the
  dataset version

## Project structure

- `code/` — Jupyter notebooks (`Exploratory_data_analyses.ipynb`,
  `KnowledgeGraph.ipynb`) and scripts for cleaning and graph construction
- `data_kaggle/` — placeholder for the raw Kaggle data
- `plots_figures/` — saved plots and visualisations

## Reproducing

1. Download the Kaggle dataset and place it in `data_kaggle/`.
2. Set up a Python environment (see `requirements.txt`).
3. Run `Exploratory_data_analyses.ipynb` to load, clean, and deduplicate the data.
4. Run `KnowledgeGraph.ipynb` to extract tasting descriptors, normalise terms, and build the knowledge graph.
5. Explore the resulting graph using network analysis tools, or export it for use elsewhere.

## Intended uses

- Explore relationships between grape varieties, tasting descriptors, and regions
- Identify flavour clusters and descriptor co-occurrence patterns
- Build recommendation systems or educational tools suggesting wines by flavour profile

## Contributing

Pull requests and issues welcome.

## Notes

The original dataset is subject to Kaggle's terms of use.
