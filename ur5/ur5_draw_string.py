# by Chloe Dietz, Jacob Gonzales, Venkateshwaran Srinivasan, Farah Al Yasari

import urx
import logging

# note: in the future, this file will be imported into others who use draw_string()
# this main function is just for testing purposing
if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)

    rob = urx.Robot("192.168.43.107")
    #rob = urx.Robot("localhost")
    rob.set_tcp((0,0,0,0,0,0))
    rob.set_payload(0.5, (0,0,0))
    try:
        l = 0.01
        v = 0.05
        a = 0.3
        pose = rob.getl()
        init_pose = rob.getl()
        draw_string("HELLO WORLD!",l,a,v)
    finally:
        rob.close()


def draw_string(string, size, accel, velocity):
    for letter in string:
        if letter is "A":
            draw_A(size)
        if letter is "B":
            draw_B(size)
        if letter is "C":
            draw_C(size)
        if letter is "D":
            draw_D(size)
        if letter is "E":
            draw_E(size)
        if letter is "F":
            draw_F(size)
        if letter is "G":
            draw_G(size)
        if letter is "H":
            draw_H(size)
        if letter is "I":
            draw_I(size)
        if letter is "J":
            draw_J(size)
        if letter is "K":
            draw_K(size)
        if letter is "L":
            draw_L(size)
        if letter is "M":
            draw_M(size)
        if letter is "N":
            draw_N(size)
        if letter is "O":
            draw_O(size)
        if letter is "P":
            draw_P(size)
        if letter is "Q":
            draw_Q(size)
        if letter is "R":
            draw_R(size)
        if letter is "S":
            draw_S(size)
        if letter is "T":
            draw_T(size)
        if letter is "U":
            draw_U(size)
        if letter is "V":
            draw_V(size)
        if letter is "W":
            draw_W(size)
        if letter is "X":
            draw_X(size)
        if letter is "Y":
            draw_Y(size)
        if letter is "Z":
            draw_Z(size)
        if letter is "!":
            draw_Bang(size)
        if letter is " ":
            pose = rob.getl()
            pose[1] -= 6*size
            rob.movel(pose, acc=accel, vel=velocity)
        if(len(string) > 1): #put spaces in mult. char
            pose = rob.getl()
            pose[1] -= 3*size
            removeMarker(l, a, v)
            rob.movel(pose, acc=accel, vel=velocity)



# helper functions that perform a simple translate
def removeMarker(back_amount, acceleration, velcoity):
    rob.translate_tool((0, 0, - back_amount), acc=acceleration, vel=velcoity)

def placeMarker(back_amount, acceleration, velocity):
    rob.translate_tool((0, 0, back_amount), acc=acceleration, vel=velocity)

    #we want to normalize all of letters to start with placeMarker and end with removeMarker - FARAH


def draw_A(l):
    #placeMarker(l, a, v)
    #placeMarker(l, a, v)

    #start away from board
    placeMarker(l, a, v)

    pose = rob.getl() #initial position
    init_pose = rob.getl()


    # first big line
    pose[2] += 4*l
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    # second big line
    pose[2] -= 4*l
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    #middle line
    pose[2] += 2*l
    pose[1] += 3*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    init_pose[1] -= 4 * l
    rob.movel(init_pose, acc=a, vel=v)

    #placeMarker(l, a, v)
    removeMarker(l, a, v)


def draw_B(l):
    placeMarker(l, a, v)
    pose = rob.getl() #initial position

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 1*l
    pose[2] -= 1*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] += 1*l
    pose[2] -= 1*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] += 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 1*l
    pose[2] -= 1*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] += 1*l
    pose[2] -= 1*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] += 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)


def draw_C(l):
    placeMarker(l, a, v)
    init_pose = rob.getl()
    pose = rob.getl()

    # placeMarker(l, a, v)

    pose[2] +=4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -=4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    pose[2] -= 4*l
    pose[1] += 4*l
    rob.movel(pose, acc=a, vel=v)

    # placeMarker(l, a, v)

    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)


def draw_D(l):
    placeMarker(l, a, v)
    pose = rob.getl() #initial position

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 1*l
    pose[2] -= 1*l
    rob.movel(pose, acc=a, vel=v)
    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    pose[2] -= 1*l
    pose[1] += 1*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] += 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)


