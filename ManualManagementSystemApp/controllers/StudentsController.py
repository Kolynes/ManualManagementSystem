from utils.controller import Controller
from utils.shortcuts import json_response
from utils.decorators import ensure_signed_in, ensure_post
from ManualManagementSystemApp import models, forms
from django.db.models import Q

class StudentsController(Controller):

    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post)
    def create(self, request):
        student = forms.StudentModelForm(request.POST)
        if student.is_valid():
            student.save()
            return json_response(201)
        else:
            return json_response(409, error={
                "summary": "Invalid data",
                "fields": student.errors
            })

    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post)
    def delete(self, request):
        try:
            student = models.StudentModel.objects.get(id=request.POST["id"])
            student.delete()
            json_response(200)
        except models.StudentModel.DoesNotExist:
            json_response(404, error={
                "summary": "Student not found"
            })

    @Controller.route()
    @Controller.decorate(ensure_signed_in)
    def get(self, request):
        department = request.GET.get("department", "")
        level = request.GET.get("level", "")
        query = request.GET.get("query", "")
        queryset = models.StudentModel.objects.filter(
            Q(first_name__contains=query) |
            Q(last_name__contains=query) |
            Q(email__contains=query),
            department__contains=department,
            level__contains=level
        )
        return json_response(200, data=[
            student.dict for student in queryset
        ])

    @Controller.route()
    @Controller.decorate(ensure_signed_in, ensure_post)
    def update(self, request):
        try:
            student = models.StudentModel.objects.get(id=request.POST["id"])
            student.first_name = request.POST.get("first_name", student.first_name)
            student.last_name = request.POST.get("last_name", student.last_name)
            student.email = request.POST.get("email", student.email)
            student.department = request.POST.get("department", student.department)
            student.reg_no = request.POST.get("reg_no", student.reg_no)
            student.level = request.POST.get("level", student.level)
            student.save()
            return json_response(200)
        except models.StudentModel.DoesNotExist:
            return json_response(404, error={
                "summary": "Student not found"
            })
