from django.shortcuts import render
from django.views import View
from .models import MetaData
from core.factory import get_ip
# Create your views here.

class HomeView(View):

    template = 'index.html'

    def get(self, request):
        print(request.META)
        args = request.META
        ip = get_ip(args)
        data = {
                "server_name": args.get('SERVER_NAME'),
                "http_host":args.get('HTTP_HOST'),
                "remote_addr":ip,
                "user":args.get('USERNAME'),
                }
        obj = MetaData.objects.create(**data)
        obj.save()
        return render(request, self.template)
