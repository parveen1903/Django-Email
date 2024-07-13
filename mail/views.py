from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

def welcome(request):
    return render(request, 'welcome.html')
def homepage(request):
    return render(request, 'homepage.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            return redirect("homepage")  # Redirect to homepage after successful registration
        else:
            # If form is invalid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				return redirect("homepage")
			
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    return render(request, 'logout.html')
	



