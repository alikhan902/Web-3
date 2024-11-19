from django.http import HttpResponse

def ice_cream_list(request):
    return HttpResponse("Список мороженого")

def ice_cream_detail(request, pk):
    return HttpResponse(f"Детали мороженого с ID {pk}")