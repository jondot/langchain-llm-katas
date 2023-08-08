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


def test_chunk_sizing_can_be_deceptive():
    with open("fixtures/wow.txt") as f:
        text = f.read()

        # TODO: chunk sizes can be deceptive. when you need to fit into a context,
        # because the context window is 4k tokens (or another limit),
        #
        # You'll see many examples use '1000' as a limit, this is *usually* char
        # count.
        # And, it roughly translates into 200-400 tokens which is why it's a good
        # number for many of these examples, on a 4k token limit, we can stuff a solid
        # 4-5 top examples for priming the context of the prompt.
        #
        # When you stuff content into a prompt in this way, you want to split
        # text accurately in order not to go over limit, but guess what?

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)

        splits = splitter.split_text(text)

        # GOOD: as expected
        assert [len(s) for s in splits[1:3]] == [999, 339]

        splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000, chunk_overlap=10
        )

        splits = splitter.split_text(text)

        # TODO: fix this
        assert [len(s) for s in splits[1:3]] == [999, 339]