def draw_E(l):
    placeMarker(l, a, v);
    init_pose = rob.getl()
    pose = rob.getl() #Initial pose

    pose[2] += 4 * l
    rob.movel(pose, acc=a, vel=v) #Main line

    pose[1] -= 4 * l
    rob.movel(pose, acc=a, vel=v) #Top line

    removeMarker(l, a, v) #pickup to draw middle line


    pose[1] += 4*l
    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v) #go to beginning of middle line


    # placeMarker(l, a, v)

    pose[1] -= 4*l # middle line
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v) #pickup to draw bottom line

    pose[1] += 4*l
    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v) #position for drawing bottom line
    # placeMarker(l, a, v)

    pose[1] -= 4 * l
    rob.movel(pose, acc=a, vel=v) #Bottom line

    removeMarker(l, a, v)

    #end draw_E


def draw_F(l):
    placeMarker(l, a, v)

    init_pose = rob.getl()
    pose = rob.getl() #Initial pose

    pose[2] += 4 * l
    rob.movel(pose, acc=a, vel=v) #Main line

    pose[1] -= 4 * l
    rob.movel(pose, acc=a, vel=v) #Top line

    removeMarker(l, a, v) #pickup to draw middle line


    pose[1] += 4*l
    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v) #go to beginning of middle line


    placeMarker(l, a, v)

    pose[1] -= 4*l # middle line
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    init_pose[1] -= 4 * l
    rob.movel(init_pose, acc=a, vel=v)

    removeMarker(l, a, v)


def draw_G(l):

    placeMarker(l, a, v)

    pose = rob.getl()
    init_pose = rob.getl()

    removeMarker(l, a, v)

    pose[2] += 4*l
    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)


    pose[1] += 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] += 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 0.5*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    pose[2] -= 1.5*l
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)



def draw_H(l):
  placeMarker(l, a, v)
  pose = rob.getl() #initial position

  #draw the LHS leg of H
  pose[2]+= 4*l
  rob.movel(pose, acc=a, vel=v)

  #skip some middle space
  removeMarker(l, a, v)
  pose[2] -= 2*l
  rob.movel(pose, acc=a, vel=v)

  #draw the RHS leg of H
  pose[1] -= 4*l
  rob.movel(pose, acc=a, vel=v)

  #pick up to position for the middle part of H
  removeMarker(l, a, v)
  pose[2] += 2*l
  rob.movel(pose, acc=a, vel=v)

  #draw the middle part of  H
  pose[2] -= 4*l
  rob.movel(pose, acc=a, vel=v)

  #place at the end position
  removeMarker(l, a, v)


def draw_I(l):
    placeMarker(l, a, v)

    init_pose = rob.getl()
    pose = rob.getl()

    # placeMarker(l, a, v)

    pose[1] -=4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    pose[1] +=2*l
    rob.movel(pose, acc=a, vel=v)

    # placeMarker(l, a, v)

    pose[2] +=4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] +=2*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -=4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)


def draw_J(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    pose[1] -=2*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] +=4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] +=2*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -=4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)


def draw_K(l):
  placeMarker(l,a,v)
  pose = rob.getl() #initial position

  #assume the robot hand starts away from the board. move y = -1 to center the H
  pose[1] -= 1*l
  rob.movel(pose, acc=a, vel=v)

  #draw the | in K
  placeMarker(l, a, v)
  pose[2] += 4*l
  rob.movel(pose, acc=a, vel=v)

  #Go to the center intersection of K
  pose[2] -= 2*l
  rob.movel(pose, acc=a, vel=v)

  #draw the positive slope of K
  pose[1] -= 2*l
  pose[2] += 2*l
  rob.movel(pose, acc=a, vel=v)

  #returns to the center intersection of K
  pose[1] += 2*l
  pose[2] -= 2*l
  rob.movel(pose, acc=a, vel=v)

  #draw the negative slope of K
  pose[1] -= 2*l
  pose[2] -= 2*l
  rob.movel(pose, acc=a, vel=v)

  #place at the end position
  removeMarker(l, a, v)
  pose[1] -= 1*l
  rob.movel(pose, acc=a, vel=v)
  removeMarker(l, a, v)


def draw_L(l):
    placeMarker(l,a,v)
    pose = rob.getl()
    init_pose = rob.getl()

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)

    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)


    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)


