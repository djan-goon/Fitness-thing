from django.shortcuts import render, redirect
from .forms import MembershipForm

def membership_page(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership:membership_verification')
    else:
        form = MembershipForm()

    return render(request, 'membership/membership_page.html', {'form': form})


def membership_verification(request):
    return render(request, 'membership/membership_verification.html')
