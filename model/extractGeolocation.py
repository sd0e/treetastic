import os
from PIL import Image
from PIL.ExifTags import TAGS

# source: https://medium.com/@osah.dilshan/how-to-extract-gps-data-from-images-using-python-9c09254bc80e

# takes an image file location and returns the coordinates in the form
# [latitude, longitude]
# returns [0.0, 0.0] if they could not be found
def extractGeolocation(imageLocation):
    imageObject = Image.open(imageLocation)

    exif = {}
    if imageObject._getexif() is not None:
        for tag, value in imageObject._getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]] = value

    if "GPSInfo" in exif:
        gps_info = exif["GPSInfo"]

        def convert_to_degrees(value):
            d = float(value[0])
            m = float(value[1])
            s = float(value[2])
            return d + (m / 60.0) + (s / 3600.0)

        lat = convert_to_degrees(gps_info[2])
        lon = convert_to_degrees(gps_info[4])
        lat_ref = gps_info[1]
        lon_ref = gps_info[3]

        if lat_ref != "N":
            lat = -lat
        if lon_ref != "E":
            lon = -lon

        return [lat, lon]
    else:
        return [0.0, 0.0]