from django.urls import include, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'playsessions', views.PlaySessionViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'employers', views.EmployerViewSet)
router.register(r'modules', views.ModulesViewSet)

urlpatterns = [
    re_path('api', include(router.urls)),
    re_path('employees/', views.login),
    re_path('addSession/', views.addSession),
    re_path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    re_path('addEthicalData/', views.addEthicalData),
]
