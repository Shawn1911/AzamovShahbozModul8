from django.urls import include, path

from apps.views import UserRegisterAPIView, CategoryListAPIView, ProductListAPIView

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('register', UserRegisterAPIView.as_view()),
    path('category', CategoryListAPIView.as_view()),
    path('product', ProductListAPIView.as_view()),
]
