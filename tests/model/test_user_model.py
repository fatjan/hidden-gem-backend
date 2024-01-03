import unittest
from app.main import create_app
from app.extensions import db
from app.main.model.user import User

user_data = {
    "username": "aqiz",
    "email": "aqiz@gmail.com",
    "password": "Aqiz123!"
}

class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_object="app.test_settings")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_user(self):
        # ARRANGE
        user_model = User()
        new_user = user_model.register_user(user_data)
        # ASSERT
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user["username"], user_data["username"])
        self.assertEqual(new_user["email"], user_data["email"])

    def test_update_user(self):
        # ARRANGE
        user_model = User()
        user = user_model.register_user(user_data)

        # ACT
        updated_data = {
            "username": "aqiz edited",
            "email": "aqiz_edited@gmail.com",
            "password": "Aqiz12345!"
        }
        updated_user = user_model.update_user(user["public_id"], updated_data)

        # ASSERT
        self.assertIsNotNone(updated_user)
        self.assertEqual(user["public_id"], updated_user["public_id"])
        self.assertEqual(user["username"], user_data["username"])
        self.assertEqual(user["email"], user_data["email"])

    def test_get_all_users(self):
        # ARRANGE
        user_model = User()
        user = user_model.register_user(user_data)

        # ACT
        retrieved_users = user_model.get_all_users()

        # ASSERT
        self.assertIsNotNone(retrieved_users)
        self.assertEqual(len(retrieved_users), 1)
        self.assertEqual(user["public_id"], retrieved_users[0]["public_id"])
        self.assertEqual(user["username"], retrieved_users[0]["username"])
        self.assertEqual(user["email"], retrieved_users[0]["email"])

    def test_get_user_by_id(self):
        # ARRANGE
        user_model = User()
        user = user_model.register_user(user_data)

        # ACT
        retrieved_users = user_model.get_user_by_id(user["public_id"])

        # ASSERT
        self.assertIsNotNone(retrieved_users)
        self.assertEqual(user["public_id"], retrieved_users["public_id"])
        self.assertEqual(user["username"], retrieved_users["username"])
        self.assertEqual(user["email"], retrieved_users["email"])
        
    def test_delete_user(self):
        # ARRANGE
        user_model = User()
        user = user_model.register_user(user_data)

        # ACT
        deleted_user = user_model.delete_user(user["public_id"])

        # ASSERT
        self.assertIsNotNone(deleted_user)
        self.assertEqual(deleted_user,True)

    def test_update_user_status(self):
        # ARRANGE
        user_model = User()
        user = user_model.register_user(user_data)

        # ACT
        updated_user = user_model.update_user_status(user["public_id"])

        # ASSERT
        self.assertIsNotNone(updated_user)
        self.assertEqual(updated_user['status'],"inactive")



if __name__ == "__main__":
    unittest.main()
