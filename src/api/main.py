from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    history: list | None = None


app = FastAPI(title='enterprise-rag-agent')

@app.get('/health')
def health():
    return {'status': 'ok'}



@app.post("/chat")
def chat(request: ChatRequest):
    history = request.history if request.history else []
    return {
        "response": f"你发的消息是：{request.message}",
        "history_length": len(history)  # 返回历史记录长度
    }


