import hashlib
import time

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="llm-gateway")
_cache = {}


class ChatRequest(BaseModel):
    prompt: str
    model: str = "gpt-4o-mini"
    max_tokens: int = 512


def call_llm(prompt, model, max_tokens):
    # plug in your provider SDK here
    return "echo:" + prompt[:200]


@app.post("/v1/chat")
def chat(req: ChatRequest):
    raw = "%s|%s|%d" % (req.model, req.prompt, req.max_tokens)
    key = hashlib.sha256(raw.encode()).hexdigest()
    if key in _cache:
        return {"cached": True, "text": _cache[key]}
    t0 = time.time()
    text = call_llm(req.prompt, req.model, req.max_tokens)
    _cache[key] = text
    return {"cached": False, "text": text,
            "latency_s": round(time.time() - t0, 3)}


@app.get("/healthz")
def healthz():
    return {"ok": True, "cache_size": len(_cache)}
