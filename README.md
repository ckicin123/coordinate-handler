# coordinate-handler
handles coordinates by moving your cursor to act as a point

this code will control your cursor and will interpret a coordinate system and instructions to draw or plot points using the cursor
do not have anything open that's important as it can click and ruin stuff on those windows
after hitting run open a drawing application (this is made for microsoft paint so perfferably use that)

at the bottom of the code you can see what the code something is assigned to a variable called "orderofop"
this variable should contain correct syntax for the operations the coordinate handler should do and in the correct order

after you have an orderofop you should use it as the paramater to the function "processinstruction(orderofop)"
this of course means the variable does not need to be orderofop it just needs to be passed into this function

syntax:
should be a list with each index holding instructions in that order

e.g.

orderofop=[instruction1,instruction2......] so on

instructions:
["moveto",[x,y]]
["setangle",angle]
["addangle",angle]
["iterate",number of iterations,[instruction1,instruction2...]]
["drawforward",numOfPixels]

explanation of instructions:

["moveto",[x,y]]
moves the current position of the cursor to the given x,y coordinates

["drawforward",numOfPixels]
draws forward from the cursor's current position a specified number of pixels in the direction of it's current angle

["setangle",angle]
sets the angle the cursor is facing, the default is strait up, angle is anti-clockwise (so when you draw forward it'll draw forwards in that angle)

["addangle,angle]
adds to the current angle of the cursor

["drawrandom"]
draws to a random point from it's current position in a bounding box around the origin/(0,0) coordinate

["iterate",number of iterations,[instruction1,instruction2...]]
iterates through a given list of instructions a given number of times



examples of using this

orderofop=[["moveto",[100,100]],["drawforward",100]]
processinstruction(orderofop)

this will draw a strait line going up from coordinates (100,100) for 100 pixels

orderofop=[["moveto",[200,100]],["setangle",270],["drawforward",100]]
processinstruction(orderofop)

this will draw a strait line going from coordinates (200,100) to the right for 100 pixels

orderofop=[
["moveto",[200,-50]],
["iterate",5,
  [
    ["drawforward",30],
    ["addangle",72]
  ]
]

]
processinstruction(orderofop)

this will draw a pentagon, it moves the cursor to (200,-50) then iterates through the instructions: draw forward 30 pixels, turn 72 degrees (72 degrees is the exterior angle of a regular pentagon)






you can also have a loop create instructions to draw some cool patterns (which is the loop at the bottom)
feel free to delete the loop to use it normally first before doing anything crazy with it or if your feeling like it, go for it and use the loop
