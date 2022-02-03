from django.shortcuts import render
from myapp.models import Student
from django.views.generic.edit import CreateView
from django.urls import reverse

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_create.html'
    fields = ['name','nick_name','email','phone_number']
    def get_success_url(self):
        return reverse('student_create')
        # kwargs={'pk': self.object.pk}