from django.urls import path
from .views import *


urlpatterns = [
    path("", BookmarkListview.as_view(), name="list"),
    path("add/", BookmarkCreateview.as_view(), name="add"),
    path("detail/<int:pk>/", BookmarkDetailview.as_view(), name="detail"),
    path("update/<int:pk>/", BookmarkUpdateview.as_view(), name="update"),
    path("delete/<int:pk>/", BookmarkDeleteview.as_view(), name="delete"),
]
