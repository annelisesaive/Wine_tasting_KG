# Wine Tasting Knowledge Graph

## Overview
Wine_tasting_KG is a data‑science project that cleans, structures and explores a large corpus of wine reviews to build a knowledge graph. The dataset comes from Wine Enthusiast (~130 k reviews published on Kaggle) and includes variables such as country, province, variety, winery, points, price and tasting descriptions:contentReference[oaicite:1]{index=1}. After cleaning and deduplicating the dataset (e.g., removing rows with missing data and combining entries for the same wine rated by different users:contentReference[oaicite:2]{index=2}), the notebooks extract tasting notes and relationships to construct a graph linking wines, descriptive terms and geographical origins.

## Data
The raw data is available from the Kaggle “Wine Tasting” dataset. To reproduce this project you should download `wine_tasting.csv` from Kaggle and place it in the `data_kaggle` folder. The repository does not include the raw dataset for licensing reasons. Example notebooks demonstrate the cleaning steps and graph construction.

### Key variables
- `country`, `province`, `winery` – geographic and producer metadata.
- `variety` – grape variety.
- `description` – free‑text tasting note.
- `points` – Wine Enthusiast score.
- `price` – price.
- Additional fields (e.g., vintage, taster name) may be present depending on the dataset.

## Project structure
- **`code/`** – Jupyter notebooks (`Exploratory_data_analyses.ipynb`, `KnowledgeGraph.ipynb`) and scripts for cleaning and graph construction.
- **`data_kaggle/`** – placeholder for the raw Kaggle data.
- **`plots_figures/`** – saved plots and visualisations.
- **Repository config** – `.devcontainer/`, `.gitattributes`, `.gitignore`, etc.

## Steps to reproduce
1. Download the Kaggle dataset and place it in `data_kaggle/`.
2. Set up a Python environment (see `requirements.txt` or the environment specification in the notebooks).
3. Run the cleaning notebook (e.g., `Exploratory_data_analyses.ipynb`) to load the data, drop missing values and merge duplicate wines:contentReference[oaicite:3]{index=3}.
4. Run `KnowledgeGraph.ipynb` to extract tasting descriptors, normalise terms and build the knowledge graph.
5. Explore the resulting graph using network analysis or export it for use in other tools.

## Intended use
The cleaned dataset and knowledge graph can be used to:
- Explore relationships between grape varieties, tasting descriptors and geographical regions.
- Identify flavour clusters or descriptor co‑occurrence patterns.
- Build recommendation systems or educational tools that suggest wines based on desired flavour profiles.

## Contributing
Pull requests and issues are welcome. Feel free to suggest improvements or report problems.

## Note
Note that the original dataset is subject to Kaggle’s terms of use.
