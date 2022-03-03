from typing import List
from django.http import HttpResponse, JsonResponse
from ninja import NinjaAPI
from user.models import UserModel
from point.models import PointHistory
from point.schema import NotEnoughPoint, PointSchema
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core import serializers

api_point = NinjaAPI(urls_namespace="point")


@api_point.get("/point", response=List[PointSchema])
def my_point(request):
    point = request.user.point
    return HttpResponse(point)


@api_point.get("/charge", response=List[PointSchema])
def charge(request, point):
    p = request.user.point
    UserModel.objects.filter(id=request.user.id).update(point=p+int(point))
    PointHistory.objects.create(user_id=request.user.id, point=int(point), history='charge', usage=True)
    return redirect('/point')


@api_point.get("/charge_history/{page}")
def charge_history(request, page: int):
    data = PointHistory.objects.filter(user_id=request.user.id, usage=True)
    data = list(data.values())
    p = Paginator(data, 5)
    total_page = p.num_pages
    p_data = p.page(page)
    p_data = p_data.object_list
    t_page = {"total_page": total_page}
    data = {"p": p_data, "t": t_page}

    return JsonResponse(data, safe=False)


@api_point.get("/usage_history")
def usage_history(request):
    data = PointHistory.objects.filter(user_id=request.user.id, usage=False)
    data = list(data.values())
    return JsonResponse(data, safe=False)
