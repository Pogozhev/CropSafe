from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'landing/index.html', locals())

def dashboard(request):
    return render(request, 'app/dashboard.php', locals())