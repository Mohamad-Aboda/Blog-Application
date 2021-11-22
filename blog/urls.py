from django.urls import path 

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'), 
    path('register/', views.register, name = 'register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('search/', views.search, name = 'search'),
    path('create/', views.createPost, name='create'), 
    path('delete/<int:pk>/', views.deletePost, name='delete'),
    path('update/<int:pk>/', views.updatePost, name='update'),
    path('<slug:post>/', views.postDetail, name='postDetail'), 
    path('category/<str:category>/', views.category_list, name='category_list')
]
