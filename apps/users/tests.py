from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')


class ProfileViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com',
            password='secretpw', first_name='John',
            last_name='Doe'
        )

        self.user2 = get_user_model().objects.create_user(
            username='testuser2', email='test2@email.com',
            password='secretpw', first_name='Maria',
            last_name='Doe'
        )

    def test_view_url_exists_at_proper_location(self):
        self.client.force_login(self.user)
        response = self.client.get('/users/profile/1/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.force_login(self.user)
        response = self.client.get('/users/profile/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/customuser_detail.html')

    def test_user_cannot_view_others_profile(self):
        self.client.force_login(self.user)
        response = self.client.get('/users/profile/1/', follow=True)
        response2 = self.client.get('/users/profile/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 404)
