
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("user", views.UserViewSet, basename="user")


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('login/', views.LoginView.as_view(),name = "user_login"),
    path('logout/',views.user_logout,name="user_logout")
]
urlpatterns += router.urls