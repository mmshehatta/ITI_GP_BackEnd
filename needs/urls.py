from django.urls import path
from django.conf.urls import url
from needs import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('need/', views.needApi),
    path('need/<int:id>',views.needApi),
    path('needByUserId/<int:id>',views.getNeedByUserId),


]