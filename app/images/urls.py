from django.urls import path

from .views import AccountList, AccountDetail

urlpatterns = [
    path("api/account/", AccountList.as_view()),
    path("api/account/<int:pk>/", AccountDetail.as_view()),
]