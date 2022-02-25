from django.shortcuts import render
from ninja import NinjaAPI

from .models import PointHistory

api = NinjaAPI()


@api.get("/point")
def test(request) -> None:
    template_name = "point/test.html"
    return render(template_name)
    # point_list = PointHistory.objects.filter()