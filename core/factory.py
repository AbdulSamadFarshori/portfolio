def get_ip(request):

    user_ip_address = request.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.get('REMOTE_ADDR')
    return ip