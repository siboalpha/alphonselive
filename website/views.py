from django.shortcuts import redirect, render
from .forms import ContactForm
# Create your views here.
def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'form': form}
    return render(request, 'website/index.html', context)

def offer(request):
    return render(request, 'website/offer.html')

def thankYou(request):
    return render(request, 'website/thank-you.html')
