class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        altitude = 0
        for i in gain:
            altitude += i
            if altitude > highest: highest = altitude
        return highest