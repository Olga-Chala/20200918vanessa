from django.shortcuts import render
from django.http import HttpResponse
from .models import VanessaModule

def abc_modules_list(request):
    return HttpResponse("...to be continued")

# def find_row(request):
#     # if VanessaModule.objects.all().filter(module_number=0):
#     #     return HttpResponse(VanessaModule.vanessa_question)
#     # b = VanessaModule.objects.filter(module_number=0)
#     b = VanessaModule.objects
#     return HttpResponse(b.vanessa_question)

