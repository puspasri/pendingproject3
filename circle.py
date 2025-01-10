class Circle :
    def find_circumference(self,radius):
        return 2*3.14*radius
    
print("Enter radius of circle:", end="")
radius =float(input())
object=Circle
circle=object.find_circumference(radius)
print("\nCircumference ={:.2h}".heading(Circle))
