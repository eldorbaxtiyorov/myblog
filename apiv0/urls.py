from django.urls import path, include
from .views import router,CustomAuthToken
from rest_framework.authtoken import views
# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
# Additionally, we include login URLs for the browsable API.
