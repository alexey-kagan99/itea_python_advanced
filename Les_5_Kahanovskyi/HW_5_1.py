from threading import Thread


def decor_threder(arg_name, arg_daemon):
    def dec(func):

        t = Thread(target=func, args=(), name=arg_name, daemon=arg_daemon)
        t.start()
        print(t.getName())
        print(t.isDaemon())

    return dec


@decor_threder('alex', True)
def func_1():
    print('hello')
