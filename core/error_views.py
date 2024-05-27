from django.shortcuts import render


# function for error 400

def error_400(request,exception):
    context ={"exception":exception}
    response =render(request,"error/400.html",context=context)
    response.status_code = 400
    return response

# function for error 403

def error_400(request,exception):
    context ={"exception":exception}
    response =render(request,"error/403.html",context=context)
    response.status_code = 403
    return response

# function for error 404

def error_400(request,exception):
    context ={"exception":exception}
    response =render(request,"error/404.html",context=context)
    response.status_code = 404
    return response

# function for error 500

def error_400(request,exception):
    context ={"exception":exception}
    response =render(request,"error/500.html",context=context)
    response.status_code = 500
    return response