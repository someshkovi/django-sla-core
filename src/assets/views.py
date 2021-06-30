from django.shortcuts import render, get_object_or_404

from assets.models import NetworkDevice

def index(request):
    asset_list = NetworkDevice.objects.order_by('name')
    context = {
        'asset_list':asset_list,
    }
    return render(request, 'assets/index.html', context)

def detail(request, id):
    asset = get_object_or_404(NetworkDevice,pk=id)
    return render(request, 'assets/detail.html', {'asset': asset})