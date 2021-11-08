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
light = BlyncLight.get_light()      #la luz
cycleTime = 60                 #number of hours (in seconds for sleep()) as a formula
steps = 512+512+512                 #2*256 steps per color
color = (255, 0, 0)                 #start with red
#NOTE: (red,blue,green)!!!

#setup
light.on = True

while(True):
    #increase green
    for green in range(0,255,1):
        color = (color[0],color[1],green)
        light.color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #decrease red
    for red in range(255,0,-1):
        color = (red,color[1],color[2])
        light.color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #increase blue
    for blue in range(0,255,1):
        color = (color[0],blue,color[2])
        light.color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #decrease green
    for green in range(255,0,-1):
        color = (color[0],color[1],green)
        light.color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #increase red
    for red in range(0,255,1):
        color = (red,color[1],color[2])
        light.color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    
    #decrease blue
    for blue in range(255,0,-1):
        color = (color[0],blue,color[2])
        light.color = color
        #wait until next update
        time.sleep(cycleTime/steps)
    

#teardown
light.on = False

'''#useful color values
True-ish white: (215,235,145)
'''

