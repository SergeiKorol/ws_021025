import requests

def get_tasks_test():
    response = requests.get("https://todo-app-sky.herokuapp.com/")
    assert response.status_code == 200
    assert type(response.json()) is list

def test_new():
    body = {"title": "Полить цветы", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    respons_body = response.json()
    id = respons_body ['id']
    body_2 = {"completed": True}
    requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body_2)
    response = requests.get(f"https://todo-app-sky.herokuapp.com/{id}")
    get_respons = response.json()
    complite = get_respons['completed']
    assert complite == True
