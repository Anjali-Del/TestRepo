from django.shortcuts import render
from django import template
from models import author_signup, article
from django.utils import timezone

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")


def signup(request):
    return render(request, "register.html")


def new_session(request):
    a = author_signup(author_name=request.POST['name'], email=request.POST['email'], pswd=request.POST['password'])
    a.save()
    request.session['author_id'] = a.aid
    request.session['author_name'] = a.author_name
    request.session['author_email'] = a.email
    return render(request,"nsession.html",{"author":a})


def login(request):
    return render(request, "login.html")


def login_view(request):
    a = author_signup.objects.get(email=request.POST['email'])
    if a.pswd == request.POST['password']:
        request.session['author_id'] = a.aid
        request.session['author_name'] = a.author_name
        request.session['author_email'] = a.email
        return render(request,"nsession.html",{"author":a})
    else:
        return render(request,"incorrect_login.html")


def logout(request):
    try:
        del request.session['author_id']
        del request.session['author_name']
        del request.session['author_email']
    except KeyError:
        pass
    return render(request,"logout.html")


def add_view(request):
    a = author_signup(aid=request.session.get('author_id'), author_name=request.session.get('author_name'), email=request.session.get('author_email'))
    return render(request,"user.html",{"author":a})


def new_article(request):
    ai = request.session.get('author_id')
    aname = request.session.get('author_name')
    aemail=request.session.get('author_email')
    a = author_signup(aid=ai, author_name=aname, email=aemail)
    return render (request, "add_article.html", {"author":a})


def success_page(request):
    ai = request.session.get('author_id')
    aname = request.session.get('author_name')
    aemail=request.session.get('author_email')
    a = author_signup(aid=ai, author_name=aname, email=aemail)
    at = article(uid=a, title=request.POST['title'], content=request.POST['content'], pub_date=timezone.now())
    at.save()
    return render(request, "success.html", {"art":at})
    

def view_article(request):
    ai = request.session.get('author_id')
    if ai == None:
        art = article.objects.all()
        return render(request,'view.html',{"article_list":art})
    else:
        aname = request.session.get('author_name')
        aemail=request.session.get('author_email')
        a = author_signup(aid=ai, author_name=aname, email=aemail)
        all_article = article.objects.all()
        art = article.objects.filter(uid=ai)
        return render(request,'view_aut.html',{'auth':a,'article_list':art})


def delete_article(request, ar_id):
    ai = request.session.get('author_id')
    aname = request.session.get('author_name')
    aemail=request.session.get('author_email')
    a = author_signup(aid=ai, author_name=aname, email=aemail)
    q = article.objects.filter(article_id=ar_id).delete()
    return render(request, 'deleted.html', {"auth":a})


def edit_article(request, ar_id):
    ai = request.session.get('author_id')
    aname = request.session.get('author_name')
    aemail=request.session.get('author_email')
    a = author_signup(aid=ai, author_name=aname, email=aemail)
    q = article.objects.get(article_id=ar_id)
    return render(request, 'edit.html', {'article':q, 'auth':a})


def success_edit(request, ar_id):
    ai = request.session.get('author_id')
    aname = request.session.get('author_name')
    aemail=request.session.get('author_email')
    a = author_signup(aid=ai, author_name=aname, email=aemail)
    at = article(uid=a, article_id=ar_id, title=request.POST['title'], content=request.POST['content'], pub_date=timezone.now())
    at.save()
    return render(request, "success_update.html", {"art":at})

