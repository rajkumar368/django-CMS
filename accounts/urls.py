from django.contrib import admin
from django.urls import path,include
from accounts.views import Signup_create_view,HomePageView,ProfileUpdateView,ProfileView
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView,PasswordResetCompleteView,LogoutView
urlpatterns = [
    path('',HomePageView.as_view(),name= 'home'),
    path('login/',LoginView.as_view(template_name= 'account/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name= 'account/logout.html'), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('edit-profile/',ProfileUpdateView.as_view(),name= 'edit-profile'),
    path('signup', Signup_create_view.as_view(), name= 'signup'),
    path('password-reset/',PasswordResetView.as_view(template_name='account/password_reset_form.html',email_template_name='account/password_reset_email.html'),name= 'password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view( template_name= 'account/password_reset_done.html'),name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name= 'account/password_confirm.html'),name= 'password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name= 'account/password_reset_complete.html'),name= 'password_reset_complete'),
    path('password-change/',PasswordChangeView.as_view(template_name= 'account/password_change.html'),name= 'password_change'),
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name= 'account/password_change_done.html'),name= 'password_change_done'),
]