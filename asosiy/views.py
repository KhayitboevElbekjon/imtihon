from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views import View
class HomeView(View):
    def get(self,request):
        ll=request.GET.get('login')
        pp = request.GET.get('parol')
        user=authenticate(request,username=ll,password=pp)
        if user:
            login(request,user)
            return redirect('blog/')
        return render(request,'login.html')

class BlogView(View):
    def post(self,request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                sarlavha=request.POST.get('sarlavha'),
                sana=request.POST.get('sana'),
                mavzu=request.POST.get('mavzu'),
                matn=request.POST.get('matn'),
                muallif=request.user
            )
            return redirect('/blog/')
        return redirect('/')

    def get(self,request):
        data={
            'data':Maqola.objects.all(),
            'muallif':Muallif.objects.all()
        }
        return render(request,'blog.html',data)


def register_view(request):
    username=request.POST.get('login')
    password=request.POST.get('parol')
    passwordN=request.POST.get('parol2')
    if request.method=='POST' and passwordN==password:
        User.objects.create_user(
            username=username,
            password=passwordN
        )
        return redirect('/')
    return render(request,'register.html')

class MaqolaView(View):
    def get(self,request,son):
        if request.user.is_authenticated:
            data={
            'data':Maqola.objects.get(id=son)
            }
            return render(request,'maqola.html',data)
        return redirect('/')
def logautview(request):
    logout(request)
    return redirect('/')