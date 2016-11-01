from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def hello_world(request):
#	return HttpResponse("Hello World!")

from datetime import datetime

def hello_world(request):
	return render(request,'hello_world.html',{
		'current_time':str(datetime.now()),
	})


