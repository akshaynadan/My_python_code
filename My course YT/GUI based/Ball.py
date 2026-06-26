class Ball:
    def __init__(self, canvas, x, y, diameter, xvelocity, yvelocity, color):
        self.canvas = canvas
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.diameter = diameter
        self.image = canvas.create_oval(x, y, x + diameter, y + diameter, fill=color)

    def move(self,width,height):
        coords=self.canvas.coords(self.image)
        print(coords)
       
        if (coords[0]<0 or coords[2]>=width) :
            self.xvelocity=-self.xvelocity
            
        if (coords[1]<0 or coords[3]>=height) :
            self.yvelocity=-self.yvelocity
        # else:
        #     self.yvelocity+=2.5
       
        self.canvas.move(self.image,self.xvelocity,self.yvelocity)