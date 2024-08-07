# # forms.py
# from django import forms
# from .models import Contact

# class UserRegistrationForm(forms.ModelForm):
#     confirm= forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Contact
#         fields = ['name', 'address', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm = cleaned_data.get("confirm")

#         if password and confirm and password != confirm:
#             self.add_error('confirm', "Password and confirm password do not match.")
#             # raise forms.ValidationError("password does not match")