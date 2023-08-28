from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from testapp.models import Employee,EmployeeProfileInfo
from testapp.forms import PromiseForm, UserForm,EmployeeProfileInfoForm
from django.shortcuts import render


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
class BookList(ListView):
    model = Employee
    

class BookView(DetailView):
    model = Employee

class BookCreate(CreateView):
    model = Employee
    form_class = PromiseForm
    success_url = reverse_lazy('testapp:employee_list')

class BookUpdate(UpdateView):
    model = Employee
    fields = ['name','emailid','department','doj']
    success_url = reverse_lazy('testapp:employee_list')

class BookDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('testapp:employee_list')

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')


def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = EmployeeProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'department' in request.POST:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.department = request.POST['department']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = EmployeeProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'testapp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))
@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return render(request,'testapp/employee_list.html',{})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'testapp/login.html', {})


class EmployeeCreate(CreateView):
    model = EmployeeProfileInfo
    form_class = EmployeeProfileInfoForm
    success_url = reverse_lazy('employee_list')

class EmployeeList(ListView):
    model = EmployeeProfileInfo
    

class EmployeeDelete(DeleteView):
    model = EmployeeProfileInfo
    success_url = reverse_lazy('employee_list')


class EmployeeUpdate(UpdateView):
    model = EmployeeProfileInfo
    fields = ['username','first_name','last_name','email','department','doj']
    success_url = reverse_lazy('employee_list')


class EmployeeView(DetailView):
    model = EmployeeProfileInfo
