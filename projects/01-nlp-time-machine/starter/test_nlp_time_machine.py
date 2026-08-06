"""Public autograder for Project 01."""

from nlp_time_machine import (
    build_statistical_classifier,
    lexicon_score,
    rule_based_predict,
    tokenize,
)


def test_tokenize_lowercases_and_removes_punctuation():
    assert tokenize("Amazing, CLEAR results!") == ["amazing", "clear", "results"]


def test_tokenize_preserves_contractions():
    assert tokenize("It's helpful; don't stop.") == ["it's", "helpful", "don't", "stop"]


def test_positive_lexicon_score():
    assert lexicon_score(["a", "good", "reliable", "tool"]) == 2


def test_negative_lexicon_score():
    assert lexicon_score(["slow", "and", "confusing"]) == -2


def test_negation_reverses_positive_word():
    assert lexicon_score(["not", "good"]) == -1


def test_negation_reverses_negative_word():
    assert lexicon_score(["never", "bad"]) == 1


def test_prediction_labels():
    assert rule_based_predict("An excellent and reliable tool") == "positive"
    assert rule_based_predict("A terrible, confusing tool") == "negative"
    assert rule_based_predict("The tool arrived yesterday") == "neutral"


def test_statistical_pipeline_is_supplied():
    model = build_statistical_classifier()
    assert list(model.named_steps) == ["tfidf", "classifier"]
