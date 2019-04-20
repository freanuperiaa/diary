from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from apps.diary.models import Post


class PostModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com',
            password='secretpw', first_name='John',
            last_name='Doe'
        )

        self.post = Post.objects.create(
            title='Test Title',
            content='Loren ipsum dolor sit amet',
            author=self.user,
        )
        self.client.force_login(self.user)

    def test_string_representation(self):
        post = Post(title='Test Title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test Title')
        self.assertEqual(f'{self.post.author}', 'John Doe')
        self.assertEqual(f'{self.post.content}', 'Loren ipsum dolor sit amet')

    def test_post_list_view(self):
        response = self.client.get(reverse('diary:archive'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Loren ipsum dolor sit amet')
        self.assertTemplateUsed(response, 'diary/post_list.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/99999999/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test Title')
        self.assertTemplateUsed(response, 'diary/post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('diary:add'), {
            'title': 'Test Title',
            'author': self.user,
            'content': 'Loren ipsum'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')
        self.assertContains(response, 'Loren ipsum')


class HomePageViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('diary:home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/home.html')


class CreatePostViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('diary:add'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/post_form.html')


class ArchiveViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com',
            password='secretpw', first_name='John',
            last_name='Doe'
        )
        self.client.force_login(self.user)

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/archive/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('diary:archive'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/archive/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/post_list.html')


class DetailViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com',
            password='secretpw', first_name='John',
            last_name='Doe'
        )
        self.client.force_login(self.user)
        self.client.post(reverse('diary:add'), {
            'title': 'Test Title',
            'author': self.user,
            'content': 'Loren ipsum'
        })
        self.client.logout()
        self.user2 = get_user_model().objects.create_user(
            username='testuser2', email='test2@email.com',
            password='secretpw', first_name='John',
            last_name='Doe'
        )
        self.client.force_login(self.user2)
        self.client.post(reverse('diary:add'), {
            'title': 'Test Title',
            'author': self.user,
            'content': 'Loren ipsum'
        })
        self.client.logout()
        self.client.force_login(self.user)

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/post_detail.html')

    def test_cannot_view_others_post(self):
        self.client.logout()
        self.client.force_login(self.user2)
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 404)
