def func_executor(*funcs):
    result = []

    for func, args in funcs:
        result.append(f"{func.__name__} - {func(*args)}")

    return '\n'.join(result)