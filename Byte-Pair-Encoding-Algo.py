import streamlit as st
from collections import Counter, defaultdict
import pandas as pd

# ---------------- BPE FUNCTIONS ----------------
def get_vocab(text):
    """Create vocabulary from input text."""
    vocab = Counter()
    for word in text.strip().split():
        word = " ".join(list(word)) + " </w>"
        vocab[word] += 1
    return vocab

def get_stats(vocab):
    """Get frequency of character pairs."""
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_vocab(pair, vocab):
    """Merge the most frequent pair."""
    bigram = " ".join(pair)
    replacement = "".join(pair)
    new_vocab = {}
    for word in vocab:
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="BPE Demo", page_icon="🔡", layout="centered")
st.title("🔡 Byte Pair Encoding (BPE) Demonstration")
st.write("This demo shows how Byte Pair Encoding (BPE) works step by step.")

# Input text
user_text = st.text_area("Enter your text:", "low lower newest widest")
num_merges = st.slider("Number of merges", min_value=1, max_value=20, value=10)

if st.button("Run BPE"):
    st.subheader("Step-by-step BPE Process")

    vocab = get_vocab(user_text)
    st.markdown("### Initial Vocabulary")
    st.json(vocab)

    for i in range(num_merges):
        pairs = get_stats(vocab)
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        freq_table = pd.DataFrame(pairs.items(), columns=["Pair", "Frequency"]).sort_values(by="Frequency", ascending=False)

        st.markdown(f"### Step {i+1}")
        st.write(f"**Merging Pair:** `{best}` → `{''.join(best)}`")
        st.dataframe(freq_table)

        vocab = merge_vocab(best, vocab)
        st.write("Updated Vocabulary:")
        st.json(vocab)

    st.subheader("✅ Final Subword Vocabulary")
    tokens = set()
    for word in vocab:
        tokens.update(word.split())
    st.write(tokens)
