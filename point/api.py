from ninja import NinjaAPI
from point.models import PointHistory
from point.schema import PointSchema, NotEnoughPoint
api_point = NinjaAPI(urls_namespace='point')


@api_point.get("/mypoint", response={200: PointSchema, 404: NotEnoughPoint})
def mypoint(request, user_id: int):
    try:
        # 작성중...
        point = PointHistory.objects.filter(user_id=user_id)[:1]
        return 200, point
    except PointHistory.DoesNotExist as e:
        return 404, {"message": "기록이 존재하지 않습니다."}


@api_point.post("/charge")
def charge(request, point, uid):
    pass


@api_point.get("/chargehistory")
def chargehistory(request, uid):
    data = PointHistory.objects.filter(user_id=uid, usage=True)

    return data


@api_point.get("/usagehistory")
def usagehistory(request, uid):
    data = PointHistory.objects.filter(user_id=uid, usage=False)

    return data


