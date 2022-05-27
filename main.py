class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("The student name is {} and his age {} has the following Track: {} and score of {} ".format(self.name, self.age, self.tracks, self.score))

    def change_name(self, newName):
        self.name = newName
        print("The student New name is {} ".format(self.name))
    def change_age(self, newAge):
        self.age = newAge
        print("The student New age is {} ".format(self.age))
    def add_track(self, newTrack):
        self.tracks = newTrack
        print("The student New track is {} ".format(self.tracks))
    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print("The new score is: ", Bob.get_score())
