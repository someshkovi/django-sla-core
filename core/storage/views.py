from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404, JsonResponse
from storage.models import PrimaryStroageTraps, PrimaryStorageModuleStatus, StorageUtilSummary, StorageTapePolicySummary
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import date


@login_required(login_url='/login/')
def trap_list(request):
    # latest_sla_list = SlaAchievedOverview.objects.order_by('-date').filter(slaPoint='1.1')[:7]
    storage_trap_list = PrimaryStroageTraps.objects.order_by('-date').filter(nonCritical=0)

    context = {'storage_trap_list': storage_trap_list}
    return render(request, 'storage/index.html', context)

@staff_member_required(login_url='/login/')
def index(request):
    today = date.today()
    # latest_sla_list = SlaAchievedOverview.objects.order_by('-date').filter(slaPoint='1.1')[:7]
    storage_status_list = PrimaryStorageModuleStatus.objects.filter(dateToday=today)

    context = {'storage_status_list': storage_status_list,
                'today':today,
                }
    return render(request, 'storage/status.html', context)


@login_required()
def StorageSummaryView(request):
    today = date.today()

    StorageTapePolicySummaryList = StorageTapePolicySummary.objects.all()
    StorageUtilSummaryList = StorageUtilSummary.objects.all()
    storage_status_list = PrimaryStorageModuleStatus.objects.filter(dateToday=today)
    storage_trap_list = PrimaryStroageTraps.objects.order_by('-date').filter(nonCritical=0)

    context = {
        'StorageTapePolicySummaryList':StorageTapePolicySummaryList,
        'StorageUtilSummaryList':StorageUtilSummaryList,
        'storage_status_list':storage_status_list,
        'storage_trap_list':storage_trap_list,
    }
    return render(request, 'storage/summary.html', context)
