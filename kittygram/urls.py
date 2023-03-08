from django.urls import include, path

from cats.views import CatList, CatDetail
# from cats.views import APICatDetail, 

urlpatterns = [
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>/', CatDetail.as_view()),
   # path('cats/', APICat.as_view()),
   # path('cats/<int:pk>/', APICatDetail.as_view()),
]


