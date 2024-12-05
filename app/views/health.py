from django.http import JsonResponse


def health_check(request):
    response_data = {"message": "Application is running"}
    return JsonResponse(response_data, status=200)
