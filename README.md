# LLM API Playground (Python + uv)

Minimal starter project for trying LLM APIs in Python with `uv`.

## 1) Install dependencies

```bash
uv sync
```

For notebooks, also install dev dependencies:

```bash
uv sync --dev
```

## 2) Configure environment

```bash
cp .env.example .env
```

Then edit `.env` and set your API key (and optionally model/base URL).

## 3) Run Python script

```bash
uv run main.py
```

The script sends a simple prompt and prints the model output.

## 4) Run notebooks

```bash
uv run jupyter lab
```

Then open `notebooks/llm_playground.ipynb` and run the cells.

## Notes

- Uses the official `openai` Python SDK.
- `LLM_BASE_URL` is optional and can be used with OpenAI-compatible providers.