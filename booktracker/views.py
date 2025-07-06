from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from booktracker.models import Book

# Create your views here.

class IndexView(generic.ListView):
    template_name = "booktracker/index.djhtml"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.all()
