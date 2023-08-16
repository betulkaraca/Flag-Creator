#Project Flag

#Ask the users input values
width=input("Flag width:\n")
width=int(width)

height=input("Flag height:\n")
height=int(height)

#Calculations
half_h=int(height/2)
half_w=int(width/2)

#Printings
upside='#' * half_w + '-' * half_w+'\n'
downside='-' * width+'\n'

print(upside*half_h, end='')
print(downside*half_h, end='')



