from django.shortcuts import render
from django.views import View


#  public area


class Home(View):

    def get(self, request):
        return render(request, 'public_area/index.html')
