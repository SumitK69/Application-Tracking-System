from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password!=confirm_password:
            return HttpResponse("Your password does not match")
        else:
            my_user=User.objects.create_user(email,password)
            my_user.save()
        return redirect('login')
        # print(email,password,confirm_password)
    return render (request,'htmltemplate.html')

def LoginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("details incorrect")
    return render (request,'htmltemplate.html')




# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login

# def HomePage(request):
#     return render(request, 'home.html')

# def handle_forms(request):
#     if request.method == 'POST':
#         form_type = request.POST.get('form_type')  # Check which form is submitted

#         if form_type == 'signup':
#             # Handle signup form
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             confirm_password = request.POST.get('confirm_password')

#             if password != confirm_password:
#                 return HttpResponse("Your password and confirm password are not the same")
#             try:
#                 my_user = User.objects.create_user(username=email, password=password)
#                 my_user.save()
#                 return redirect('login')  # Redirect to login page
#             except Exception as e:
#                 return HttpResponse(f"Error: {e}")

#         elif form_type == 'login':
#             # Handle login form
#             email = request.POST.get('email')
#             password = request.POST.get('password')

#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to home page
#             else:
#                 return HttpResponse("Invalid login credentials")

#     return render(request, 'htmltemplate.html')

