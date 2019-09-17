from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

#def handle_uploaded_file(f):
#    return HttpResponse("")

def home(request):
	template = loader.get_template('logs/index.html')
	context = {}

	if request.method == 'POST':
		#handle_uploaded_file(request.FILES['file'])
		path = request.POST.get('path',None)
		return HttpResponse("<h1>"+path+"</h1>")
	else:
		return HttpResponse(template.render({},request))