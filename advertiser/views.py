from django.shortcuts import render

def advertiser_dashboard(request):
    return render(request, 'advertiser/dashboard.html')
