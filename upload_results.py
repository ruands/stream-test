import json
import requests

data_set_1 = {
    "test_id": 2,
    "scores": [
        {
            "student_id": 1,
            "score": 76
        },
        {
            "student_id": 2,
            "score": 45
        },
        {
            "student_id": 3,
            "score": 83
        },
        {
            "student_id": 4,
            "score": 26
        }
    ]
}

def send(url, scores):
    resp = requests.post(url,json=scores)
    print(resp.status_code)
    print(resp.text)


send("http://127.0.0.1:8000/api/v1/scores/", data_set_1)
