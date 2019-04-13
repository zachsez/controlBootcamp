import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from time import sleep

def drawcartpend(stateVector, time, timeStep, timeStop):
    # stateVector is a one dimesional vector, [x, x', theta, theta']
    x = stateVector[0]
    theta = stateVector[2]

    widthCart = 1       # Width of the cart
    heightCart = 0.5    # Height of the cart
    wheelRadius = 0.1   # Radius of cart's wheels
    massRadius = 0.2    # Radius of mass
    length = 1          # Length of pendulum arm

    # Create wheel shapes
    leftWheel = patches.Circle((x-0.8*(widthCart/2),wheelRadius/2),wheelRadius, color='k')
    rightWheel = patches.Circle((x+0.8*(widthCart/2),wheelRadius/2),wheelRadius, color='k')
    cart = patches.Rectangle((x-widthCart/2,wheelRadius), widthCart, heightCart, color='k')
    
    massX = x + length*np.sin(theta)
    massY = wheelRadius + heightCart/2 - length*np.cos(theta)
    
    arm = patches.ConnectionPatch((x,wheelRadius+heightCart/2),(massX,massY), coordsA="data", coordsB="data", color='k')
    mass = patches.Circle((massX,massY), massRadius, color='r')

    # Draw shapes on plot
    fig, ax = plt.subplots(1)
    plt.axis([-10,10,-5,5])
    ax.set_aspect('equal')

    ax.add_patch(leftWheel)
    ax.add_patch(rightWheel)
    ax.add_patch(cart)
    ax.add_patch(arm)
    ax.add_patch(mass)

    plt.show()

def main():
    print("Running main of drawcartpend.py")
    #for i in np.arange(-8,8,0.1):
      #  drawcartpend([i,0,np.sin(i),0], i, 0.1, 7.9)
    drawcartpend([1,0,3.14,0], 10, 0.1, 7.9)

if __name__ == "__main__":
    # If run as script call main function
    main()
