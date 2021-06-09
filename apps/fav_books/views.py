from django.shortcuts import render, redirect
from datetime import datetime
from .models import User, Book


def feed(request):
    """
        Funksioni feed - bejme redirect ne '/books' nese kemi used logged in, nese jo kthehmi tek login/register format
    """
    if 'uid' in request.session:
        context = {
            "logged_user": User.objects.get(id=request.session['uid'])
        }
        return render(request, 'feed.html', context)
    else:
        return redirect('/')


def add_book(request):
    """
        Funksioni add_book - nese perdoruesi eshte loggedin at'her krijojme nje rekord te ri ne databaze me te dhenat nga forma, perndryshe bejme redirect ne index faqe
    """
    if 'uid' in request.session:
        logged_user = User.objects.get(id=request.session['uid'])
        year = datetime(
            year=int(request.POST['book_year_published']), month=1, day=1)
        book = Book.objects.create(title=request.POST['book_title'], author=request.POST['book_author'],
                                   isbn_number=request.POST['book_isbn'], published_year=year, of_user=logged_user)
        return redirect('/books')
    else:
        return redirect('/')


def show_book(request, book_id):
    """
        Funksioni show_book - nese perdoruesi eshte loggedin at'her marrim te dhenat e librit me ID te dhene ne URL dhe shfaqim nje faqe te re "show_book" me te dhenat e nje libri
    """
    if 'uid' in request.session:
        context = {
            "book_details": Book.objects.get(id=book_id)
        }
        # Te dhenat is dictionary qe i japim si parameter te trete tek 'render' na mundeson perdorimin e ketyre te dhenave ne templates
        # context dictionary eshte i mundshem te perdoret ne templatin 'show_book.html'
        return render(request, 'show_book.html', context)
    else:
        return redirect('/')


def delete_book(request, book_id):
    """
        Funksioni delete_book - nese perdoruesi eshte loggedin at'her ne e largojme librin me ID 'book_id' te dhene ne URL
    """
    if 'uid' in request.session:
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('/books')
    else:
        return redirect('/')
