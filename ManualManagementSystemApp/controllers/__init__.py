from django.urls import path
from .AccountsController import AccountsController
from .StudentsController import StudentsController

urlpatterns = [
    path("accounts/", AccountsController()),
    path("students/", StudentsController())
]