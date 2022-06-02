from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BlogView

router = DefaultRouter()
router.register('blog', BlogView)

urlpatterns = [
    path('blog/', include(router.urls)),
    path('blog/', BlogView.as_view())
]
