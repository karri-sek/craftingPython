def print_msg(msg):
    def printer():
        print(msg)
    return printer

closure = print_msg("sekhar print this")
closure()
