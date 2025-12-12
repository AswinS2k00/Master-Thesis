2SSP – Domain-Specific LLM Pruning Framework (Modified Version)

This repository is an extended and customized version of the original
🔗 2SSP framework: https://github.com/FabrizioSandri/2SSP

The original 2SSP algorithm introduces Two-Stage Structured Pruning for compressing transformer-based large language models (LLMs).
In this project, the framework has been adapted to support domain-specific datasets, enabling pruning experiments on health and hallucination evaluation corpora.

All modifications made to the base 2SSP framework are documented in Appendix B of the dissertation accompanying this project.

📌 Overview of This Repository

This repository contains:

✔️ Four custom datasets used for domain-specific pruning

✔️ A dataset conversion utility (Convert dataset.py) to convert arbitrary CSV files into HuggingFace datasets

✔️ A Jupyter notebook (Llama Pruning notebook.ipynb) demonstrating pruning experiments
Datasets Included (4 Total)

This repo contains four datasets used in pruning experiments:

Dataset	Description
halueval.csv	Hallucination evaluation samples
Healthver.csv	Health claim verification dataset
Medquad.csv	Medical question–answering dataset
Codah.xlsx	Commonsense reasoning dataset

These datasets were converted into the HuggingFace Dataset format (.arrow) for compatibility with 2SSP.
Dataset Conversion Utility

The script Convert dataset.py converts any CSV/XLSX dataset into a format required by the 2SSP framework.

✔️ It performs:

Cleaning and normalization

Constructing a "text" field

Saving to HuggingFace format (dataset.save_to_disk())

Example usage:

from datasets import Dataset
dataset = Dataset.from_pandas(df[['text']])
dataset.save_to_disk("./data/my_dataset")

✔️ Integration with 2SSP

The modified datasets.py includes a function:

def load_custom_dataset(local=True, path="./data/my_dataset"):
    from datasets import load_from_disk
    return load_from_disk(path)


This allows 2SSP to prune models using any custom dataset stored in ./data/.
Llama Pruning notebook.ipynb

This notebook provides a complete pruning workflow:

Included in the notebook:

Loading LLaMA-2 models (HuggingFace)

Converting datasets into token sequences

Running 2SSP pruning at multiple sparsity levels (25%, 37.5%, 50%)

Computing perplexity on custom datasets
Pruning Commands

Once datasets are prepared, LLaMA pruning can be run with:

python main.py \
  --model meta-llama/Llama-2-7b-hf \
  --pruning_method 2ssp \
  --sparsity_rate -2 \
  --evaluate_perplexity \
  --cache_dir ./cache


This runs 2SSP pruning for three sparsity levels:

25%

37.5%

50%

and evaluates perplexity on your custom validation dataset.
Acknowledgement

This work extends the excellent pruning framework developed by the original authors of 2SSP:
🔗 https://github.com/FabrizioSandri/2SSP

All credit for the Two-Stage Structured Pruning algorithm belongs to them.
