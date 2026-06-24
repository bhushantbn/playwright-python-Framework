def test_create_user(playwright):
    request_context = playwright.request.new_context()

    response = request_context.post(
        "https://jsonplaceholder.typicode.com/users",
        data={
            "name": "Bhushan",
            "email": "bhushan@test.com"
        }
    )

    assert response.status == 201

    body = response.json()
    print(body)

    request_context.dispose()