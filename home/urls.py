from django.urls import path
from django.views.generic import ListView
from home.models import FAQDatabase
from . import views

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact),
    path('faq/', ListView.as_view(queryset=FAQDatabase.objects.all(), template_name='home/faq.html')),
    path('termsandconditions/', views.tandc),
    path('privacy/', views.privacy),
    path('submit_email', views.email_list),
]
