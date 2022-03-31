from django.shortcuts import render
from myapp.models import Profile
from myapp.forms import ProfileForm
from django.shortcuts import get_object_or_404, redirect

def home(request):
    return render(request, 'home.html')

def profile(request): 
    instance = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        context = {
            'form':form,
            'user':request.user
            }
        return render(request, 'profile.html', context) 