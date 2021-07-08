from django.shortcuts import render

def index_view(request):
    return render(request, 'assets/network-devices.html')


import datetime
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from assets.models import NetworkDevice

# def index(request):
#     asset_list = NetworkDevice.objects.order_by('name')
#     context = {
#         'asset_list':asset_list,
#     }
#     return render(request, 'assets/index.html', context)

# def detail(request, id):
#     asset = get_object_or_404(NetworkDevice,pk=id)
#     return render(request, 'assets/detail.html', {'asset': asset})

class IndexView(generic.ListView):
    template_name = 'assets/network-devices.html'
    context_object_name = 'listOfNetworkDevices'
    model = NetworkDevice

    # def get_queryset(self):
    #     # return NetworkDevice.objects.order_by('-date_added')[:10]
    #     return NetworkDevice.objects.filter(
    #         date_added__lte=timezone.now()
    #     ).order_by('-date_added')[:10]

class DetailView(generic.DetailView):
    model = NetworkDevice
    template_name = 'assets/detail.html'