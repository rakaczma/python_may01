class A:
    def introduce(self):
        print("I'm A")

class B:
    def introduce(self):
        print("I'm B")

class C(A):
    def different(self):
        print("Different")

my_list = [A(), B(), C()]

for poli_class in my_list:
    poli_class.introduce()


# a = 1
# b = 'string'
# c = 1, 2, 3
# d = {'key': 1}
#
# print(a)
# print(b)
# print(c)
# print(d)