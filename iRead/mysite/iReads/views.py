from django.shortcuts import render, HttpResponse, redirect
from iReads.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

BUTTONS='<a href="loginUser" class="btn">Login</a><a href="signupUser" class="btn">Signup</a>'

def index(request):
    global BUTTONS
    if request.user.is_authenticated:
        BUTTONS='<a href="logoutUser" class="btn">Logout</a>'+f'<a class="btn">{request.user.username}</a>'
    content = {
        "buttons": BUTTONS}
    return render(request, 'index.html', content)


def stories(request):
    global BUTTONS
    if request.user.is_authenticated:
        BUTTONS='<a href="logoutUser" class="btn">Logout</a>'+f'<a class="btn">{request.user.username}</a>'
    cat = {
        "cat": StoriesCat.objects.all(),
        "buttons": BUTTONS
    }
    return render(request, 'stories.html', cat)


def discussion(request):
    global BUTTONS
    if request.user.is_authenticated:
        BUTTONS='<a href="logoutUser" class="btn">Logout</a>'+f'<a class="btn">{request.user.username}</a>'

    cat = {
        "cat": DiscussionCat.objects.all(),
        "buttons": BUTTONS
    }
    return render(request, 'discussion.html', cat)


def threadlist(request):
    cat = request.GET.get('cat')
    type = int(request.GET.get('type'))
    if(cat == "story"):
        stories = StoriesThreads.objects.filter(type=type)
        if(len(stories) != 0):
            content = {"content": stories, 
                        "typeof": "story",
                       "url": '/thread?cat={{typeof}}&&id={{con.id}}', 
                       "buttons":BUTTONS
                       }
        else:
            desc = StoriesCat.objects.filter(id=type).first()
            content = {"content": [{"name": "No story found. be first to add", "type": {
                "catName": desc, "catDesc": desc.catDesc}}], "typeof": "story", "url": "/", 
                "buttons":BUTTONS}

        return render(request, 'threadlist.html', content)
    elif(cat == "idiscuss"):
        discussions = DiscussionThreads.objects.filter(type=type)
        if(len(discussions) != 0):
            content = {"content": discussions, "typeof": "idiscuss", "url": "/thread?cat=idiscuss&&id={{con.id}}",
                       "buttons": BUTTONS}
        else:
            desc = DiscussionCat.objects.filter(id=type).first()
            content = {"content": [{"name": "No Discussion found. be first to add", "type": {
                "catName": desc, "catDesc": desc.catDesc}}],
                 "typeof": "idiscuss", "url": "/", 
                 "buttons": BUTTONS}
        return render(request, 'threadlist.html', content)
    else:
        return redirect(index)


def thread(request):
    global BUTTONS
    if request.user.is_authenticated:
        BUTTONS='<a href="logoutUser" class="btn">Logout</a>'+f'<a class="btn">{request.user.username}</a>'
    cat = request.GET.get('cat')
    id = request.GET.get('id')
    if(cat == "story" and id != ''):
        id = int(id)
        comments=Comment.objects.filter(onpost=id)
        context = {"story": StoriesThreads.objects.filter(id=id).first(
        ), "buttons": BUTTONS,"comments":comments,"typeof":"story"}
        print(context['story'].name)
        return render(request, 'thread.html', context)
    elif(cat == "idiscuss" and id != ''):
        id = int(id)
        context = {"story": StoriesThreads.objects.filter(id=id).first(
        ), "buttons": BUTTONS}
        print(context['story'].name)
        return render(request, 'thread.html', context)
    else:
        return redirect(index)


def submitPost(request):
    cat = request.GET.get('cat')
    type = request.GET.get('type')
    if request.method == "POST":
        if request.user.is_authenticated:
            BUTTONS='<a href="logoutUser" class="btn">Logout</a>'+f'<a class="btn">{request.user.username}</a>'
            title = request.POST.get('title')
            intro = request.POST.get('intro')
            body = request.POST.get('body')
            conclusion = request.POST.get('conclusion')
            author=request.user.username
            if type == "story":
                category = StoriesCat.objects.filter(catName=cat).first()
                post = StoriesThreads(
                    name=title, body=body, head=intro, conclusion=conclusion, type=category,author=author)
                post.save()
                return redirect(threadlist)
            elif type == "idiscuss":
                category = DiscussionCat.objects.filter(catName=cat).first()
                post = DiscussionThreads(
                    name=title, body=body, head=intro, conclusion=conclusion, type=category,author=author)
                post.save()
                return redirect(threadlist)
        else:
            return redirect(loginUser)
    else:
        return redirect(index)

def submitComment(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            content=request.POST.get('comment')
            type=request.GET.get('type')
            category=request.GET.get('category')
            id=int(request.GET.get('id'))
            author=request.user
            comment=Comment(content=content,author=author,onpost=id,category=category,type=type)
            comment.save()
            return redirect(thread)
        else:
            return redirect(loginUser)
    else:
        return redirect(index)


def loginUser(request):
    global BUTTONS
    #h123@123
    if request.user.is_authenticated:
        BUTTONS='<a href="logoutUser" class="btn">Logout</a>'+f'<a class="btn">{request.user.username}</a>'
        return redirect(index)
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                BUTTONS='<a href="logoutUser" class="btn">Logout</a><h3>'+f'<a class="btn">{request.user.username}</a>'
                return redirect(index)
            else:
                return redirect(loginUser)
            
        else:
            return render(request,'login.html')

def signupUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=User.objects.create_user(username,email,password)
        customer.save()
        return redirect(loginUser)

    else:
        return render(request,'signup.html')


def logoutUser(request):
    global BUTTONS
    logout(request)
    BUTTONS='<a href="loginUser" class="btn">Login</a><a href="signupUser" class="btn">Signup</a>'
    return redirect(index)