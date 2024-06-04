from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def main(request):
    """The home page for learning Log."""
    current_user = request.user  # - Access currently logged-in user
    context = {'current_user': current_user}
    return render(request, 'index.html', context=context)


@login_required
def topics(request):
    """Show all topics."""
    current_user = request.user  # - Access currently logged-in user
    topics = Topic.objects.filter(owner=current_user).order_by('date_added')
    context = {'topics': topics, 'current_user': current_user}
    return render(request, 'topics.html', context=context)


@login_required
def show_topic(request, id):
    """Show a single topic and all its entries."""
    current_user = request.user  # - Access currently logged-in user
    topic = Topic.objects.get(pk=id)
    # Make sure the topic belongs to the current user.
    if topic.owner != current_user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, 'current_user': current_user}
    return render(request, 'topic.html', context=context)


@login_required
def new_topic(request):
    """Add a new topic."""
    current_user = request.user  # - Access currently logged-in user
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = current_user
            new_topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form, 'current_user': current_user}
    return render(request, 'new_topic.html', context=context)


@login_required
def new_entry(request, id):
    """Add a new entry for a particular topic."""
    current_user = request.user  # - Access currently logged-in user
    topic = Topic.objects.get(pk=id)
    if topic.owner != current_user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:show_topic', id)

    context = {'topic': topic, 'form': form, 'current_user': current_user}
    return render(request, 'new_entry.html', context=context)


@login_required
def edit_entry(request, id):
    """Edit an existing entry."""
    current_user = request.user  # - Access currently logged-in user
    entry = Entry.objects.get(pk=id)
    topic = entry.topic
    if topic.owner != current_user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:show_topic', topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form, 'current_user': current_user}
    return render(request, 'edit_entry.html', context=context)


def delete_topic(request, id):
    """delete a specific topic."""
    current_user = request.user
    topic = Topic.objects.get(pk=id)
    if topic.owner != current_user:
        raise Http404
    topic.delete()
    return redirect('learning_logs:topics')


def delete_entry(request, id):
    """delete a specific entry."""
    current_user = request.user
    entry = Entry.objects.get(pk=id)
    topic = entry.topic
    if topic.owner != current_user:
        raise Http404
    entry.delete()
    return redirect('learning_logs:show_topic', topic.id)
