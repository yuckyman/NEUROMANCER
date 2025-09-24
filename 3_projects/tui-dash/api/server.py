from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="tui-dash API")

@app.get("/health")
async def health():
	return {"status": "ok"}
