from django.urls import path
from books import views

urlpatterns = [
    path("checkout", views.checkout, name='checkout'),
    path("return", views.return_book, name='return'),
    path("overdues", views.overdues, name='overdues')
]