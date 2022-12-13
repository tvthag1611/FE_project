from django.urls import path
  
# importing views from views..py
from .views import index_view, index_view_register
  
urlpatterns = [
    path('login/', index_view ),
    path('register/', index_view_register), 
]