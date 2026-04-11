# -*- coding: utf-8 -*-


class TestStart:
    def test_get_returns_200(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_get_contains_link_to_print(self, client):
        response = client.get('/')
        assert b'/print' in response.data


class TestPrinterGet:
    def test_get_returns_200(self, client):
        response = client.get('/print')
        assert response.status_code == 200

    def test_get_renders_form(self, client):
        response = client.get('/print')
        assert b'<form' in response.data
        assert b'name="text"' in response.data


class TestPrinterPost:
    def test_post_with_text_redirects(self, client):
        response = client.post('/print', data={'text': 'hello'})
        assert response.status_code == 302
        assert response.headers['Location'] == '/'

    def test_post_with_text_flashes_message(self, client):
        response = client.post('/print', data={'text': 'hello'}, follow_redirects=True)
        assert b'hello!!!' in response.data

    def test_post_empty_text_returns_form_error(self, client):
        response = client.post('/print', data={'text': ''})
        assert response.status_code == 200
        assert b'error' in response.data.lower() or b'This field is required' in response.data

    def test_post_missing_text_stays_on_form(self, client):
        response = client.post('/print', data={})
        assert response.status_code == 200
        assert b'<form' in response.data
