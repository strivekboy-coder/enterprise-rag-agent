from fastapi import FastAPI

app = FastAPI(title='enterprise-rag-agent')

@app.get('/health')
def health():
    return {'status': 'ok'}