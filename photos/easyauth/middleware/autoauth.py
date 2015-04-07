from urlparse import parse_qs
from django.http import HttpResponse
from easyauth.models import LoginToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class AutoAuthMiddleware(object):
	def process_request(self, request):
		if request.user.is_authenticated():
			return
		query = request.META["QUERY_STRING"]
		query = parse_qs(query, True)
		possible_keys = []

		for key in query:
			if len(key) == 32:
				if query[key] == [""]:
					possible_keys.append(key)

		if len(possible_keys) > 1 :
			# this is probably somebody probing... block ip / ratelimit / whatever
			return bad_login()
		if len(possible_keys) == 0:
			# somebody who doesn't know what's up; nothing to do besides give them a 503
			return bad_login()
		
		key = possible_keys[0]
		u = authenticate(token=key)
		if u is None:
			# key was invalid
			return bad_login()
		login(request, u)

def bad_login():
	resp = HttpResponse("Sorry, too much load on server.")
	resp.status_code = 503
	return resp

class AutoAuthBackend(object):
	def authenticate(self, token=None):
		try:
			t = LoginToken.objects.get(token=token)
			u = t.user
			return u
		except LoginToken.DoesNotExist:
			return None
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None