## Judge Small Language Models ##

2SSP – Domain-Specific LLM Pruning Framework 

This repository is an extended and customized version of the original
🔗 2SSP framework: https://github.com/FabrizioSandri/2SSP

The original 2SSP algorithm introduces Two-Stage Structured Pruning for compressing transformer-based Large Language Models (LLMs).
In this project, the framework has been adapted to support domain-specific datasets, enabling pruning experiments on healthcare, medical QA, and hallucination evaluation corpora.

All modifications made to the base 2SSP framework are documented in Appendix B of the dissertation accompanying this work.

📌 Overview of This Repository

This repository contains:

✔️ Four custom datasets used for domain-specific pruning

✔️ A dataset conversion utility (Convert dataset.py) that converts arbitrary CSV/XLSX files into HuggingFace datasets

✔️ A Jupyter notebook (Llama Pruning notebook.ipynb) demonstrating pruning experiments and results

📊 Datasets Included (4 Total)

This repository includes four datasets used for pruning and perplexity evaluation:

Dataset Name	Description
halueval.csv	Hallucination evaluation samples
Healthver.csv	Health claim verification dataset
Medquad.csv	Medical question–answering dataset
Codah.xlsx	Commonsense reasoning dataset

These datasets were converted into the HuggingFace Dataset format (.arrow) for compatibility with 2SSP.

🔄 Dataset Conversion Utility: Convert dataset.py

The script Convert dataset.py converts any CSV/XLSX dataset into a format required by the 2SSP pruning framework.

✔️ Steps performed by the script

Cleaning and normalization

Constructing a unified "text" field

Saving the dataset using HuggingFace's dataset.save_to_disk()

Example Usage
from datasets import Dataset
dataset = Dataset.from_pandas(df[['text']])
dataset.save_to_disk("./data/my_dataset")

🔧 Integration with 2SSP

The modified datasets.py file includes a helper function:

def load_custom_dataset(local=True, path="./data/my_dataset"):
    from datasets import load_from_disk
    return load_from_disk(path)


This enables 2SSP to prune models using any custom dataset placed inside the ./data/ directory.

✂️ Llama Pruning Notebook

The notebook Llama Pruning notebook.ipynb provides a complete workflow for:

Loading LLaMA-2 models from HuggingFace

Tokenizing custom datasets

Running structured pruning at multiple sparsity levels

25%

37.5%

50%

Computing perplexity on the domain dataset

Recording and visualizing pruning results

🧪 Pruning Commands

After preparing datasets, LLaMA pruning may be executed with:

python main.py \
  --model meta-llama/Llama-2-7b-hf \
  --pruning_method 2ssp \
  --sparsity_rate -2 \
  --evaluate_perplexity \
  --cache_dir ./cache


This command runs 2SSP pruning at three sparsity levels:

25%

37.5%

50%

and evaluates perplexity on the custom validation dataset.

🙏 Acknowledgement

This work builds upon the excellent pruning framework developed by the authors of 2SSP:
🔗 https://github.com/FabrizioSandri/2SSP

Full credit for the Two-Stage Structured Pruning algorithm belongs to the original authors.
