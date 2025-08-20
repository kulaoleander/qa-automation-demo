# tests_api/test_httpbin.py
import requests

def test_get_httpbin():
    r = requests.get("https://httpbin.org/get", timeout=10)
    assert r.status_code == 200
    data = r.json()
    # httpbin 会把你的请求信息返回回来
    assert "url" in data
    assert data["url"].startswith("https://httpbin.org/get")

def test_post_httpbin():
    payload = {"name": "qa", "level": "junior"}
    r = requests.post("https://httpbin.org/post", json=payload, timeout=10)
    assert r.status_code == 200
    data = r.json()
    # json 字段里应包含我们发送过去的 payload
    assert data["json"] == payload
