from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from django.contrib import messages
import json

# Create your views here.
def index(request):
    context = {
        'name' : 'Carlos Daeli'
    }
    return render(request,'index.html', context)

def tambah_user(request):
    return render(request, 'tambah-user.html')

def post_user(request):
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    if Users.objects.filter(userid=userid).exists():
        messages.error(request, 'UserID sudah digunakan')
    else:
        if password == password2:
            tambah_user = Users(
                userid=userid,
                username=username,
                password=password,
            )
            tambah_user.save()
            messages.success(request, "Data User berhasil disimpan")
        else:
            messages.error(request, "Password tidak sama!")
    return redirect(request.META.get('HTTP_REFERER', '/'))

def master_user(request):
    data_user = Users.objects.all().order_by('-userid')
    context = {
        'data_user': data_user
    }
    return render(request, 'master-user.html', context)

def update_user(request, userid): 
    data_user = Users.objects.get(userid=userid)
    context = {
        'data_user': data_user
    }
    return render(request,'update-user.html', context)

def postupdate_user(request):
    userid = request.POST['userid']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']


    user = Users.objects.get(userid=userid)
    if password == password2:
        user.username = username
        user.password = password
        user.save()
        messages.success(request, 'Berhasil Update Data User')
    else:
        messages.error(request, 'Password tidak sama!')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def delete_user(request, userid):
    user = Users.objects.get(userid=userid).delete()
    messages.success(request, 'Berhasil hapus data user')
    return redirect(request.META.get('HTTP_REFERER', '/'))
