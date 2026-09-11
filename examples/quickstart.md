# Quickstart

Fresh machine, five minutes.

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then:

```bash
curl localhost:8000/v1/chat \
  -H 'content-type: application/json' \
  -d '{"prompt": "hello", "model": "gpt-4o-mini"}'
```

If nothing happens, check docs/usage.md first.