def draw_M(l):
    placeMarker(l,a,v)
    pose = rob.getl()
    init_pose = rob.getl()

    pose[2] += 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)


    pose[2] -= 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)


    pose[2] -= 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)


def draw_N(l):

    placeMarker(l,a,v)
    pose = rob.getl()
    init_pose = rob.getl()

    placeMarker(l, a, v)

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 4*l
    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)

    init_pose[2] -= 4 * l
    rob.movel(init_pose, acc=a, vel=v)
    removeMarker(l, a, v)


def draw_O(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    placeMarker(l, a, v)

    pose[2] +=4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -=4*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] += 4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)

#normal- yes
def draw_P(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -= 3*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] += 3*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 3*l
    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)
    #end draw_R


def draw_Q(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    removeMarker(l, a, v)
    pose[1] -= 1*l
    pose[2] += 1*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 3*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 3*l
    rob.movel(pose, acc=a, vel=v)
    pose[2] -= 3*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] += 3*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 2*l
    pose[2] += 1*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 1*l
    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)
    #end draw_Q

#normal -
def draw_R(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -= 3*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] += 3*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -= 3*l
    pose[2] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)
    #end draw_R


def draw_S(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    pose[1] -= 3*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] += 3*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -= 3*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)
    #end draw_S


def draw_T(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    removeMarker(l, a, v)
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    # placeMarker(l, a, v)

    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] += 2*l
    rob.movel(pose, acc=a, vel=v)
    # placeMarker(l, a, v)

    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)
    # placeMarker(l, a, v)
    #end draw_T


def draw_U(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    pose[2] += 4 * l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 4 * l
    rob.movel(pose, acc=a, vel=v)

    pose[1] -= 4 * l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 4 * l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)
    #end draw_U


def draw_V(l):
    placeMarker(l,a,v)
    pose = rob.getl() #initial position
    init_pose = rob.getl()

    removeMarker(l, a, v)

    pose[2]+=4*l
    rob.movel(pose, acc=a, vel=v)
    placeMarker(l, a, v)

    pose[2] -= 4*l
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 4*l
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    init_pose[2] -= 4 * l
    rob.movel(init_pose, acc=a, vel=v)
    removeMarker(l,a,v)


def draw_W(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    pose[2] +=4*l
    rob.movel(pose, acc=a, vel=v)

    placeMarker(l, a, v)

    pose[2] -= 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] -= 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 4*l
    pose[1] -= 1*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)


def draw_X(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    pose[2] += 4 * l
    rob.movel(pose, acc=a, vel=v)
    placeMarker(l, a, v)

    pose[2] -= 4 * l
    pose[1] -= 4 * l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)

    pose[2] += 4 * l
    rob.movel(pose, acc=a, vel=v)
    placeMarker(l, a, v)

    pose[2] -= 4 * l
    pose[1] += 4 * l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 4 * l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l,a,v)


def draw_Y(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    removeMarker(l, a, v)
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    #placeMarker(l, a, v)

    pose[2] += 2*l
    rob.movel(pose, acc=a, vel=v)

    pose[2] += 2*l
    pose[1] += 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    # placeMarker(l, a, v)

    pose[2] -= 2*l
    pose[1] += 2*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[2] -= 2*l
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l, a, v)
    #end draw_Y


def draw_Z(l):
    placeMarker(l,a,v)
    init_pose = rob.getl()
    pose = rob.getl()

    removeMarker(l, a, v)
    pose[2] += 4*l
    rob.movel(pose, acc=a, vel=v)
    # placeMarker(l, a, v)

    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] += 4*l
    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    pose[1] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    removeMarker(l,a,v)
    #end draw_Z

def draw_Bang(l):
    init_pose = rob.getl()
    pose = rob.getl()

    removeMarker(l, a, v)
    pose[1] -= 2*l
    rob.movel(pose, acc=a, vel=v)
    # placeMarker(l, a, v)

    pose[2] += .5*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[2] += .5*l
    rob.movel(pose, acc=a, vel=v)
    # placeMarker(l, a, v)

    pose[2] += 3*l
    rob.movel(pose, acc=a, vel=v)

    removeMarker(l, a, v)
    pose[1] -= 2*l
    pose[2] -= 4*l
    rob.movel(pose, acc=a, vel=v)
    # placeMarker(l, a, v)
    #end draw_Z
