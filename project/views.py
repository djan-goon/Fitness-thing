from django.shortcuts import redirect

def newspage(request):
    return redirect("news:newspage")