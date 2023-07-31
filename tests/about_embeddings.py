import pytest
import tiktoken
from langchain.embeddings import GPT4AllEmbeddings


def test_embed_gpt4all(t):
    gpt = GPT4AllEmbeddings()
    embeds = gpt.embed_documents(["hello world"])

    # TODO: fix this. print embeds to see what they are, and put a number here
    assert len(embeds) == 0


def test_embed_huggingface():
    pytest.fail("TODO: find how create this sentence transformer 'st'")
    # use sentence transformers model: 'all-MiniLM-L6-v2'
    st = None

    embeds = st.embed_documents(["hello world"])
    assert len(embeds) > 100


def test_cost_estimator():
    tt = tiktoken.encoding_for_model("gpt-3.5-turbo")
    sentence = "Different encodings are used in openai: cl100k_base, p50k_base, gpt2"
    embeddings = tt.encode(sentence)

    # TODO: fix this. Words turn into tokens, which turn into embeddings.
    # So the number of embedding isn't 1:1 the number of words
    assert len(embeddings) == len(sentence.split(" "))
