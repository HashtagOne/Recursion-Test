import turtle

t = turtle.Turtle()

def drawing_tree(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    t.left(45)
    drawing_tree(t, length / 1.4142, depth - 1)
    t.right(90)
    drawing_tree(t, length / 1.4142, depth - 1)     
    t.left(45)
t.speed(0)
drawing_tree(t, 100, 6)
turtle.mainloop()