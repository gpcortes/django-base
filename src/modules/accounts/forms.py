from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, HTML, Div
from crispy_forms.bootstrap import FormActions
from django.contrib import messages
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _


class AccountAuthenticationForm(AuthenticationForm):

    remember_me = forms.BooleanField(required=False, label=_('Remenber me'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Div(
                HTML('<h3>' + _('Sign in') + '</h3>'),
                css_class='card-header'
            ),
            Div(
                HTML('<p>' + _('Use the username registered to your account.') + '</p>'),
                Fieldset(
                    None,
                    'username',
                    'password',
                    'remember_me',
                ),
                FormActions(
                    Submit(
                        'login', _('Sign in'),
                    ),
                ),
                Div(
                    HTML(
                        '<p>' + _('Forgot password?') + ' <a href="{% url "PasswordReset" %}">' + _('Click here') + '</a></p>'),
                    css_class='d-flex justify-content-center'
                ),
                css_class='card-body'
            )
        )

    def get_invalid_login_error(self):
        messages.error(
            self.request, _(
                "Please enter a correct username and password. Note that both fields may be case-sensitive."
            ))
        return ValidationError([])


class AccountPasswordReset(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Div(
                HTML('<h3>'+ _('Recover your password') + '</h3>'), 
                css_class='card-header'
            ),
            Div(
                HTML('<p>' + _('Enter the email registered to your account to retrieve your password.') + '</p>'),
                Fieldset(
                    '',
                    'email',
                ),
                FormActions(
                    Submit(
                        'reset', _('Reset'),
                    ),
                ),
                css_class='card-body'
            )
        )


class AccountSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.layout = Layout(
        )
        self.helper.layout = Layout(
            Div(
                HTML('<h3>' + _('Create a new password') + '</h3>'),
                css_class='card-header'
            ),
            Div(
                HTML(
                    '<p>' + _('Follow the instructions to create a new password.') + '</p>'),
                Fieldset(
                    None,
                    'new_password1',
                    'new_password2',
                ),
                FormActions(
                    Submit(
                        'change', _('Change'),
                    ),
                ),
                css_class='card-body'
            )
        )
