from django.http import HttpResponse

def home(request):
    return HttpResponse("To jest strona główna.")

def main(request):
    return HttpResponse("To jest strona main.")