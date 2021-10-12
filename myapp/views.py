from django.shortcuts import render, get_object_or_404

from .models import Message, Channel
from .forms import MessageForm


def main_page(request):
  channels = Channel.objects.all()
  context = {'channels': channels}

  return render(request=request, template_name='main_page.html', context=context)

def channel_page(request, name):
  channel = get_object_or_404(klass=Channel, name=name)
  if request.method == 'POST':
    form = MessageForm(data=request.POST)
    if form.is_valid():
        message = form.save(commit=False)
        message.author = request.user
        message.channel = channel
        message.save()

  messages = Message.objects.filter(channel=channel)
  context = {'form': MessageForm(), 'msgs': messages, 'channel': channel}

  return render(request=request, template_name='channel_page.html', context=context)
