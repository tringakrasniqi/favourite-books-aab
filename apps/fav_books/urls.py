from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed),  # GET request
    path('add_book', views.add_book),  # POST request
    # formati <int:book_id> eshte vendosur si indikator qe presim nje id nga url
    path('<int:book_id>', views.show_book),  # GET request
    path('delete/<int:book_id>', views.delete_book)  # POST request
]
