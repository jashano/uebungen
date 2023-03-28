class WGS84Coord():
    def __init__(self,lng=0,lat=0):
        self.setLongitude(lng)
        self.setLatitude(lat)
    
    def setLatitude(self,lat):
        if lat > 90:
            self._lat=lat - lat%180
        elif lat < -90:
            self._lat = lat-lat%180
        else:
            self._lat=lat

    
    def setLongitude(self,lng):
        if lng > 180:
            self._lng=lng - lng%180
        elif lat < -180:
            self._lng = lng-lng%180
        else:
            self._lng=lng

    def getLatitude(self):
        return self._lat

    def getLongitude(self):
        return self._lng

a=WGS84Coord(555,1)