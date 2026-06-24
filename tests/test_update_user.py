def test_update_user(playwright):
    request_context = playwright.request.new_context()

    response = request_context.put(
        "https://jsonplaceholder.typicode.com/users/1",
        data={
            "name": "Bhushan",
            "email": "bhushan@test.com"
        }
    )

    assert response.status == 200

    body = response.json()
    print(body)

    request_context.dispose()