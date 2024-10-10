from django.http import HttpResponse
from django.shortcuts import render, redirect
from items.models import recipe2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login

def home_recipe(request):
    if request.method == 'POST':
        #data = request.POST
        rname =  request.POST.get('foodName')
        rdes = request.POST.get('foodDescription')
        rprice = request.POST.get('foodPrice')
        my_userr = recipe2(rname = rname ,rdes = rdes,rprice= rprice)
        my_userr.save()
        return redirect('home')
    return render(request,'homee.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        my_user = User.objects.create_user(username,email,password)
        
        my_user.save()
        return redirect('login')
    
    return render(request,'registration.html')
     
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')   
        else:
            return HttpResponse("INCORRECT PASSWORD, TRY AGAIN")
        
    return render(request,'login.html')      


def delete_food(request, food_id):
    recipe2.objects.get(id=food_id).delete()
    return redirect('show')

def update_food(request, food_id):
    food = recipe2.objects.get(id=food_id)
    if request.method == 'POST':
        food.name = request.POST['rname']
        food.description = request.POST['rdes']
        food.price = request.POST['rprice']
        food.save()
        return redirect('show')
    return render(request, 'update_food.html', {'food': food})

def show(request):
    
    data = recipe2.objects.all()
    return render(request,'showfood.html',{'data':data})