from PIL import Image, ExifTags

def Get_Metadata(image_path):
    """
    Generate a caption for an image using its metadata and a specific caption.

    :param image_path: Path to the image
    :param specific_caption: Specific caption to add
    :return: Generated caption
    """
    img = Image.open(image_path)
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    Metadata = input("Put Metadata into the image ? (y/n)")
    if Metadata.lower() == "y":
        GPS = input("Put GPS information ? (y/n) \t")
        if GPS.lower() == "y":
            if "GPSInfo" in exif:
                GPS_info = exif["GPSInfo"]

                # Convert latitude and longitude to degrees
                lat = convert_to_degrees(GPS_info[2])
                lon = convert_to_degrees(GPS_info[4])
                lat_ref = GPS_info[1]
                lon_ref = GPS_info[3]

                # Adjust the sign of the coordinates based on the reference (N/S, E/W)
                if lat_ref != "N":
                    lat = -lat
                if lon_ref != "E":
                    lon = -lon

                # Format the GPS coordinates into a human-readable string
                geo_coordinate = "{0}° {1}, {2}° {3}".format(lat, lat_ref, lon, lon_ref)
            else:
                geo_coordinate = "No GPS info"
        else:
            geo_coordinate = "No GPS info"

        if 'Model' in exif:
            Camera = '\nCamera: ' + str(exif['Model'])
        else:
            Camera = '\nCamera: N/A'

        if 'LensModel' in exif:
            Lens = ' || LensModel: ' + str(exif['LensModel'])
        else:
            Lens = ' || LensModel: N/A'

        if 'DateTimeOriginal' in exif:
            DateTimeOriginal = exif['DateTimeOriginal']
        else:
            DateTimeOriginal = 'N/A'

        if 'FocalLength' in exif:
            FocalLength = '\nFocal length: ' +exif['FocalLength']
        else:
            FocalLength = '\nFocal length: N/A'

        if 'ExposureTime' in exif:
            ExposureTime = '\nExposure time: 1/' + str(exif['ExposureTime'].denominator)
        else:
            ExposureTime = '\nExposure time: N/A'

        if 'ISOSpeedRatings' in exif:
            ISO = ' || ISO: ' + str(exif['ISOSpeedRatings'])
        else:
            ISO = ' || ISO: N/A'

        if 'FNumber' in exif:
            FNumber = ' || FNumber: f/' + str(exif['FNumber'])
        else:
            FNumber = ' || FNumber: N/A'

        caption = 'Date and Time: '+ DateTimeOriginal + ' | GPS Location : ' + geo_coordinate + Camera + Lens + FocalLength + ExposureTime + ISO + FNumber
    else:
        caption = 'No MetaData'
    return caption

def convert_to_degrees(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degrees in float format.

    Args:
        value (tuple): The GPS coordinate as a tuple (degrees, minutes, seconds)

    Returns:
        float: The coordinate in degrees
    """
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)