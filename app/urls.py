from django.urls import path
from .views import index, tambah_user, post_user, master_user, update_user, postupdate_user, delete_user

urlpatterns = [
    path('index', index,name="index"),
    path('tambah_user', tambah_user, name='tambah_user'),
    path('post_user', post_user, name='postuser'),
    path('master_user', master_user, name='masteruser'),
    path('update_user/<str:userid>', update_user, name='updateuser'),
    path('postupdate_user', postupdate_user, name='postupdateuser'),
    path('delete_user/<str:userid>', delete_user, name='deleteuser')
]