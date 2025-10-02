import requests


def test_delete():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')

    assert response.status_code == 204

# создать задачу, удалить созданную задачу, проверить что гет по удалённой задаче == 404


def test_create_delete_verify():
    url = "https://todo-app-sky.herokuapp.com/"

    create_response = requests.post(
        {url}, json={"title": "Тренировка", "completed": True})
    new_id = create_response.json()["id"]

    delete_response = requests.delete(f"({url}/{new_id}")

    assert delete_response.status_code == 201

    get_response = requests.get(f"{url}/{new_id}")

    assert get_response.status_code == 404
