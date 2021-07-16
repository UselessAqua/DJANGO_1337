from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.blog_info, name='blog_info'),
]