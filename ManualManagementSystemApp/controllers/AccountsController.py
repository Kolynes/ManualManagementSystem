from utils.controller import Controller
from utils.shortcuts import json_response
from utils.decorators import ensure_signed_in, ensure_post

class AccountsController(Controller):
    
    @Controller.route()
    @Controller.decorate(ensure_signed_in)
    def ping(self, request):
        return json_response(200, data=request.user.dict)

    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post)
    def update(self, request):
        request.user.first_name = request.POST.get("first_name", request.user.first_name)
        request.user.last_name = request.POST.get("last_name", request.user.last_name)
        request.user.email = request.POST.get("email", request.user.email)
        request.user.phone = request.POST.get("phone", request.user.phone)
        request.user.save()
        return json_response(200)