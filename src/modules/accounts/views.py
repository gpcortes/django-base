from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from modules.accounts import forms
from django.urls import reverse_lazy


class SignIn(LoginView):
    redirect_authenticated_user = True
    form_class = forms.AccountAuthenticationForm
    template_name = "accounts/credentials.html"

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True \

        return super(SignIn, self).form_valid(form)  # type: ignore


class SignOut(LogoutView):
    template_name = "accounts/logged_out.html"


class PasswordReset(PasswordResetView):
    email_template_name = "accounts/password_reset_email.html"
    form_class = forms.AccountPasswordReset
    subject_template_name = "accounts/password_reset_subject.txt"
    success_url = reverse_lazy("PasswordResetDone")
    template_name = "accounts/credentials.html"


class PasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    form_class = forms.AccountSetPasswordForm
    reset_url_token = "set-password"
    success_url = reverse_lazy("PasswordResetComplete")
    template_name = "accounts/credentials.html"


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
