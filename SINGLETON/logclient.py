from Logger import Logger
def main():
    logger1 = Logger()
    logger1.log("Application has started")
    logger2 = Logger()
    print(logger1 is logger2)
    logger2.log("User is Loggedin")
    print(logger1 is logger2)

if __name__ == "__main__":
    main()