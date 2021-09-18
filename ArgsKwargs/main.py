def my_func(positional_args, *args, **kwargs):
    print("Hello World.")
    print(positional_args)
    print(args)
    print(kwargs)

my_func("positional args", "abc", docker="awesome", kubernetes="amazing")