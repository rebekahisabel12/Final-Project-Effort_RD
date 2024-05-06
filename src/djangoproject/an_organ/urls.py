from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import AnalyticalMethodViewSet, InstrumentViewSet, HomeView, UserViewSet


from . import views

app_name = "an_organ"

router = DefaultRouter()
router.register(r'instruments', views.InstrumentViewSet)
router.register(r'analytical-methods', views.AnalyticalMethodViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('', HomeView.as_view(), name='home'),
    path("", include(router.urls)),
]

urlpatterns += router.urls


#  self.list_url = reverse("barkyapi:bookmark-list")
#         self.detail_url = reverse(
#             "barkyapi:bookmark-detail", kwargs={"pk": self.bookmark.id}
#         )

# router = routers.DefaultRouter()
# router.register(r"bookmarks", views.BookmarkViewSet)
