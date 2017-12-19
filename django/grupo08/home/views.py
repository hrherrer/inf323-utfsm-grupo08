from django.shortcuts import render
from django.views import View
import socket


# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'home/home.html', {
            'hostname': socket.gethostname(),
        })
