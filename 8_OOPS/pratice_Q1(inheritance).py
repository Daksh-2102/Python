#create a class (2-D vector) and use it to create another class representing a 3-D  vector.

class TwoD_vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The 2D vectors are {self.i}i + {self.j}j")

class ThreeD_vector(TwoD_vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The 3D vectors are {self.i}i + {self.j} + {self.k}k")

vec1 = TwoD_vector(1,2)
vec1.show()

vec2 = ThreeD_vector(1,2,3)
vec2.show()
    

     

