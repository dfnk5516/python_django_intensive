from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# Create your views here.

def index(request):
  return render(request, 'index.html', {'email' : request.session.get('user')})

class RegisterView(FormView):
  template_name = 'register.html'
  form_class = RegisterForm
  success_url = '/'

class LoginView(FormView):
  template_name = 'login.html'
  form_class = LoginForm
  success_url = '/'

  def form_valid(self, form): # 모든 데이터가 정상이면 session 에 저장
    self.request.session['user'] = form.email
    return super().form_valid(form)
