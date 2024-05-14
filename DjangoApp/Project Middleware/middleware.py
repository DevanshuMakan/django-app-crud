from django.shortcuts import render


def simplemiddleware(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 404:
            return render(request, 'Accounts/errorpage.html')
        return response
    return middleware