def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

result = outer_function(10)
print(result(5))