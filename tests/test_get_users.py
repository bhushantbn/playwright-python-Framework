def test_get_users(playwright):
    request_context = playwright.request.new_context()

    response = request_context.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    assert response.status == 200

    users = response.json()

    # Assert we got a non-empty list
    assert len(users) > 0, "Expected at least one user in the response"

    print(f"\nTotal users retrieved: {len(users)}")
    print("-" * 50)

    for user in users:
        # Assert each user has the expected fields
        assert "id" in user
        assert "name" in user
        assert "username" in user
        assert "email" in user

        print(f"ID       : {user['id']}")
        print(f"Name     : {user['name']}")
        print(f"Username : {user['username']}")
        print(f"Email    : {user['email']}")
        print("-" * 50)