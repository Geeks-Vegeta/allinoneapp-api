import sys
import os
value = os.path.dirname(os.path.abspath("app.py"))

sys.path.append(value)

from app import app
import json


def test_link1():
    response = app.test_client().post(f"/shortlink?mode=tinyurl&link=https://www.youtube.com/watch?v=R8_veQiYBjI")
    data = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert data["url"] == "https://tinyurl.com/25rmyhh5"
