import fitz  # type: ignore  # noqa: PGH003
import pytest
from langchain.document_loaders import UnstructuredFileLoader
from toolz import filter, first  # type: ignore  # noqa: PGH003


def test_read_pdf():
    with fitz.open("fixtures/paper.pdf"):
        # TODO: figure out how to extract text from pages
        pages = []
        assert len(pages) == 30


# troubleshooting apple silicon with unstructured throws an lxml related panic
# https://apple.stackexchange.com/questions/436801/m1-mac-mach-o-file-but-is-an-incompatible-architecture-have-x86-64-need-a
def test_use_unstructured():
    pytest.fail("TODO: use UnstructuredPDFLoader to read 'fixtures/paper.pdf'")
    assert len(data) == 1
    assert list(data[0].dict().keys()) == ["page_content", "metadata"]
    assert len(data[0].page_content) > 100000


def test_you_can_load_folders():
    # TODO: load all files from 'fixtures/' regardless of their format
    docs = []
    assert len(docs) == 4
    pdf = first(
        filter(lambda doc: doc.metadata["source"] == "fixtures/paper.pdf", docs)
    )
    assert len(pdf.page_content) > 100000


def test_loaders_can_work_with_splitters():
    loader = UnstructuredFileLoader("fixtures/paper.pdf")
    doc = loader.load()
    assert len(doc) == 1

    # TODO: find a way to load and split to 33 documents with
    # RecursiveCharacterTextSplitter
    doc = []
    assert len(doc) == 33
