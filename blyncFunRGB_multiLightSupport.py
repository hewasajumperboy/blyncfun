'''################################
#
#Playing with the BlyncLight
#    only in RGB this time
#Brandon Brocker (brandon.brocker@intel.com)
#Usage: python blyncFunRGB.py
#
################################'''

#imports
from blynclight import BlyncLight
#import colorsys
import time

#declariations
lights = BlyncLight.available_lights()      #Array of light members
cycleTime = 0                               #number of hours (in seconds for sleep()) as a formula
steps = 512+512+512                         #2*256 steps per color
color = (255, 0, 0)                         #start with red
#NOTE: (red,blue,green)!!!

#setup
for x in range(0, len(lights), 1):
        lights[x] = BlyncLight.get_light(x) #populate light member array

for x in range(0, len(lights), 1):
        lights[x].on = True                 #turn on lights for the big show


while(True):
    #increase green
    for green in range(0,255,1):
        color = (color[0],color[1],green)
        for x in range(0, len(lights), 1):
            lights[x].color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #decrease red
    for red in range(255,0,-1):
        color = (red,color[1],color[2])
        for x in range(0, len(lights), 1):
            lights[x].color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #increase blue
    for blue in range(0,255,1):
        color = (color[0],blue,color[2])
        for x in range(0, len(lights), 1):
            lights[x].color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #decrease green
    for green in range(255,0,-1):
        color = (color[0],color[1],green)
        for x in range(0, len(lights), 1):
            lights[x].color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #increase red
    for red in range(0,255,1):
        color = (red,color[1],color[2])
        for x in range(0, len(lights), 1):
            lights[x].color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #decrease blue
    for blue in range(255,0,-1):
        color = (color[0],blue,color[2])
        for x in range(0, len(lights), 1):
            lights[x].color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    

#teardown
light.on = False

'''#useful color values
True-ish white: (215,235,145)
'''

