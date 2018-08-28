try:  # called from host.py, main dir is ../
    import modes.IrisUtil as IrisUtil
except Exception as e:
    import IrisUtil

def test():
    print("haha")

class TestClass:

    def __init__(self, main):
        print(main)
        print("__init__ called")

    def loop(self):
        print("hello world")
        raise Exception('haha')


if __name__ == "__main__":
    test()
