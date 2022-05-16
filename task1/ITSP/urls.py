from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)

urlpatterns=[
    path('',views.index),
    path('ITSP220001',views.next1),
    path('ITSP220002',views.next2),
    path('ITSP220003',views.next3),
    path('ITSP220004',views.next4),
    path('ITSP220005',views.next5),
    path('ITSP220006',views.next6),
    path('ITSP220007',views.next7),
    path('ITSP220008',views.next8),
    path('ITSP220009',views.next9),
    path('ITSP220010',views.next10),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]