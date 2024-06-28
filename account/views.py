from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View,TemplateView,FormView,CreateView
from .forms import LoginForm,RegisterForm
from django.http import HttpResponse
from django.contrib import messages

class HomeView(TemplateView):
    template_name='index.html'

class LoginView(FormView):
    template_name='login.html'
    form_class= LoginForm
    def post(self,request,*args,**kw):
        form_dat = LoginForm(request.POST)
        if form_dat.is_valid():
            usr = form_dat.cleaned_data.get('username')
            pwd = form_dat.cleaned_data.get('password')
            usr_obj = authenticate(request,username=usr,password=pwd)
            if usr_obj:
                login(request,usr_obj)
                messages.success(request,'Login Successful!!')
                return redirect('index')
            else:
                messages.error(request,'Invalid Credentials!!')
                return redirect("login")
        
        messages.error(request,'Invalid Input!!')
        return render(request,"login.html",{"form":form_dat})
    
class RegisterView(CreateView):
    template_name='Register.html'
    form_class=RegisterForm
    success_url = "login"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request,'Registration Successfull!!')
        return super().form_valid(form)
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.error(self.request,'Registration Failed!!')
        return super().form_invalid(form)
    
def lgout(request):
    logout(request)
    messages.success(request,'Logged out Successfully')
    return redirect('login')