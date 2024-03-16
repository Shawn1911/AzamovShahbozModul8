"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

schema_view = get_schema_view(
    openapi.Info(
        title="Exam Project",
        default_version='v1',
        description="""exam javoblarini githubga yuklaymiz va linkini yuboramiz


1. category va product(product xususiyatlari va kop rasmli bolsin, owneri ham),login(jwt orqali),
register(username, email,password, confirm_password - emailga saytdan royhatdan otildi degan xabar kelsin) qilinsin

2. category(name) boyicha filter, product nomi va description boyicha search qilinsin,
category va product uchun list api pagination bilan chiqarilsin

3. har kuni ertalab 8:00 da barcha userlarga bugun bizda yangi productlar qo'shilsin degan xabarni pochtasiga yuborish kk

4. productni o'zgartirish va o'chirish uchun api chiqarilsin(faqat owner uchun)

5. category,product,user modellari uchun UUID ishlatilsin, swaggerda ham uuid orqali ishlaydigan qilish kerak,
postgres databaseda o'z ismimiz bilan user ochamiz database nomi esa ism_db bolsin""",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('apps.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
