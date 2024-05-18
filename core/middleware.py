from django.shortcuts import render

class ComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add any condition here to bypass the "Coming Soon" page if needed
        if request.path.startswith('/admin'):
            return self.get_response(request)
        
        if request.path.startswith('/blog'):
            return self.get_response(request)
        
        if request.path.startswith('/accounts'):
            return self.get_response(request)
        
        if request.path.startswith('/'):
            return self.get_response(request)
        
        return render(request, 'coming_soon.html')
