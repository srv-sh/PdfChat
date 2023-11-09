from django.shortcuts import render, HttpResponse
from .models import uploadfile
from utils.embedding import makeEmbedding

# Create your views here.
def index(request):
    return render(request, "index.html")

def send_files(request):
    if request.method == "POST":
        name = request.POST.get("filename")
        files = request.FILES.getlist("uploadfiles")
        for file in files:
            uploadfile(f_name = name,files=file).save()

        return HttpResponse("ok")

def makeEmbed(request):
    if request.method == "POST":
        print("ready for the embedding")
        response=  makeEmbedding()
        return HttpResponse(response)