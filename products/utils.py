def slider_set_generator(iterable, num: int):
    result = []
    i = 0
    while i < len(iterable):
        result.append(iterable[i:i + num])
        i += num

    return result
