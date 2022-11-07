from astral import LocationInfo
from astral.sun import sun
import pytz
from datetime import datetime
from datetime import time
from zoneinfo import ZoneInfo
from time import sleep
import os

localCity="Bend"
localRegion="Oregon"
localTzName="America/Los_Angeles"
localZoneInfo = ZoneInfo(localTzName)
localLatitude = 44.074278 
localLongitude = -121.270139
localLocationInfo = LocationInfo(localCity, localRegion, localTzName, localLatitude, localLongitude)

#print("Timezone: ", localTzName)
#print("sunset time: ", localSun["sunset"])
#print("dusk time: ", localSun["dusk"])
#print("sunrise time: ", localSun["sunrise"])
#print("current time: ", datetime.now(tz=localZoneInfo))

while True:
    localSun = sun(observer = localLocationInfo.observer, tzinfo=localZoneInfo)

    dtNow = datetime.now(tz=localZoneInfo)
    bedtime = datetime.combine(dtNow.date(), time(20, 0, 0, 0, tzinfo=localZoneInfo))

    if dtNow > localSun["dusk"] and dtNow < bedtime: # am I in between sunset and bedtime?
        os.system('busylight --all on 0xbbffff')
    else:
        os.system('busylight --all off')

    sleep(120)

