from django.shortcuts import render, redirect
from .forms import NewRegisterForm
from .models import Profile
from django.http import HttpResponse

# Create your views here.


def register(request): 

    if request.method == "POST":
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('article:index')  
    else:
        form = NewRegisterForm()

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context) 

def profile(request):
    
    return render(request, 'users/profile.html') 



# def edit_profile(request):
#     try:
#         have_profile = request.user.profile
#         profile = request.user.profile 
#         if request.method == 'POST':
#             profile.first_name = request.POST.get('first_name')
#             profile.last_name = request.POST.get('last_name')
#             profile.contact_number = request.POST.get('contact_number')
#             profile.bio = request.POST.get('bio')
#             if request.FILES.get('image'):
#                 profile.image = request.FILES['upload']
#             profile.save() 
#             return redirect('users:profile')
#         return render(request, 'users/edit_profile.html', {'profile': profile})    
#     except:
#         have_profile = False
#         if request.method == 'POST':
#             user = request.user
#             first_name = request.POST.get('first_name')
#             last_name = request.POST.get('last_name')
#             contact_number = request.POST.get('contact_number')
#             bio = request.POST.get('bio')
#             image = request.FILES['upload'] 
#             profile = Profile(user = user, first_name= first_name, last_name=  last_name, contact_number= contact_number, bio= bio, image= image )
#             profile.save() 
#             return redirect('users:profile')  
#         return render(request, 'users/edit_profile.html') 


def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        if profile:  # User has a profile
            profile.first_name = request.POST.get('first_name')
            profile.last_name = request.POST.get('last_name')
            profile.contact_number = request.POST.get('contact_number')
            profile.bio = request.POST.get('bio')
            if request.FILES.get('image'):
                profile.image = request.FILES['image']
            profile.save()
        else:  # User doesn't have a profile
            user = request.user
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            contact_number = request.POST.get('contact_number')
            bio = request.POST.get('bio')
            image = request.FILES.get('image')
            profile = Profile(user=user, first_name=first_name, last_name=last_name, contact_number=contact_number, bio=bio, image=image)
            profile.save()
        
        return redirect('users:profile')

    return render(request, 'users/edit_profile.html', {'profile': profile})




       
