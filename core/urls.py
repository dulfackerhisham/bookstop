from django.urls import path
from .views import *

urlpatterns = [
    path('', BookView.as_view(), name="bookview"),
    path('book-detail/<int:id>/', BookDetailView.as_view(), name="detailview"),
    path('book-delete/<int:id>/', BookDeleteView.as_view(), name="deletebook"),
]