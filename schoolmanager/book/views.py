from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render (request, 'book/index.html')

def uploadbook(request):
    if request.method == "POST":
        uploaded_file  = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

    return render(request, 'book/uploadbook.html')