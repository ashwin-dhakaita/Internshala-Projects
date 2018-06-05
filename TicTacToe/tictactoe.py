import turtle
turtle.Screen()
def draw_board():
    turtle.pensize(5)
    turtle.pencolor((1,0,0))
    turtle.forward(300)
    turtle.backward(600)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(250)
    turtle.backward(125)
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(600)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(125)
    turtle.backward(375)
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(125)

def mark_decider(choice):
    if choice == 1:
        return (-200 , 187.5)
    elif choice == 2:
        return (0 , 187.5)
    elif choice == 3:
        return (200 , 187.5)
    elif choice == 4:
        return (-200 , 62.5)
    elif choice == 5:
        return (0 , 62.5)
    elif choice == 6:
        return (200 , 62.5)
    elif choice == 7:
        return (-200 , -62.5)
    elif choice == 8:
        return (0, -62.5)
    elif choice == 9:
        return (200 , -62.5)
    

def draw_circle(posx , posy):
    turtle.penup()
    turtle.home()
    turtle.setpos(posx , posy)
    turtle.forward(50)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(50)

def draw_cross(posx , posy):
    turtle.penup()
    turtle.home()
    turtle.setpos(posx , posy)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(50)
    turtle.backward(100)
    turtle.setpos(posx , posy)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)

def draw_horzline(posx , posy):
    turtle.penup()
    turtle.home()
    turtle.setpos(posx,posy)
    turtle.pendown()
    turtle.forward(-100)
    turtle.forward(600)

def draw_vertline(posx , posy):
    turtle.penup()
    turtle.home()
    turtle.setpos(posx , posy)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(62.5)
    turtle.forward(-375)

def draw_diag1(posx , posy):
    turtle.penup()
    turtle.home()
    turtle.setpos(posx , posy)
    turtle.pendown()
    turtle.left(45-12.5)
    turtle.forward(100)
    turtle.forward(-600)

def draw_diag2(posx , posy):
    turtle.penup()
    turtle.home()
    turtle.setpos(posx , posy)
    turtle.left(135+12.5)
    turtle.pendown()
    turtle.forward(100)
    turtle.backward(600)

def check_win(l):
    win = None
    if l[0] is l[1] is l[2]:
        win = l[0]
        posx , posy =  mark_decider(1)
        draw_horzline(posx , posy)
    elif l[3] is l[4] is l[5] :
        win = l[4]
        posx , posy = mark_decider(4)
        draw_horzline(posx , posy)
    elif l[6] is l[7] is l[8]:
        win = l[6]
        posx , posy = mark_decider(7)
        draw_horzline(posx , posy)
    elif l[0] is l[3] is l[6]:
        win = l[0]
        posx , posy = mark_decider(1)
        draw_vertline(posx , posy)
    elif l[1] is l[4] is l[7]:
        win = l[1]
        posx,posy = mark_decider(2)
        draw_vertline(posx , posy)
    elif l[2] is l[5] is l[8]:
        win = l[2]
        posx , posy = mark_decider(3)
        draw_vertline(posx ,posy)
    elif l[2] is l[4] is l[6]:
        win = l[2]
        posx,posy = mark_decider(3)
        draw_diag1(posx , posy)
    elif l[0] is l[4] is l[8]:
        win = l[0]
        posx , posy = mark_decider(1)
        draw_diag2(posx , posy)
    if win is None:
        for i in l:
            if  isinstance(i , int):
                break
        else:
            turtle.textinput("Winner" , 'The game is a draw')
            return 1
        return 0
    global toggle,toggleno
    if toggle is win:
        turtle.textinput("Winner" , 'Player' + str(toggleno) + 'wins the game')
    else:
        if toggleno == 1:
            turtle.textinput("Winner" , 'Player 2 wins the game(OK to exit)')
        elif toggleno == 2:
            turtle.textinput("Winner" , 'Player 1 wins the game(OK to exit)')
    return 1


gameexit = 0
l = [0,1,2,3,4,5,6,7,8]
draw_board()
toggle = turtle.textinput("Signature" , "Please enter your signature('cross' for cross , 'zero' for zero)")
toggleno = 1
while not gameexit:
    choice = turtle.textinput('Player turn ' , 'Player :' + str(toggleno) + 'ENTER THE BLOCK NUMBER')
    if isinstance(l[int(choice)-1] , int):
        if toggle == 'cross':
            posx , posy = mark_decider(int(choice))
            draw_cross(posx , posy)
            l[int(choice)-1] = 'cross'
            toggle = 'zero'
        elif toggle == 'zero':
            posx , posy = mark_decider(int(choice))
            draw_circle(posx , posy)
            l[int(choice)-1] = 'zero'
            toggle = 'cross'
        if toggleno == 1:
            toggleno = 2
        elif toggleno == 2:
            toggleno = 1
        if not check_win(l):
            continue
        else:
            break
    else:
        turtle.textinput("Choice error" , "Press OK to re-enter")

        
