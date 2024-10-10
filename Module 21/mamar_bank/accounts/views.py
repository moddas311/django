from django.shortcuts import render
from django.views.generic import FormView
from .forms import userRegistrationForm, userUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect

# Create your views here.
class userRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = userRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid call hobe jodi sob sthik thake 


class userLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class userLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
    
class userBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = userUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = userUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})

    