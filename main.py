'''
Mahima has been experimenting with a new style of art. She stands in front of a canvas and, using
her brush, flicks drops of paint onto the canvas. When she thinks she has created a masterpiece,
she uses her 3D printer to print a frame to surround the canvas.
This program is to help Mahima by determining the coordinates of the smallest possible rectangular
frame such that each drop of paint lies inside the frame. Points on the frame are not considered
inside the frame.
Input Specification
The first line of input contains the number of drops of paint, N, where 2 <= N <= 100 and N is an
integer. Each of the next N lines contain exactly two positive integers X and Y separated by one
comma (no spaces). Each of these pairs of integers represents the coordinates of a drop of paint on
the canvas. Assume that X < 100 and Y < 100, and that there will be at least two distinct points.
The coordinates (0, 0) represent the bottom-left corner of the canvas.
'''
num = int(input())
i = 0
xcoords = []
ycoords = []
for i in range(num):
    coordinput = input()
    x = coordinput.split(",")
    xcoords.append(int(x[0]))
    ycoords.append(int(x[1]))

xcoords.sort()
ycoords.sort()


print(f"{xcoords[0]-1},{ycoords[0]-1}")
print(f"{xcoords[num-1]+1},{ycoords[num-1]+1}")

