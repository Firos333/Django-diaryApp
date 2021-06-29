from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'entries' : entries}

    return render(request, 'entries/index.html', context)


@login_required
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'entries/add.html', context)

@login_required
def viewdiary(request,id):
    entries = Entry.objects.filter(id =id)
    context = {'entries' : entries}

    return render(request, 'entries/viewdiary.html', context)


def logg(request):
    
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'Invalid User account!')
            return redirect('')
    else:
        return render(request,'entries/logg.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def registerr(request):

    if request.method == 'POST':
        username =request.POST['username']
        email =request.POST['email']
        password1 =request.POST['password1']
        password2 =request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken!')
                return redirect('registerr')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken!')
                return redirect('registerr')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'Password not matching!')
            return redirect('registerr','username',)
        return redirect('/')
    else:
        return render(request,'entries/registerr.html')
