#############################################
## 2SSP – Domain-Specific LLM Pruning Framework (Modified Version) ##
#############################################

This repository is an extended and customized version of the original 2SSP pruning framework:
https://github.com/FabrizioSandri/2SSP

The original 2SSP algorithm introduces Two-Stage Structured Pruning for compressing transformer-based Large Language Models (LLMs). In this project, the framework has been adapted to support domain-specific datasets, enabling pruning experiments on healthcare, commonsense reasoning, and hallucination evaluation corpora.

All modifications made to the base 2SSP framework are documented in Appendix B of the dissertation accompanying this work.


==============================
## OVERVIEW OF THIS REPOSITORY ##
==============================

This repository contains:
- Four custom datasets used for domain-specific LLM pruning
- A dataset conversion utility (Convert dataset.py) for converting CSV/XLSX files into HuggingFace datasets
- A Jupyter notebook (Llama Pruning notebook.ipynb) demonstrating pruning experiments and evaluation


==============================
## DATASETS INCLUDED (4 TOTAL) ##
==============================

The following datasets were used for pruning and perplexity evaluation:

1. halueval.csv   – Hallucination evaluation samples  
2. Healthver.csv  – Health claim verification dataset  
3. Medquad.csv    – Medical question–answering dataset  
4. Codah.xlsx     – Commonsense reasoning dataset  

All datasets were converted into HuggingFace Dataset format (.arrow) for compatibility with 2SSP.


==============================
## DATASET CONVERSION UTILITY ##
==============================

The script "Convert dataset.py" converts arbitrary CSV/XLSX files into the required HuggingFace dataset structure.

It performs:
- Cleaning and normalization
- Creation of a unified "text" field
- Saving using the dataset.save_to_disk() method

Example usage:

from datasets import Dataset
dataset = Dataset.from_pandas(df[['text']])
dataset.save_to_disk("./data/my_dataset")

Integration with the modified 2SSP loader:

def load_custom_dataset(local=True, path="./data/my_dataset"):
    from datasets import load_from_disk
    return load_from_disk(path)


==============================
## LLAMA PRUNING NOTEBOOK ##
==============================

The notebook "Llama Pruning notebook.ipynb" contains:
- Loading of LLaMA-2 models from HuggingFace
- Tokenization of custom datasets
- Running 2SSP pruning at 25%, 37.5%, and 50% sparsity
- Computing perplexity on the domain dataset
- Saving and analyzing pruning results


==============================
## PRUNING COMMANDS ##
==============================

After dataset preparation, pruning may be executed using:

python main.py \
    --model meta-llama/Llama-2-7b-hf \
    --pruning_method 2ssp \
    --sparsity_rate -2 \
    --evaluate_perplexity \
    --cache_dir ./cache

The argument:
--sparsity_rate -2  
triggers pruning at the following sparsity levels:
- 25%
- 37.5%
- 50%

Perplexity is computed on the provided custom validation dataset.


==============================
## ACKNOWLEDGEMENT ##
==============================

This work extends the pruning framework created by the original authors of 2SSP:
https://github.com/FabrizioSandri/2SSP

All credit for the Two-Stage Structured Pruning algorithm belongs to the original authors.
