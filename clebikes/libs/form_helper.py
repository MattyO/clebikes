def is_valid(form, request_data):
    return form(request_data).is_valid()
