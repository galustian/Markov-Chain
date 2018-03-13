# Markov-Chain
Word-Suggestion with Markov-Chains using Wikipedias 500 most important pages as data to train the model.

Run in following order to download the data & create the transition-matricies:
1. `python download-wiki-links.py`
2. `python download-wiki-articles.py`
3. `python create_transition_matrix.py`

Type words or sentences.
Example:
`python word-prediction.py Albert`

Output:
`Einstein`
