from django.shortcuts import render

# Create your views here.

def index(request):
	#Homepage for PORTFOLIO
	return render(request, 'peronalApplication/index.html')
