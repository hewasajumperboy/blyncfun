'''################################
#
#Playing with the BlyncLight
#    (for fun and profit)
#Brandon Brocker (brandon.brocker@intel.com)
#Usage: run maybe?  I'm unsure as of yet...
#
################################'''

#imports
from blynclight import BlyncLight
import colorsys
import time

#declariations
light = BlyncLight.get_light()      #la luz
cycleTime = 60                      #number of minutes as a formula
fps = 24                            #more cinematic
steps = cycleTime * fps             #redefine for dramatic effect
steps = 256*2*3                     #steps as number of rgb integer steps
prev_color = (0,0,0)                #define previous color variable

#setup
light.on = True

while(True):
    for x in range(steps,0, -1):
        #convert HSV to RGB space based on step count (hue, saturation, value)
        raw_color  = colorsys.hsv_to_rgb(x/steps,1,1)
        #convert float to int for the RGB color this step
        color = (int(raw_color[0]*255),int(raw_color[1]*255),int(raw_color[2]*255))
        #update only if there's an integer change in RGB space
        if color != prev_color:
            prev_color = color
            light.color = color
        #sleep to to keep cadence
        time.sleep(cycleTime/steps)

#teardown
light.on = False

#this was a terrible idea
#so I'm leaving this as an example of what NOT to do in RGB space
#cycle through all the colors
#for x in range(0,255):
#    for y in range(0,255):
#        for z in range(0,255):
#            light.color = (x,y,z)
#            time.sleep(1/255)   #1 seconds per color range

'''#useful color values
True-ish white: (215,235,145)
'''
