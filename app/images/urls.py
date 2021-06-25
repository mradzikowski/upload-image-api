from django.urls import path

from .views import AccountDetail, AccountList, UserList

urlpatterns = [
    path("api/account/", AccountList.as_view()),
    path("api/account/<int:pk>/", AccountDetail.as_view()),
    path("api/user/", UserList.as_view()),
]
