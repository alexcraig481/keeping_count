from django.shortcuts import render
from . models import Log


def index(request):
    """The home page for the logs"""
    return render(request, 'logs/index.html')


def logs(request):
    """Index of logs by date"""
    user_logs = Log.objects.order_by('date_added')
    context = {'logs': user_logs}
    return render(request, 'logs/logs.html', context)


def log_entry(request, log_id):
    """An individual log entry"""
    entry = Log.objects.get(id=log_id)
    context = {'log': entry}
    return render(request, 'logs/log_entry.html', context)

