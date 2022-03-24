from django.shortcuts import render
from myapp.forms import ProfileForm

def profile(request):
    form = ProfileForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(user=request.user)
    context = {
        'form':form,
        'user':request.user
        }
    return render(request, 'profile.html', context)
