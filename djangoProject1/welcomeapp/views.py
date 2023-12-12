from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def home(request):
    return HttpResponse("""<html><body bgcolor=light yellow
    ><center>welcome to eshwarit</h1>
    </center></body></html>""")
