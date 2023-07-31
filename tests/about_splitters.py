from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)


def test_text_splitter_and_long_lines():
    with open("fixtures/wow.txt") as f:
        text = f.read()

        # TODO: find a better splitter. a line can be bigger than chunk_size and this
        # only cares about '\n\n' between lines.
        splitter = CharacterTextSplitter(
            separator="\n\n", chunk_size=50, chunk_overlap=10, length_function=len
        )

        splits = splitter.split_text(text)

        # view the splits
        # print("\n\n-----------------------\n\n".join(splits))

        assert len(splits[5]) < 50


def test_token_splitter_counts_what():
    with open("fixtures/wow.txt") as f:
        text = f.read()

        splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=50, chunk_overlap=10
        )

        splits = splitter.split_text(text)

        # TODO: why does this fail? fix this assertion.
        # hint: think - 50 counts of what?
        assert len(splits[5]) < 50
