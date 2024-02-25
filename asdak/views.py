from django.shortcuts import render

def main(request):
    return render(request,'index.html')

def signPage(request):
    return render(request,'signin.html')