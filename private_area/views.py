from django.shortcuts import render
from django.views import View

#  private area


class Home(View):
    def get(self, request):
        return render(request, 'private_area/index.html')
