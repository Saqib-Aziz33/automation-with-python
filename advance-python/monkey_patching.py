# Monkey Patching in Python (Dynamic Behavior)
class A:
    def func(self):
        print("func() is being called")


# New function to replace original func()

def monkey_f(self):
    print("monkey_f() is being called")


# Replacing the address of "func" with "monkey_f"
A.func = monkey_f
obj = A()
obj.func()
