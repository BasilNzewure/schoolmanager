from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.template import context

# Create your views here.

def index(request):
    return render (request, 'book/index.html')

def uploadbook(request):
    context = {}
    if request.method == "POST":
        uploaded_file  = request.FILES['document']
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        #url = fs.url(name)
        context['url'] = fs.url(name)

    return render(request, 'book/uploadbook.html', context)