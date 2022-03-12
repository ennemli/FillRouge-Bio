from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from bbe.forms import UserAuthenticationForm,UserRegistrationForm,ClientChangeForm
from django.contrib.auth import get_user_model
# Create your views here.
class Index(generic.TemplateView):
    template_name="index.html"

class Register(views.FormView):
    template_name="register.html"
    form_class=UserRegistrationForm
    success_url=reverse_lazy("bbe:login")
    def dispatch(self, request):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('bbe:profile'))
        return super().dispatch(request)
    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
        
class Login(views.LoginView):
    template_name="login.html"
    redirect_authenticated_user=True
    authentication_form=UserAuthenticationForm
    redirect_field_name=''
    next_page=reverse_lazy('bbe:profile')

class Logout(views.LogoutView):
    next_page=reverse_lazy("bbe:index")

class Profile(LoginRequiredMixin,generic.UpdateView):
    model=get_user_model()
    template_name='profile.html'
    success_url=reverse_lazy("bbe:profile")
    form_class=ClientChangeForm
    def get_object(self):
        return self.request.user
class UpdateProfile(LoginRequiredMixin,generic.UpdateView):
    model=get_user_model()
    redirect_field_name=''
    login_url=reverse_lazy('bbe:login')
    success_url=reverse_lazy("bbe:profile")
