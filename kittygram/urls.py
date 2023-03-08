from django.urls import include, path

from cats.views import APICat
from cats.views import APICatDetail 

urlpatterns = [
   path('cats/', APICat.as_view()),
   path('cats/<int:pk>/', APICatDetail.as_view()),
]


