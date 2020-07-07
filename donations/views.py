from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class LandingPageView(View):
    def get(self, request):
        return render(self.request, 'index.html')
    def post(self):
        pass

class AddDonationView(View):
    def get(self, request):
        return render(self.request, 'form.html')
    def post(self):
        pass

class LoginView(View):
    def get(self, request):
        return render(self.request, 'login.html')
    def post(self):
        pass

class RegisterView(View):
    def get(self, request):
        return render(self.request, 'register.html')
    def post(self):
        pass