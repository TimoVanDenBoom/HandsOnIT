from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def account_view(request):
	if(request.user.is_authenticated):
		user = User.objects.get(username=request.user)
		try:
			business = user.business
			freelancer = None
		except Exception as e:
			freelancer = user.freelancer
			business = None
		
		return render(request, "account.html", {'user':user, 'freelancer':freelancer, 'business':business})

	else:
		return redirect('/login')