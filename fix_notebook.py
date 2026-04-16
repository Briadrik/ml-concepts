import json

# Load the notebook
with open(r'c:\Users\briad\OneDrive - Momentum Credit\Documents\GitHub\ml-concepts\bert-sentence-similarity\bert_sentence_similarity.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Remove metadata.widgets if it exists
if 'metadata' in notebook and 'widgets' in notebook['metadata']:
    del notebook['metadata']['widgets']
    print("Removed metadata.widgets from the notebook.")
else:
    print("metadata.widgets not found.")

# Save the notebook back
with open(r'c:\Users\briad\OneDrive - Momentum Credit\Documents\GitHub\ml-concepts\bert-sentence-similarity\bert_sentence_similarity.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print("Notebook saved.")