from astral import LocationInfo
from astral.sun import sun
import pytz
from datetime import datetime
from zoneinfo import ZoneInfo
from time import sleep

localCity="Bend"
localRegion="Oregon"
localTzName="America/Los_Angeles"
localZoneInfo = ZoneInfo(localTzName)
localLatitude = 44.074278 
localLongitude = -121.270139
localLocationInfo = LocationInfo(localCity, localRegion, localTzName, localLatitude, localLongitude)

localSun = sun(observer = localLocationInfo.observer, tzinfo=localZoneInfo)

print("Timezone: ", localTzName)
print("sunset time: ", localSun["sunset"])
print("dusk time: ", localSun["dusk"])
print("sunrise time: ", localSun["sunrise"])
print("current time: ", datetime.now(tz=localZoneInfo))

while True:
    localSun = sun(localLocationInfo.observer, tzinfo=localZoneInfo)

    dtNow = datetime.now(tz=localZoneInfo)
    bedtime = (dtNow.date(), (20, 0, 0, 0))

    if dtNow > localSun["dusk"] and dtNow < bedtime: # am I in between sunset and bedtime?
        print("Daylight")
    else:
        print("Switch on nightlight")

    sleep(10)

