from astral import LocationInfo
from astral.sun import sun
#import pytz
from datetime import datetime
from datetime import time
from zoneinfo import ZoneInfo
from time import sleep
import os
import subprocess
import signal

localCity="Bend"
localRegion="Oregon"
localTzName="America/Los_Angeles"
localZoneInfo = ZoneInfo(localTzName)
localLatitude = 44.074278
localLongitude = -121.270139
localElevation = 1104.29
localLocationInfo = LocationInfo(localCity, localRegion, localTzName, localLatitude, localLongitude)
dtNow = datetime.now(tz=localZoneInfo)
localSun = sun(observer = localLocationInfo.observer, tzinfo=localZoneInfo)
blinkProcess = subprocess.Popen('busylight --all blink 0xffff00', shell = True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
os.killpg(os.getpgid(blinkProcess.pid), signal.SIGTERM)
bedtime = datetime.combine(dtNow.date(), time(21, 30, 0, 0, tzinfo=localZoneInfo))
bedtimeWarnStart = datetime.combine(dtNow.date(), time(19, 52, 0, 0, tzinfo=localZoneInfo))
bedtimeWarnEnd = datetime.combine(dtNow.date(), time(19, 55, 0, 0, tzinfo=localZoneInfo))
blinkProcessRunning = False

while True:
    #if new day?
    if dtNow.day != datetime.now(tz=localZoneInfo).day:
        #update day variable with today
        dtNow = datetime.now(tz=localZoneInfo)
        #recalculate the sun today
        localSun = sun(observer = localLocationInfo.observer, tzinfo=localZoneInfo)
        #recalculate bedtime today
        bedtime = datetime.combine(dtNow.date(), time(21, 30, 0, 0, tzinfo=localZoneInfo))
        bedtimeWarnStart = datetime.combine(dtNow.date(), time(19, 52, 0, 0, tzinfo=localZoneInfo))
        bedtimeWarnEnd = datetime.combine(dtNow.date(), time(19, 55, 0, 0, tzinfo=localZoneInfo))
    else:
        dtNow = datetime.now(tz=localZoneInfo)

    # check if we're between dusk and bedtime (note: this might be an issue in the summer)
    if dtNow > localSun["dusk"] and dtNow < bedtime:
        if blinkProcessRunning == False:
                os.system('busylight --all on 0xbbffff')
    else:
        if blinkProcessRunning == False:
            os.system('busylight --all off')

    #check if we should start warning  of impending bedtime
    if dtNow >= bedtimeWarnStart and dtNow <= bedtimeWarnEnd:
        if blinkProcessRunning == False:
            blinkProcess = subprocess.Popen('busylight --all blink 0xffff00', shell = True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
            blinkProcessRunning = True
    else:
        #send signal to kill process group (will kill all child processes started by shell)
        if blinkProcessRunning == True:
            os.killpg(os.getpgid(blinkProcess.pid), signal.SIGTERM)
            blinkProcessRunning = False
            os.system('busylight --all on 0xbbffff')

    sleep(60)

#if/when you calculate effects of elevation... or if you care...
#Location(localLocationInfo).dusk(observer_elevation = 1104.29)
