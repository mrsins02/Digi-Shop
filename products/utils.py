from django.http import HttpRequest


def slider_set_generator(iterable, num: int):
    """

    :param iterable: a set of objects to split
    :param num: number of objects in every set
    :return: a list of objects sets
    """
    result = []
    i = 0
    while i < len(iterable):
        result.append(iterable[i:i + num])
        i += num

    return result


def get_client_ip(request: HttpRequest):
    http_x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if http_x_forwarded_for:
        ip = http_x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
