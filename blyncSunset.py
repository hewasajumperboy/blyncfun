from astral import LocationInfo
from astral.sun import sun
import pytz
from datetime import datetime
from zoneinfo import ZoneInfo

localCity="Bend"
localRegion="Oregon"
localTzName="America/Los_Angeles"
localZoneInfo = ZoneInfo(localTzName)
localLatitude = 44.074278 
localLongitude = -121.270139
localLocationInfo = LocationInfo(localCity, localRegion, localTzName, localLatitude, localLongitude)
localTime = datetime.now()

localSun = sun(localLocationInfo.observer, tzinfo=localZoneInfo)

print("Timezone: ", localTzName)
print("sunset time: ", localSun["sunset"])
print("sunrise time: ", localSun["sunrise"])
print("current time: ", localTime)

'''
from astral import LocationInfo
from astral.sun import sun
from datetime import datetime
from time import sleep
import pytz

utc=pytz.UTC

city = LocationInfo("London", "England", "Europe/London", 51.5, -0.116) # swap with your location

while True:

    s = sun(city.observer)
    time_now = utc.localize(datetime.now())
    sunrise = s["sunrise"]
    dusk = s["dusk"]

    if time_now > sunrise and time_now < dusk: # am I in between sunset and dusk?
        print("Daylight")
    else:
        print("Switch on light")

    sleep(60)
'''