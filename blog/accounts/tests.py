from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class HomePagetests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_templates(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.asserttemplateUsed (response, 'home.html')

    class SignupPageTests(TestCase):

        username = 'newuser'
        email = 'newuser@email.com'

        def test_signup_page_status_code(self):
            response = self.client.get('/user/signup')
            self.assertEqual(response.status_code, 200)

        def test_view_url_by_name(self):
            response = self.client.get(reverse('signup'))
            self.assertEqual(response.status_code, 200)

        def test_view_uses_correct_template(self):
            response = self.client.get(reverse('signup'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'signup.html')

        def test_signup_form(self):
            new_user = get_user_model().objects.create_user(
                self.username, self.email
            )
            self.assertEqual(get_user_model().objects.all().count(), 1)
            self.assertEqual(get_user_model().objects.all()[0].username,
            self.username)

            self.assertEqual(get_user_model().objects.all()[0].email, self.email)

