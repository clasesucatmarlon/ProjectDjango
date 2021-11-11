from django.urls import path
from . views import *


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', ListManageUserViews.as_view(), name='list'),
    path('list', ListManageUserViews.as_view(), name='list'),
    path('detail/<str:pk>/', DetailManageUserViews.as_view(), name='detail'),
    path('create', CreateManageUserViews.as_view(), name='create'),
    path('update/<str:pk>/', UpdateManageUserViews.as_view(), name='update'),
    path('delete/<str:pk>/', DeleteManageUserViews.as_view(), name='delete'),
]