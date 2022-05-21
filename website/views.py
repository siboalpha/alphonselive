from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def offer(request):
    return render(request, 'website/offer.html')
