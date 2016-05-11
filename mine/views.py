from django.shortcuts import render
from number_one.utilities import audit_error



# @audit_error
def index(request):
    greeting = 'hello'
    context = {
        'greeting': greeting,
    }

    return render(request, 'mine/index.html', context)
