from singleton import *
def main():
    a = singleton()
    b = singleton()
    print(a is b)

if __name__ == "__main__":
    main()