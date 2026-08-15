# Project 01: The NLP Time Machine

The complete project lives in `nlp_time_machine.ipynb`. Students implement a
small but meaningful part of a rule system, a statistical classifier, and a
pretrained Transformer, then compare all three on the same sentiment dataset.

## Setup

Install the locked environment and open the notebook:

```bash
uv sync
uv run jupyter lab nlp_time_machine.ipynb
```

Run the notebook from top to bottom. A fresh starter intentionally stops at the
first `NotImplementedError`. Complete each TODO and rerun its check before
continuing.

The first run downloads Stanford SST-2 and the pretrained DistilBERT sentiment
model. Later runs reuse the local caches.

## Submission

Submit the completed `nlp_time_machine.ipynb` with all outputs preserved. The
final notebook must contain the comparison table, accuracy figure, model
disagreements, and 250–400 word reflection.
