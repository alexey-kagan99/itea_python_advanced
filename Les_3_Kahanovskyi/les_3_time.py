from time import clock

def time_counter(func):

    def wrapper(*args, **kwargs):

        current_time = clock()
        rez = func(*args, **kwargs)
        dt = clock() - current_time
        print(f" function's time is {dt} seconds ")
        return rez
    return wrapper


@time_counter
def add_arg(arg1, arg2):

    res = arg1 + arg2
    print(res)

print(time_counter(add_arg(1,2)))