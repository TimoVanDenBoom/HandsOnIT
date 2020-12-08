from django.shortcuts import render, redirect

from .forms import SignupForm
from .models import Business, Freelancer
from django.contrib.auth.models import User

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from .utils import generate_token

# Create your views here.
def signup_view(response, is_business):
	if response.method == "POST":
		form = SignupForm(response.POST)
		if form.is_valid():
			user = form.save()
			user.is_active = False
			user.save()

			if (is_business >= 1):
				b = Business(user=user)
				b.save()
			elif (is_business <= 0):
				f = Freelancer(user=user)
				f.save()

			current_site = get_current_site(response);


			emailBody = render_to_string('confirmationmail/confirmationmail.html',{
				'user':user.username,
				'domain':current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':generate_token.make_token(user)
				}
			)
			email = EmailMessage(
				'HandsOnIT Account Activation',
				emailBody,
				settings.EMAIL_HOST_USER,
				[user.email]
			)
			email.fail_silently = False
			email.send()

			return render(response, "signup/user_created.html", {}) #TODO: redirect to profile page
	else:
		form = SignupForm()
	return render(response, "signup/signup.html", {"form":form})

def activated_view(request, uidb64, token, *args, **kwargs):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk = uid)
	except Exception as identifier:
		user = None
	if user is not None and generate_token.check_token(user, token) and not user.is_active:
		user.is_active = True
		user.save()
		return render(request, "confirmationmail/account_activated.html", {})
	elif user is not None and user.is_active:
		return render(request, 'confirmationmail/token_used.html', status=401)
	return render(request, '/confirmationmail/activate_failed.html', status=401)