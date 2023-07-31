import pytest
from langchain import PromptTemplate


def FIXME():  # noqa: N802
    return None


def test_prompt_templates():
    prompt = PromptTemplate.from_template(
        """\
You are an expert guitar maker.
What is a good measurement for string height?"""
    )

    # TODO: make the template render different things
    assert (
        prompt.format()
        == """\
You are an expert guitar maker.
What is a good measurement for pickup distance?"""
    )


def test_fewshot_prompt():
    _shots = [
        {"category": "blues", "progression": "1,4,4,2,1"},
        {"category": "jazz", "progression": "1,1,1,1,2"},
    ]
    prompt = PromptTemplate(
        input_variables=["query"],
        template="this is the wrong prompt formatting {query}",
    )
    assert (
        prompt.format(query="melodic and sad music")
        == """\
category: blues
chord progression: 1,4,4,2,1

category: jazz
chord progression: 1,1,1,1,2

Qustion: act as a musical expert. Give me a chord progression\
 for melodic and sad music"""
    )


def test_prompts_can_be_stored_and_loaded():
    pytest.fail("TODO: fix this by loading from 'fixtures/example_prompt.yaml'")
    prompt = FIXME()

    assert (
        prompt.format(adjective="funny", content="chickens")
        == "Tell me a funny joke about chickens."
    )
