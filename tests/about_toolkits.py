import pytest
from langchain import FAISS, OpenAI
from langchain.agents.agent_toolkits import (
    VectorStoreInfo,
    VectorStoreToolkit,
    create_vectorstore_agent,
)
from langchain.document_loaders import TextLoader
from langchain.embeddings import GPT4AllEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


def test_store_toolkit_can_be_brittle():
    #
    # agent toolkits can be brittle. they parse responses and the LLM
    # needs to structure its response appropriately.
    #
    # this test uses local embedding to save costs
    # then, it uses an agent with OpenAI because we need
    # a very capable LLM that can formulate response in a way that can
    # be parsed.
    #
    # Set your OPENAI_API_KEY before running
    #
    pytest.fail(
        "TODO: remove before you start. Failing by default to avoid \
                extra calls to Open AI"
    )

    loader = TextLoader("fixtures/wow.txt")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=300, chunk_overlap=80
    )

    texts = text_splitter.split_documents(documents)

    embeddings = GPT4AllEmbeddings()
    wow = FAISS.from_documents(texts, embeddings)

    llm = OpenAI(temperature=0)

    vectorstore_info = VectorStoreInfo(
        name="wow_collection",
        description="war of the worlds",
        vectorstore=wow,
    )
    toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info, llm=llm)
    agent = create_vectorstore_agent(llm=llm, toolkit=toolkit, verbose=True)

    # LLM provides answer directly without an action/observation which breaks langchain
    # parsing
    # https://github.com/langchain-ai/langchain/issues/3750
    res = agent.run("what was the key point in war of the worlds")

    # this is better since it requires some "thinking"
    res = agent.run("what did the person say in war of the worlds")

    print(res)
    pytest.fail(
        "TODO: observe the results and remove this when done \
                note - you can delete this to avoid calls to OpenAI"
    )
