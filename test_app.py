import unittest
import app
import json

class FunctionalTest(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_get(self):
        response = self.app.get('/hello')
        self.assertEqual(
            json.loads(response.data.decode()),
            {"message": "hello"}
        )

    def test_post(self):
        response = self.app.post(
             '/hello',
             data=json.dumps({"message": "hello"}),
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/json'}
    )

        self.assertEqual(
            200,
            response.status_code
        )
