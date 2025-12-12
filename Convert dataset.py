from datasets import Dataset
import pandas as pd
import ast

df = pd.read_csv("med.csv")

# Convert the evidence_descriptions (string representation of list) into plain text
def flatten_evidence(text):
    try:
        items = ast.literal_eval(text)  
        if isinstance(items, list):
            return " ".join(items)
        return str(items)
    except Exception:
        return str(text)

df["text"] = df["evidence_descriptions"].apply(flatten_evidence)

# Keep only the text column
dataset = Dataset.from_pandas(df[["text"]])

dataset.save_to_disk("./data/my_dataset")
