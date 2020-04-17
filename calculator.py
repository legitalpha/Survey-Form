import re

print('My calculator')
print('Type quit to exit from calculator')

previous =0
run=True


def my_function():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Type an equation")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("You entered ",  previous)


while run == True:
     my_function()




