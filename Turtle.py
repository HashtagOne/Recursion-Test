import turtle

t = turtle.Turtle()

def drawing_tree(t, length):
    if length < 5:
        return


    t.forward(length)
    t.left(30)
    drawing_tree(t, length - 20)
    t.right(60)
    drawing_tree(t, length - 20)      
    t.left(30)
    t.backward(length)
t.speed(0)
drawing_tree(t, 100)
turtle.mainloop()