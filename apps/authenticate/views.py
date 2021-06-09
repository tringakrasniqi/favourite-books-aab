from django.shortcuts import render, redirect
from .models import User
import bcrypt


def index(request):
    """
        Funksioni index - ben redirect ne url '/books' (faqen kryesore) nese kemi nje user loggedin (eshte e mundshme t'a dijme nese kemi id e user ne session)
    """
    if 'uid' in request.session:
        return redirect('/books')
    else:
        return render(request, 'index.html')


def login(request):
    """
        Funksioni Login - sigurohemi qe email-i egziston ne databaze dhe bejme redirect ne '/books'
    """
    user = User.objects.filter(email=request.POST['user_email'])
    # Krahasimi i password ne databaze me ate te dhene permes formes
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['uid'] = user[0].id
        return redirect('/books')
    else:
        return redirect('/')


def register(request):
    """
        Funksioni Register - perdor librarine bcrypt per te encode password, krijon ne User object te ri dhe ruan ne databaze. Nese eshte e suksesshme bejme redirect ne 'books' url
    """
    password = request.POST['user_password']
    # Krijimi i hash te password per te ruajtur ne databaze
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['user_email'], password=pw_hash)
    request.session['uid'] = user.id
    return redirect('/books')


def logout(request):
    """
        Funksioni logout - largon te dhenat ne session dhe nuk eshte e mundshme te casemi '/books' 
    """
    request.session.flush()
    return redirect('/')
