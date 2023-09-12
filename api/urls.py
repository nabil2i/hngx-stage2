from django.urls import path, include
# from rest_framework.routers import SimpleRouter
# from rest_framework.routers import DefaultRouter
from .import views

# router = DefaultRouter()
# router.register('/', views.PersonViewSet)

# urlpatterns = [
#   path('', include(router.urls))
# ]
# urlpatterns = router.urls

urlpatterns = [
  path('', views.PersonList.as_view(), name = "person_list"),
  path('<str:identifier>', views.PersonView.as_view(), name = "person_view"),
  # path('/<int:id>', views.PersonDetail.as_view(), name = "person_detail"),
]

# urlpatterns = [
#   path('', views.person_list, name = "person_list"),
#   path('/<str:identifier>', views.person_detail, name = "person_detail"),
# ]