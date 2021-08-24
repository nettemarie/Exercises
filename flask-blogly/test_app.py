# from app import app
# from models import db, connect_db, User, Post, Tag
# from flask import Flask, session
# from flask_sqlalchemy import SQLAlchemy
# import unittest
# from unittest import TestCase


# app.config["TESTING"] = True
# app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


# class BloglyTestCase(TestCase):

#     app = Flask(__name__)
#     db = SQLAlchemy(app)

#     # def setUp(self):
#     #     self.app.config["TESTING"] = True
#     #     self.app.config["DEBUG"] = False
#     #     self.app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
#     #     self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     #     self.app = self.app.test_client()
#     #     self.db.drop_all()
#     #     self.db.create_all()
#     #     new_user = User(
#     #         first_name="Antoinette",
#     #         last_name="Medlock",
#     #         image_url=None,
#     #     )

#     #     db.session.add(new_user)
#     #     db.session.commit()

#     def tearDown(self):
#         user = User.query.filter_by(first_name="Tommy").first()
#         self.db.session.remove()
#         db.session.delete(user)

#     def test_user_submit(self):
#         with app.test_client() as client:
#             res = client.post(
#                 "/users/new",
#                 data={
#                     "first_name": "Tommy",
#                     "last_name": "Lewis",
#                     "image_url": "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png",
#                 },
#             )
#             html = res.get_data(as_text=True)

#             # user = User.query.filter_by(first_name="Tommy").first()
#             # self.db.session.remove()
#             # db.session.delete(user)

#             self.assertEqual(res.status_code, 302)
#             self.assertEqual(res.location, "http://localhost/users")
#             # self.db.session.remove()
#             # db.session.delete(user)
#             # self.assertIn("Antoinette Medlock", html)

#     def test_new_user(self):
#         user = {
#             "first_name": "Antoinette",
#             "last_name": "Medlock",
#             "image_url": "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png",
#         }
#         with app.test_client() as client:
#             res = client.get(
#                 "/users",
#                 data=user,
#             )

#             html = res.get_data(as_text=True)

#             self.assertEqual(res.status_code, 200)
#             self.assertIn("Antoinette Medlock", html)
#             self.db.session.remove()
#             db.session.delete(user)

#     def test_post_submit(self):
#         with app.test_client() as client:
#             res = client.post(
#                 "/",
#                 data={
#                     "title": "Test",
#                     "content": "Test post",
#                     "user": "Antoinette Medlock",
#                     "user_id": "1",
#                 },
#             )
#             html = res.get_data(as_text=True)

#             self.assertEqual(res.status_code, 302)
#             self.assertIn("Test", html)


# if __name__ == "__main__":
#     unittest.main()
#     app.run()
