# Задача №2 Автотест API Яндекса

import unittest
import requests
import ya_api


class TestApiYaTranslate(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_right_result(self):
        text_for_translate = 'hello'
        result = 'привет'
        self.assertEqual(ya_api.translate_it(text_for_translate), result)

    def test_wrong_result(self):
        text_for_translate = 'hello'
        result = 'привед'
        self.assertNotEqual(ya_api.translate_it(text_for_translate), result)

    def test_get_response_200(self):
        params = {'key': ya_api.API_KEY, 'lang': 'ru', 'text': 'hello'}
        response = self.session.get(ya_api.URL, params=params)
        print(response.json()['text'][0])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['text'][0], 'привет')

    def test_get_response_401(self):
        params = {'key': '0', 'lang': 'en'}
        response = self.session.get(ya_api.URL, params=params)
        print(response.json()['message'])
        self.assertEqual(response.json()['code'], 401)

    def test_get_response_502(self):
        params = {'key': ya_api.API_KEY, 'lang': '123'}
        response = self.session.get(ya_api.URL, params=params)
        print(response.json()['message'])
        self.assertEqual(response.json()['code'], 502)


if __name__ == '__main__':
    unittest.main()
