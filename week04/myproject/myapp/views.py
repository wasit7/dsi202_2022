from django.shortcuts import render
from myapp.models import Student
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_create.html'
    fields = ['name','nick_name','email','phone_number']
    def get_success_url(self):
        return reverse('student_list')
        # kwargs={'pk': self.object.pk}

class StudentListView(ListView):
    model = Student
    paginate_by = 5
    #queryset=Student.objects.filter(type='mountain')
    template_name = 'student_list.html'