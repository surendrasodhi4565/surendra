class circle:
    def CalculateArea (self):
            print("enter radius:")
            self.s = float (input())
            area = 3.14*self.s*self.s
            print("area of circle is = %f"%(area))
    def Calculateperimeter(self):
            Perimeter = 2*3.14*self.s
            print("Perimeter of circle is = %f"%(perimeter))
Circles = circle()
Circles.CalculateArea()
Circles.Calculateperimeter()
