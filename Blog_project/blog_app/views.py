from django.shortcuts import render,redirect
from .models import Blog
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def Home(request):

    if request.user.is_authenticated:
        blog = Blog.objects.all()
        return render(request, 'home.html',{'blog':blog})

    else:
        return redirect('login')

    

def Register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email already exists')
                return redirect('register') 
            else:
                user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    username = username,
                    password = password)
                user.save()        
                return redirect('login')
        
        else:
            messages.info(request,'Password is incorrect ')
            return redirect('register') 

    else:

      return render(request,'register.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')

        else:
            messages.info(request,'username or password is incorrect ')
            return redirect('login') 

    else:
     return render(request, 'login.html')      

def LogOut(request):
    auth.logout(request)
    return redirect('login')
         
def search(request,search):
    eSearch = request.POST['search']
    blog = Blog.objects.filter(blog_heading__icontains = eSearch)
    return render(request, 'home.html',{'blog':blog})

def About(request):
    return render(request,'about.html')    

