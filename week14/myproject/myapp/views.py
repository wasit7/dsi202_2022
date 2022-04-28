from django.shortcuts import render
from myapp.models import Profile, Item
from myapp.forms import ProfileForm
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
import json 

data =[]

class ItemListView(ListView):
    model = Item
    paginate_by = 3
    #queryset=Bike.objects.filter(type='mountain')
    template_name = 'item_list.html'


def add_to_cart(request):
    global data
    pk = request.POST.get("pk", "")
    title = request.POST.get("title", "")
    myitem={
        "pk": pk,
        "tile": title,
        "quantity": 1
        }
    data += [myitem,]
    dictionary = {"data": data}
    json_object = json.dumps(dictionary, indent = 4)
    print(json_object)
    response = redirect('home')
    response.set_cookie('cart', json_object)
    return response

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