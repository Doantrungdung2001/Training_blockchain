from main import app
import json
import unittest


class BooksTests(unittest.TestCase):
    """ Unit testcases for REST APIs """

    def test_get_all_books(self):
        request, response = app.test_client.get('/books')
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        self.assertGreaterEqual(data.get('n_books'), 0)
        self.assertIsInstance(data.get('books'), list)

    # TODO: unittest for another apis

    def test_register_user(self):
        user = {
            "username": "trungdung",
            "password": "1234567"
        }

        request, response = app.test_client.post('/user/register',json = user)
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        # if(data['status'],'login success'):
        # auth_token = data["token"]
        # headers = {"Authorization": f"Bearer {auth_token}"}
        # return headers

    def test_login_user(self):
        user = {
            "username": "trungdung",
            "password": "1234567"
        }
        request, response = app.test_client.post('/user/login',json = user)
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        print(data)
        # auth_token = data["token"]
        # headers = {"Authorization": f"Bearer {auth_token}"}
        # return headers

    def test_get_book_by_id(self):
        id = 'ed38c908-b4ab-4d43-b46e-3a58f14a498c'
        request, response = app.test_client.get(f'/books/{id}')
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        # self.assertEqual(data.get('_id'),'ed38c908-b4ab-4d43-b46e-3a58f14a498c')
        self.assertEqual(data['status'], 'success')
        self.assertIsInstance(data.get('books'), list)

    def test_create_book(self):
        headers = self.test_login_user()

        book = {
            "title": "book test",
            "authors": ["Dung"],
            "description": "Nothing",
            "publisher": "2024"
        }

        # Make a POST request to create the book
        request, response = app.test_client.post('/books', json=book, headers=headers)
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        self.assertEqual(data['status'], 'success')
        request, response = app.test_client.get('/books')
        data = json.loads(response.text)
        books = data['books']
        self.assertTrue(any(b['title'] == 'book test' for b in books))

    #
    def test_update_book(self):
        headers = self.test_login_user()
        print(headers)
        book = {
            "title": "book test update",
            "authors": ["Dung","Doan"],
            "description": "Nothing",
            "publisher": "2024"
        }
        request, response = app.test_client.put(f'/books/{id}', json=book, headers=headers)
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        self.assertEqual(data['status'], 'success')
        data = json.loads(response.text)
        books = data['books']
        self.assertTrue(any(b['title'] == 'book test' for b in books))

    def test_delete_book(self):
        headers = self.test_login_user()

        request, response = app.test_client.delete(f'/books/{id}', headers=headers)
        self.assertEqual(response.status, 200)
        data = json.loads(response.text)
        self.assertEqual(data['status'], 'success')

if __name__ == '__main__':
    unittest.main()
