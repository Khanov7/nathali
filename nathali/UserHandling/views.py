from django.shortcuts import render
from django.views import generic, View
# Create your views here.
from .forms import UserSignUpForm

class ResgisterUserView(View):

    def get(self,request):
        return render(request, 'Sign Up.html', {'form': UserSignUpForm()})

