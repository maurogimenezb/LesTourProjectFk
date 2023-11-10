from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lesTourWeb.views import home, signUp, reservation, signOut, signIn, Hoteles, Personal, Usuarios

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signUp)

    def test_reservation_url_resolves(self):
        url = reverse('reservation')
        self.assertEqual(resolve(url).func, reservation)

    def test_signout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, signOut)

    def test_signin_url_resolves(self):
        url = reverse('signin')
        self.assertEqual(resolve(url).func, signIn)

    def test_hoteles_url_resolves(self):
        url = reverse('hoteles')
        self.assertEqual(resolve(url).func, Hoteles)

    def test_personal_url_resolves(self):
        url = reverse('personal')
        self.assertEqual(resolve(url).func, Personal)

    def test_usuarios_url_resolves(self):
        url = reverse('usuarios')
        self.assertEqual(resolve(url).func, Usuarios)

class TestViews(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario

    def test_reservation_view(self):
        response = self.client.get(reverse('reservation'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario

    def test_signout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario

    def test_signin_view(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario

    def test_hoteles_view(self):
        response = self.client.get(reverse('hoteles'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario

    def test_personal_view(self):
        response = self.client.get(reverse('personal'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario

    def test_usuarios_view(self):
        response = self.client.get(reverse('usuarios'))
        self.assertEqual(response.status_code, 200)
        # Añade más aserciones según sea necesario
