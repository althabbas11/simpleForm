from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    if request.method == 'GET' and 'name' in request.GET:
        name = request.GET.get('name')
        age = request.GET.get('age')

        return JsonResponse(
            {
                'result': 'My name is ' + name + ', I am ' + age + ' yo',
            },
            status=200,
        )


    return render(
        request,
        'index.html',
    )
