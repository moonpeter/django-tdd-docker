from django.http import JsonResponse


def ping(reqeust):
    data = {"ping": "pong!"}
    return JsonResponse(data)
