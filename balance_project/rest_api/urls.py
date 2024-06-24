from rest_framework.routers import SimpleRouter 
from rest_api.views import RegisterModelViewSet
from django.urls import path, include # type: ignore

app_name = 'rest_api'
router = SimpleRouter()
router.register('register', RegisterModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls