import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from time import sleep
import matplotlib.animation as animation

 # stateVector is a one dimesional vector, [x, x', theta, theta']
x = 0 #stateVector[0]
theta = 0 #stateVector[2]

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
    
arm = patches.FancyArrowPatch((x,wheelRadius+heightCart/2),(massX,massY), color='r')
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

#plt.show()

stateVectorGOL = np.zeros((160,2), dtype=float)
xValues = np.arange(-8,8,0.1)

for i in range(0,160):
    stateVectorGOL[i,0] = xValues[i]
    stateVectorGOL[i,1] = xValues[i] 

def drawcartpend(stateVector, timeStep):
    # Remove body to make global

    frameCount = stateVector.shape[0] # Number of rows in stateVector equals frame count

    ani = animation.FuncAnimation(fig, animate, frames=frameCount, fargs=(stateVector,), interval=timeStep, blit=True)

    plt.show()

    return True

def animate(frame, stateVector):
    currX = stateVector[frame, 0]
    currTheta = stateVector[frame, 1]

    currMassX = currX + length*np.sin(currTheta)
    currMassY = wheelRadius + heightCart/2 - length*np.cos(currTheta)

    leftWheel.set_center((currX-0.8*(widthCart/2),wheelRadius/2))
    rightWheel.set_center((currX+0.8*(widthCart/2),wheelRadius/2))
    cart.set_x(currX-widthCart/2)
    arm.set_positions((currX,wheelRadius+heightCart/2),(currMassX,currMassY))
    mass.set_center((currMassX,currMassY))

    return leftWheel, rightWheel, cart, arm, mass



def main():
    print("Running main of drawcartpend.py")
    #for i in np.arange(-8,8,0.1):
      #  drawcartpend([i,0,np.sin(i),0], i, 0.1, 7.9)
    #drawcartpend([1,0,3.14,0], 10, 0.1, 7.9)

    drawcartpend(stateVectorGOL, 100)

    #ani = animation.FuncAnimation(fig, animate, frames=150, interval=100, blit=True)

    #plt.show()

if __name__ == "__main__":
    # If run as script call main function
    main()
