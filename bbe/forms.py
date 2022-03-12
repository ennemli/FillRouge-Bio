from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError




client = get_user_model()


class BaseMetaClass:
    model = client

    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "birth_date",
        "address",
    )
    widgets = {
        "birth_date": type("DateInp", (forms.DateInput,), {"input_type": "date"})(),
        "email": type("EmailInp", (forms.EmailInput,), {"input_type": "email"})(),
    }


def customFields(fields, attrs):

    for field in fields.keys():
        fields[field].error_messages = {"required": "Ce champ est requis."}
        attrs.update({"placeholder": f"{fields[field].label}..."})
        fields[field].widget.attrs.update(
                    attrs
            )
        
class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages = {
            "invalid_login": "Veuillez saisir un e-mail et un mot de passe corrects. Noter que les deux champs peuvent être sensibles à la casse."
        }
        customFields(self.fields, {
            "class":"form-control"
        })


class UserRegistrationForm(UserCreationForm):
    class Meta(BaseMetaClass):
        fields = BaseMetaClass.fields + ("password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages = {
            "password_mismatch": "Les deux mots de passe ne correspondaient pas."
        }
        self.fields["password1"].label = "Mot de pass"
        self.fields["password2"].label = "Confirmation mot de passe"
        customFields(
            self.fields,
            {
                "class": "form-control",
            },
        )

    def clean_username(self):
        username = self.cleaned_data["username"]
        if client.objects.filter(username=username).count() > 0:
            raise ValidationError(
                "%(username)s existe déjà.", params={"username": username}
            )
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if client.objects.filter(email=email).count() > 0:
            raise ValidationError("%(email)s existe déjà.", params={"email": email})
        return email

    def save(self, commit=True):
        client = super().save(commit=False)
        client.username = self.clean_username()

        client.email = self.clean_email()

        if commit:
            client.save()
        return client


class ClientChangeForm(UserChangeForm):
    class Meta(BaseMetaClass):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        customFields(
            self.fields, {"class": "form-control", "disable": None, "readonly": None}
        )
