def test_given_request_with_unsupported_content_type_then_return_http_status_415(client):
    response = client.post(
        "/task1/",
        data="Given request body",
        content_type='text/plain'
    )
    assert response.status_code == 415
    assert ("Invalid request! Request should contain JSON body." in response.text) == True


def test_given_invalid_request_then_return_http_status_400(client):
    response = client.post(
        "/task1/",
        json={
            "first_names": [
                ["John", "4321e"]
            ]
        }
    )
    assert response.status_code == 400
    assert ("Invalid item: ['John', '4321e']. ID not numeric!" in response.text) == True


def test_given_non_existing_path_then_return_http_status_404(client):
    response = client.post("/task11/")
    assert response.status_code == 404
    assert response.text == "404 Not Found"
