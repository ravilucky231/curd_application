from django.urls import path
from .views import index,create,edit,update,delete,login,user_logout


urlpatterns=[
    path('index/',index),
    path('create/',create),
    path('edit/<int:sitiid>/',edit),
    path('update/<int:sitiid>/',update),
    path('delete/<int:sitiid>/',delete),
    path('login/', login),
    path('logout/', user_logout)

]