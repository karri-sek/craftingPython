def print_msg(msg):
    def printer():
        print(msg)
    return printer

closure = print_msg("sekhar print this")
closure()


# another multipler closure

def makeMultipleOf(n):
    def multiplier(x):
        return x * n
    return multiplier

multiplierClosure = makeMultipleOf(5)
multiplierClosure.__closure__
print(" is it closure ", multiplierClosure.__closure__)
print("Closure  cell content at 0", multiplierClosure.__closure__[0].cell_contents)

print(" multiplication of 5 * 3 = ", multiplierClosure(3))
