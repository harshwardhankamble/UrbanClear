from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
#view for requesting to register handle using post method
def register(request):

	#check requested method is POST
	if request.method == 'POST':

		#extract the username , password, firstname, lastname, password for POST method
		first_name = request.POST['firstname'];
		last_name = request.POST['lastname'];
		user_name = request.POST['username'];
		password1 = request.POST['password1'];
		password2 = request.POST['password2'];
		email = request.POST['email'];


		#check whether password is matched along with confirm password
		if password1 == password2:

			# filter the database to check that the username is alredy used or not
			if User.objects.filter(username = user_name).exists():

				# if username is already used then send the appropriate message to register page and render to register page
				messages.info(request,'Username already taken')
				return render(request,'register.html');

			# filter the database to check that the email is alredy used or not
			elif User.objects.filter(email = email).exists():

				# if email is already used then send the appropriate message to register page and render to register page
				messages.info(request,'Email already taken')
				return render(request,'register.html');

			#else creaate the user using creat_suer command by passing appropriate field
			else:
				user = User.objects.create_user(username = user_name,first_name = first_name,last_name = last_name,email = email,password = password1)

				#save the registered user to database and redirect to main page
				user.save()
				return redirect('login')
		#if password is not matched generate the message and render to register page again
		else:
			messages.info(request,'Password is not matched')
			return render(request,'register.html');
	else:
		return render(request,'register.html');

	return render(request,'register.html');

#views for login
def login(request):

	if request.method == 'POST':

		#extract the username and password from login page 
		user_name = request.POST['username'];
		password = request.POST['password'];

		#authenticate the user 
		user =auth.authenticate(username = user_name ,password = password);

		#if user is authenticated then login the user and redirect to main page
		if user is not None:
			auth.login(request,user);
			return redirect('/')
		#else again redirect to login page
		else:
			return redirect('login')
	return render(request,'login.html');

#views for logout
def logout(request):

	#logout the authenticated user and redirect to home page
	auth.logout(request)
	return redirect('/')