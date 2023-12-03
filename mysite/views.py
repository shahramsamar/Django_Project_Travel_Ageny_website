from django.http import HttpResponse,JsonResponse

def http_test(requests):
    # return HttpResponse("hello shari")
    return HttpResponse('<h1>this is a new test</h1>')
def json_test(requests):
    return JsonResponse({'name':'shahram','family':'samar'})