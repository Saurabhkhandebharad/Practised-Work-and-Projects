from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):    
        circle = Circle()  # create a circle
        square = Square() #create a square

        self.play(Create(square)) #animate the creation of square
        self.play(square.animate.rotate(PI/4)) #rotate a certain amount
        self.play(ReplacementTransform(square,circle)) #transform the square into circle
        self.play(circle.animate.set_fill(PINK, opacity=0.5))  # set the color and transparency