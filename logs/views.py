from django.shortcuts import render, redirect
from . models import Log
from .forms import EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """The home page for the logs"""
    return render(request, 'logs/index.html')


@login_required
def logs(request):
    """Index of logs by date"""
    user_logs = Log.objects.filter(owner=request.user).order_by('date_added')
    context = {'logs': user_logs}
    return render(request, 'logs/logs.html', context)


@login_required
def log_entry(request, log_id):
    """An individual log entry"""
    entry = Log.objects.get(id=log_id)
    if entry.owner != request.user:
        raise Http404
    context = {'log': entry}
    return render(request, 'logs/log_entry.html', context)


@login_required
def new_entry(request):
    """Create a new log entry"""
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_log_entry = form.save(commit=False)
            new_log_entry.owner = request.user
            new_log_entry.save()
            return redirect('logs:logs')

    context = {'form': form}
    return render(request, 'logs/new_entry.html', context)


@login_required
def edit_entry(request, log_id):
    """Edit an existing log entry"""
    entry = Log.objects.get(id=log_id)
    if entry.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Fill new form with existing content to edit
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs:logs')

    context = {'log': entry, 'form': form}
    return render(request, 'logs/edit_entry.html', context)

