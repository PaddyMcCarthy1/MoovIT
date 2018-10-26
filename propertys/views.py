from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Property
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


# Create your views here.


class PropertyListView(ListView):
    model = Property
    template_name = 'propertys/property_list'


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'propertys/property_detail.html'


class PropertyUpdateView(UpdateView):
    model = Property
    fields = [
        'title',
        'address1',
        'address2',
        'address3',
        'city',
        'postcode',
        'eircode',
        'county',
        'country',
        'description',
        'key1',
        'key2',
        'key3',
        'key4',
        'key5',
        'video',
        'mapping',
        'floorplan',
        'price'
    ]
    template_name = 'propertys/property_update.html'
    success_url = reverse_lazy('property_list')


class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'propertys/property_delete.html'
    success_url = reverse_lazy('property_list')


class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    fields = [
        'title',
        'address',
        'description',
        'mapping',
        'floorplan',
        'price'
    ]
    template_name = 'propertys/property_create.html'
    success_url = reverse_lazy('property_list')


