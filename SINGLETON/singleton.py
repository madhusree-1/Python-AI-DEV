# Method - 1 -- > best method to use
class singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)

        return cls._instance

# Method - 2
# class singleton:
#     _instance = None
#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls.__new__(cls)
#         return cls._instance

# if you apply method-2 it will be drawback because the user or developer don't know the methods inside the singleton class
# so they call through the class name then you can create the no of objects you want --> which actually violates the singleton
