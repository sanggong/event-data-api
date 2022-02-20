
def success(data=None):
    response = {'is_success': True}
    if data is not None:
        response['result'] = data
    return response


def error(e, code):
    response = {'is_success': False,
                'error_code': code,
                'error_message': e}
    return response
