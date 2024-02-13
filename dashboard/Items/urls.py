from django.urls import path, re_path
from Items import views
from .views import Index,SignUpView, Dashboard, AddItem, EditItem, DeleteItem
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('items/',views.ItemApi,name="item-list"),
    path('items/<int:id>', views.ItemApi, name="item-id"),
    path('category/',views.CategoryApi,name="category-list"),
    path('category/<int:id>', views.CategoryApi, name="category-id"),
    path('counts/', views.CountsApi, name='counts-api'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
]