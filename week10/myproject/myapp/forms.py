from django.forms import ModelForm
from myapp.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'address', 'postcode','mobile','email']

    def save(self, user):
        Profile.objects.create(
            name = self.cleaned_data["name"],
            address = self.cleaned_data["address"],
            postcode = self.cleaned_data["postcode"],
            mobile = self.cleaned_data["mobile"],
            email = self.cleaned_data["email"],
            user = user
        )
