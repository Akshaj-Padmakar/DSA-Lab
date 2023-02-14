#Code for part 6, 7

class Student:
    def __init__(self, name, roll_no, hostel, group_no, hobby, phone_no, native_state):
        self.name = name
        self.roll_no = roll_no
        self.hostel = hostel
        self.group_no = group_no
        self.hobby = hobby
        self.phone_no = phone_no
        self.native_state = native_state #Added native_state in my struct.


class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * self.size

    def hash_func(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    def insert(self, student):
        key = student.roll_no
        index = self.hash_func(key)
        while self.buckets[index] is not None:
            if self.buckets[index].roll_no == key:
                raise KeyError("Duplicate key")
            index = (index + 1) % self.size
        self.buckets[index] = student

    def search(self, key):
        index = self.hash_func(key)
        while self.buckets[index] is not None:
            if self.buckets[index].roll_no == key:
                return self.buckets[index]
            index = (index + 1) % self.size
        raise KeyError("Key not found")

    def __str__(self):
        return str([str(bucket) for bucket in self.buckets])

# Example usage
students = [
    Student("Akshaj", 1, "A", 1, "Reading", "111-111-1111", "Delhi"),
    Student("Dhruv", 2, "B", 1, "Reading", "222-222-2222", "Delhi"),
    Student("Aryan", 3, "C", 2, "Reading", "333-333-3333", "Tamil Nadu")
]

hash_table = HashTable(10)


for x in students:
    delattr(x, "hobby")  #deleting the attribute hobby from the student struct.


for student in students:
    hash_table.insert(student)


################## The below will result in an error! ##################
# for student in hash_table.buckets:
#     if student is not None:
#         print(student.hobby)
#     else:
#         print("[]")

# Printing the entire Hash-Table !
for student in hash_table.buckets:
    if student is not None:
        print(student.name, student.roll_no, student.hostel, student.group_no, student.phone_no, student.native_state)
