from math import radians, sin, cos, sqrt, atan2

class LongLatToKmConverter:
    #debug values lol
    #testValue1 = [57.14370583, -2.098685386]
    #testValue2 = [53.75297338, -2.369548102]


    def convert(self, lat1, lon1, lat2, lon2):
        location1 = [radians(lat1), radians(lon1)]
        location2 = [radians(lat2), radians(lon2)]

        #change if on Mars
        planetDiam = 6371.0

        distlon = location2[1] - location1[1]
        distlat = location2[0] - location1[0]

        # Haversine formula
        havTheta = sin(distlat / 2)**2 + cos(location1[0]) * cos(location2[0]) * sin(distlon / 2)**2
        theta = 2 * atan2(sqrt(havTheta), sqrt(1 - havTheta))

        distance = planetDiam * theta

        return distance

    # debug code lol
    #print(convert(testValue1[0], testValue1[1], testValue2[0], testValue2[1]))
    