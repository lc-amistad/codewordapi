# solo cuando se agregue seguridad a la api

from rest_framework.views import exception_handler



def exeption_message(exc,context):
    handlers = {
        'error404':_handle_generic_error,
        'PermisoDenegado':_handle_generic_error,
        'NoAutentificado':_handle_generic_error,
        'ErrorValidacion':_handle_error_validation
    }
    response= exception_handler(exc, context)
    exception_class=exc.__class__.__name__
    if response is not None:
        response.data['status_code'] = response.status_code
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response

def _handle_error_validation(exc, context, response):
    response.data = {
        'error':'por favor inicie sesion para acceder',
        'status_code': response.status_code
    }
    return response

def _handle_generic_error(exc, context, response):
    return response
