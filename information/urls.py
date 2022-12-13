from django.urls import path
  
# importing views from views..py
from .views import index_view
  
urlpatterns = [
    path('profile/', index_view )
]