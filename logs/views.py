from django.shortcuts import render
from . models import Log

def index(request):
    """The home page for the logs"""
    return render(request, 'logs/index.html')


def logs(request):
    """Index of logs by date"""
    user_logs = Log.objects.order_by('date_added')
    context ={'logs': user_logs}
    return render(request, 'logs/logs.html', context)

