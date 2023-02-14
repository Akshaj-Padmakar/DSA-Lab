# Here We haven't considered Native state as a feild. (Solves Part 1, 2, 3, 4)

class Student:
    def __init__(self, name, roll_no, hostel, group_no, hobby, phone_no):
        self.name = name
        self.roll_no = roll_no
        self.hostel = hostel
        self.group_no = group_no
        self.hobby = hobby
        self.phone_no = phone_no


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


# Example
students = [
    Student("Akshaj", 1, "A", 1, "Reading", "111-111-1111"),
    Student("Dhruv", 2, "B", 1, "Writing", "222-222-2222"),
    Student("Aryan", 3, "C", 2, "Cricket", "333-333-3333")
]

hash_table = HashTable(10)  # Bucket array of size 10

for student in students:
    hash_table.insert(student)

# Printing the entire Hash-Table !
for student in hash_table.buckets:
    if student is not None:
        print(student.name, student.roll_no, student.hostel, student.group_no, student.hobby, student.phone_no)
    else:
        print("[]")


print("\n\n")


# Printing only the phone_no. for each student!
for student in hash_table.buckets:
    if student is not None:
        print(student.name + " --> " + student.phone_no)

