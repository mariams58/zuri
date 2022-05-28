class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age,tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
    def  change_name(self, newName):
        newName = newName
        print("Hello, my name is", newName)

    def  change_age(self, newAge):
        newAge = newAge
        print("I am ", newAge)

    def  add_track(self, newTracks):
        newTracks = newTracks
        print("My study track is ", newTracks)

    def  get_score(self):
        print("I scored ", self.score)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
