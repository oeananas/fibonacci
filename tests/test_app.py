def test_get_fibonacci_with_params_first(client):
    response = client.get('/fibonacci?from=1&to=10')
    assert response.status_code == 200


def test_get_fibonacci_with_params_second(client):
    response = client.get('/fibonacci?from=1&to=20')
    assert response.status_code == 200


def test_get_fibonacci_with_params_third(client):
    response = client.get('/fibonacci?to=20&from=1')
    assert response.status_code == 200


def test_get_fibonacci_with_incorrect_url(client):
    response = client.get('/')
    assert response.status_code == 404


def test_get_fibonacci_without_params(client):
    response = client.get('/fibonacci')
    assert response.status_code == 422


def test_get_fibonacci_with_incorrect_params_string_first(client):
    response = client.get('/fibonacci?hello=world')
    assert response.status_code == 422


def test_get_fibonacci_with_incorrect_params_string_second(client):
    response = client.get('/fibonacci?from=world&to=12')
    assert response.status_code == 422


def test_get_fibonacci_with_incorrect_params_string_third(client):
    response = client.get('/fibonacci?from=1&to=qwerty')
    assert response.status_code == 422


def test_get_fibonacci_with_incorrect_params_extra_first(client):
    response = client.get('/fibonacci?from=1&to=15&foo=bar')
    assert response.status_code == 422


def test_get_fibonacci_with_incorrect_params_extra_second(client):
    response = client.get('/fibonacci?from=1&to=-15&foo=bar')
    assert response.status_code == 422


def test_get_fibonacci_with_incorrect_params_min_first(client):
    response = client.get('/fibonacci?from=-100&to=0')
    assert response.status_code == 422


def test_get_fibonacci_with_incorrect_params_min_second(client):
    response = client.get('/fibonacci?from=1&to=-100')
    assert response.status_code == 422

