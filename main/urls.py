from django.urls import path

from main.views import *


urlpatterns = [
    path('list/', ProductAPIView.as_view()),
    path('<int:pk>', RetrieveProductView.as_view()),
    path('delete/<int:pk>/', DestroyProductView.as_view()),
    path('create/', CreateProductView.as_view()),
    path('update/<int:pk>/', UpdateProductView.as_view())
]