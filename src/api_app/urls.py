from django.urls import include, path
from rest_framework import routers
from .views import CreateMyView

# router = routers.DefaultRouter()
# router.register(r'data', views.CreateMyView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('v1/',CreateMyView.as_view(),name="addData"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]