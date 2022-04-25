from django.shortcuts import render, redirect
from . models import Log
from .forms import EntryForm


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


def new_entry(request):
    """Create a new log entry"""
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_log_entry = form.save(commit=True)  # commit = True means save to db
            return redirect('logs:logs')

    context = {'form': form}
    return render(request, 'logs/new_entry.html', context)



