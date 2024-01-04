from django.shortcuts import render
from django.views.generic import TemplateView


async def index(request):
    return render(request, 'base.html')



class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'