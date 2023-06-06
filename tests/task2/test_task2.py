def test_given_request_with_unsupported_content_type_then_return_http_status_415(client):
    response = client.post(
        "/task2/",
        data="{'data': 'Given request body'}",
        content_type='application/json'
    )
    assert response.status_code == 415
    assert ("Invalid request! Content type of a request should be text/plain." in response.text) == True


def test_given_balanced_text_then_return_http_status_200(client):
    response = client.post(
        "/task2/",
        data="""Python {is an easy to [learn]}, (powerful programming language. It)
    has efficient high-level [(data structures) and a simple but
    effective approach to object-oriented programming]. Python's elegant
    syntax and dynamic typing, together with its {interpreted nature,
    make it an ideal language (for) scripting and rapid} application
    development in many areas on most platforms.""",
        content_type='text/plain'
    )
    assert response.status_code == 200
    assert "Braces are balanced." == response.text


def test_given_unbalanced_text_then_return_http_status_400(client):
    response = client.post(
        "/task2/",
        data="""Python) {is easy to {learn]}.""",
        content_type='text/plain'
    )
    assert response.status_code == 400
    assert "Python) << brace is unbalanced." == response.text


def test_given_unbalanced_text_with_wrong_closing_brace_type_then_return_http_status_400(client):
    response = client.post(
        "/task2/",
        data="""Python (language) {is easy to learn[}].""",
        content_type='text/plain'
    )
    assert response.status_code == 400
    assert "Python (language) {is easy to learn[ << brace is unbalanced." == response.text
