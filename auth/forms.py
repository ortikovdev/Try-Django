from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username",
            "id": "exampleFormControlInput1",
            "name": "username"
        })
        self.fields['password1'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password",
            "id": "inputPassword1",
            "name": "password1"
        })
        self.fields['password2'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirm Password",
            "id": "inputPassword2",
            "name": "password2"
        })


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username",
            "id": "exampleFormControlInput1",
            "name": "username"
        })
        self.fields['password'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password",
            "id": "inputPassword",
            "name": "password"
        })