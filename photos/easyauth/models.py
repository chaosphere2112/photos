from django.db import models
from django.contrib.auth.models import User
class LoginTokenManager(models.Manager):
	def create_token(self, user):
		return LoginToken(token=generate_token(), user=user)

# Create your models here.
class LoginToken(models.Model):
	token = models.CharField(max_length=32, unique=True)
	user = models.OneToOneField(User, unique=True)
	objects = LoginTokenManager()

import uuid
def generate_token():
	u = uuid.uuid4()
	return u.hex