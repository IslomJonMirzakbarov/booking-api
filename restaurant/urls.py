from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'booking/tables', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', views.MenuItemsView.as_view(), name=views.MenuItemsView.name),
    path('menu/<int:pk>/', views.MenuItemRetrieveUpdateDelete.as_view(),
         name='menuitem-detail'),
]

