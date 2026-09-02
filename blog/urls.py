# portfolio/urls.py
from django.urls import path
from . import views  # seedha views import karo

from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog/edit/<int:id>/', views.blog_edit, name='blog_edit'),
  path('blog/delete/<int:id>/', views.blog_delete, name='blog_delete')
]
