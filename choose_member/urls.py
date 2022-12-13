from django.urls import path
  
# importing views from views..py
from .views import index_choose_member
  
urlpatterns = [
    path('choose_member/', index_choose_member), 
]