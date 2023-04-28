from django.urls import path
from django.contrib.auth import views as auth_views
from modules.accounts import views

urlpatterns = [
    path('signin/', views.SignIn.as_view(), name='SignIn'),
    path('signout/', views.SignOut.as_view(), name='SignOut'),
    path('password-reset/', views.PasswordReset.as_view(), name='PasswordReset'),
    path('password-reset/done/', views.PasswordResetDone.as_view(),
         name='PasswordResetDone'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(),
         name='PasswordResetConfirm'),
    path('password-reset-done/', views.PasswordResetComplete.as_view(),
         name='PasswordResetComplete'),
]
