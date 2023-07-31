import pytest
from langchain import FAISS
from langchain.embeddings import GPT4AllEmbeddings


def test_splitting_is_important():
    embeddings = GPT4AllEmbeddings()
    with open("fixtures/wow.txt") as f:
        db = FAISS.from_texts([f.read()], embeddings)
        # TODO: this always returns a single result. why?
        results = db.similarity_search("who was the enemy")
        assert len(results) == 4


def test_search_and_vector_search():
    embeddings = GPT4AllEmbeddings()
    db = FAISS.from_texts(
        [
            "You take a mortal man",
            "And put him in control",
            "Watch him become a God",
            "Watch people's heads a'roll",
            "Just like the Pied Piper",
            "Led rats through the streets",
            "We dance like marionettes",
            "Swaying to the symphony of destruction",
        ],
        embeddings,
    )
    sim = db.similarity_search("dancing")
    print(sim)
    # TODO: perform a vector similarity search
    vsim = []
    assert sim[0] == vsim[0]
    assert len(sim) == 4
    assert len(vsim) == 4


def test_maximum_marginal_relevance_avoids_repeats():
    embeddings = GPT4AllEmbeddings()
    db = FAISS.from_texts(
        [
            "You take a mortal man",
            "And put him in control",
            "Watch him become a God",
            "Watch people's heads a'roll",
            "Just like the Pied Piper",
            "Led rats through the streets",
            "We dance like marionettes",
            "We dance like puppets",  # not in the original song
            "We dance like cats",  # not in the original song
            "Swaying to the symphony of destruction",
        ],
        embeddings,
    )

    # puppets and cats are top results
    sim = db.similarity_search("dancing")
    print(sim)

    # no puppets and cats
    sim = db.max_marginal_relevance_search("dancing")
    print(sim)

    pytest.fail(
        "TODO: why is this happening? \
                 research MMR on the web and remove this when done"
    )


def test_store_and_load():
    embeddings = GPT4AllEmbeddings()
    db = FAISS.from_texts(
        [
            "You take a mortal man",
            "And put him in control",
            "Watch him become a God",
            "Watch people's heads a'roll",
            "Just like the Pied Piper",
            "Led rats through the streets",
            "We dance like marionettes",
            "We dance like puppets",  # not in the original song
            "We dance like cats",  # not in the original song
            "Swaying to the symphony of destruction",
        ],
        embeddings,
    )
    db.save_local("fixtures", "megavec")
    db = None

    pytest.fail("TODO: load the database so that results work")

    sim = db.similarity_search("dancing")
    assert len(sim) == 4
