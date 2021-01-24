import funck


def runner(*args):
    if not args:
        funck.funck_1()
        funck.funck_2()
        funck.funck_3()
    else:
        for func_name in args:
            getattr(funck, func_name)()


runner()
runner('funck_1')
runner('funck_1', 'funck_2')
