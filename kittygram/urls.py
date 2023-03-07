from django.urls import include, path

from cats.views import cat_list
from cats.views import cat_detail 

urlpatterns = [
   path('cats/', cat_list),
   path('cats/<int:pk>/', cat_detail),
]


