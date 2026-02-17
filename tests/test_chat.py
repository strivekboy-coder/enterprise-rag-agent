def test_chat_ok(client):
    resp = client.post("/chat", json={"message": "hello", "history": []})
    assert resp.status_code == 200
    data = resp.json()
    assert data["response"] == "你发的消息是：hello"
    assert data["history_length"] == 0

def test_chat_missing_message_returns_422(client):
    resp = client.post("/chat", json={"history": []})
    assert resp.status_code == 422

