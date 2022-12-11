from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_n>/', views.number_view, name='number_view'), # order important int:page 1st and str:topic will be 2nd
    path('<str:topic>/', views.language_page, name='language_page'),
]