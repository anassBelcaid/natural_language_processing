"""CS 351 Project 01: The NLP Time Machine.

Complete only the functions marked "Your implementation." The remaining code is provided so that
you can focus on the ideas that distinguish the three eras of NLP.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


POSITIVE_WORDS = {
    "amazing", "best", "clear", "excellent", "fast", "good", "helpful",
    "impressive", "love", "reliable", "smooth", "wonderful",
}

NEGATIVE_WORDS = {
    "awful", "bad", "broken", "confusing", "disappointing", "hate",
    "poor", "slow", "terrible", "unreliable", "useless", "worst",
}

NEGATIONS = {"no", "not", "never"}


def tokenize(text: str) -> list[str]:
    """Return lowercase alphabetic tokens, preserving contractions.

    Example:
        >>> tokenize("It's NOT reliable!")
        ["it's", "not", "reliable"]
    """
    # Your implementation: replace the exception below.
    raise NotImplementedError


def lexicon_score(tokens: Sequence[str]) -> int:
    """Return positive-count minus negative-count, accounting for negation.

    A sentiment word is negated when the token immediately before it is one of
    ``no``, ``not``, or ``never``. Neutral words contribute zero.
    """
    # Your implementation: replace the exception below.
    raise NotImplementedError


def rule_based_predict(text: str) -> str:
    """Predict ``positive``, ``negative``, or ``neutral`` from a review."""
    # Your implementation: replace the exception below.
    raise NotImplementedError


def build_statistical_classifier() -> Pipeline:
    """Return the supplied TF–IDF plus logistic-regression baseline."""
    return Pipeline(
        [
            ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
            ("classifier", LogisticRegression(max_iter=1_000, random_state=351)),
        ]
    )


def fit_statistical_classifier(
    texts: Sequence[str], labels: Sequence[str]
) -> Pipeline:
    """Fit and return the supplied statistical classifier."""
    model = build_statistical_classifier()
    return model.fit(texts, labels)


def transformer_predict(texts: Sequence[str]) -> list[str]:
    """Optional demonstration using a pretrained sentiment pipeline.

    Install the optional dependency with ``uv add transformers torch`` before
    calling this function. Transformer inference is intentionally not graded.
    """
    try:
        from transformers import pipeline
    except ImportError as exc:
        raise RuntimeError(
            "Install the optional demo dependencies: uv add transformers torch"
        ) from exc

    classifier = pipeline("sentiment-analysis")
    outputs = classifier(list(texts))
    return [output["label"].lower() for output in outputs]
