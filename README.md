# llm-gateway-hq

FastAPI gateway in front of an LLM with response caching

## How to use

```bash
curl localhost:8000/v1/chat \
  -H 'content-type: application/json' \
  -d '{"prompt": "hello", "model": "gpt-4o-mini"}'
```

## Getting started

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Features

- Latency measured and returned per request
- POST /v1/chat with prompt/model/max_tokens
- Provider SDK plugs into one function
- SHA-256 keyed in-memory response cache

## Project structure

```text
├── docs/
│   ├── configuration.md
│   ├── faq.md
│   ├── roadmap.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── main.py
└── requirements.txt
```

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Acknowledgments

- README structure inspired by popular OSS templates
- Thanks to everyone opening issues with ideas
