from django.conf.urls import url, include
from rest_framework import routers
from sample.src import views

from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^echo/', views.echo),
    url(r'^access/', views.access)
]


#urlpatterns = format_suffix_patterns(urlpatterns)