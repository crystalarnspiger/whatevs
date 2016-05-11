from django.shortcuts import render_to_response
from django.conf import settings


def audit_error(decorated_function):
    ''' Decorates broker call functions for auditing authorization and
    error handling '''
    def inner_function(request, **additional):
        try:
            return decorated_function(request, **additional)
        except Exception:
            msg = ('I lost it.')
            context = {'exception_message': msg,
                       'document_title': 'Error Page'}
            return render_to_response('number_one/error.html', context)

    return inner_function
