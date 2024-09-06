from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, basename = 'hello-viewset')
router.register("profile", views.UserProfileViewSet,basename='user-profile')
router.register("feed", views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello_api_view'),
    path('login/', views.UserLoginViewApi.as_view()),
    path('', include(router.urls))
]
