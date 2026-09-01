from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    # CVE-2024-24762 触发点：FastAPI 处理用户输入的多部分表单
    return {"ok": True}
