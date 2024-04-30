from django.urls import include, path
from rest_framework import routers
from .views import AnalyticalMethodViewSet


from . import views

router = routers.DefaultRouter()
router.register(r"analytical-methods", AnalyticalMethodViewSet)

app_name = "an_organ"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]


#  self.list_url = reverse("barkyapi:bookmark-list")
#         self.detail_url = reverse(
#             "barkyapi:bookmark-detail", kwargs={"pk": self.bookmark.id}
#         )

# router = routers.DefaultRouter()
# router.register(r"bookmarks", views.BookmarkViewSet)
