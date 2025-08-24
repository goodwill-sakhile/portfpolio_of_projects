from django.shortcuts import render

# Create your views here.
def home(request):
    #image_url = '/media/images/GS.png'
    return render(request, 'portfolio/home.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def project_detail(request, pk):
    return render(request, 'portfolio/project_detail.html', {'pk':pk})
