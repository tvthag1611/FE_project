from django.urls import path
  
# importing views from views..py
from .views import index_view
  
urlpatterns = [
    path('list_room/', index_view ),
]