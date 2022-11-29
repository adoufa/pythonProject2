class Example:
    @classmethod
    def class_hello(cls):
        return f'class_hello {cls}'
Example.class_hello()
p = Example()
p.class_hello()
print(Example.class_hello())
