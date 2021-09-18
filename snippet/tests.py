from django.test import TestCase

class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_top_returns_excepted_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")



