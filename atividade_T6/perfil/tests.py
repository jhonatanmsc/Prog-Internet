from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from freezegun import freeze_time
from rest_framework import status
from perfil.models import *
from perfil.serializers import *

class NonAuthAcessTest(APIClient):
	def test_non_user(self):
		url = reverse('user-list')

		for i in range(20):
			response = self.client.get(url)
			self.assertEqual(response.status_code, status.HTTP_200_OK)
		
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

		freezer = freeze_time("2013-01-01 16:20:00")
		freezer.start()
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		freezer.stop()


class AuthAcessTest(APITestCase):
	def test_user(self):
		url = reverse('user-list')

		ad = Address.objects.create(street='teste')
		self.profile = User.objects.create(username='usertest', password=make_password('Informatica'), address=ad)

		self.client = APIClient()
		self.client.force_authenticate(user=self.profile)

		for i in range(50):
			response = self.client.get(url)
			self.assertEqual(response.status_code, status.HTTP_200_OK)
		
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

		freezer = freeze_time("2030-01-01 16:20:00")
		freezer.start()
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		freezer.stop()

class TokenTest(APITestCase):
	def test_obtain_token(self):
		url = reverse('api-token')

		ad = Address.objects.create(street='teste')
		self.profile = User.objects.create(username='usertest', password=make_password('Informatica'), address=ad)
		data = {'username': 'usertest', 'password': 'Informatica', 'address': ad.id}

		time = freeze_time("2013-01-01 16:00:00")
		time.start()
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		time.stop()

		time = freeze_time("2013-01-01 16:30:00")
		time.start()
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
		time.stop()

		time = freeze_time("2013-01-01 17:22:00")
		time.start()
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		time.stop()

class UserTest(APITestCase):

	def setUP(self):
		self.url = reverse('user-list')
		self.ad = Address.objects.create(street='teste')
		self.profile = User.objects.create(username='usertest', password=make_password('Informatica'), address=self.ad)
		self.client = APIClient()
		self.client.force_authenticate(user=self.profile)

	def test_readonly(self):
		response = self.client.post(self.url, {'username':'usertest', 'password':'Informatica', 'address':self.ad.id})
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
		

class PostTest(APITestCase):

	def setUP(self):
		self.url = reverse('post-list')
		self.ad = Address.objects.create(street='teste')
		self.profile = User.objects.create(username='usertest2', password=make_password('Informatica'), address=self.ad)
		self.client = APIClient()
		self.client.force_authenticate(user=self.profile)

	def test_create_post(self):
		response = self.client.post(self.url, {'title':'St@april.biz', 'body':'Sincere@april.biz', 'owner':self.profile.username}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		

	def test_delete_post(self):
		response = self.client.post(self.url, {'title':'kk', 'body':'usertest', 'owner':self.profile.username}, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)