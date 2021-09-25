from app import app
from flask import session
from unittest import TestCase
from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class BloglyTestCase(TestCase):
    def test_submit_user(self):
        with app.test_client() as client:

            user = {"first_name": "John", "last_name": "Jacobs"}
            res = client.post("/users/new", data=user, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 404)
            self.assertIn("John Jacobs", html)
