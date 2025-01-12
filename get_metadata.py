from PIL import Image, ExifTags

def Get_Metadata(image_path):
    img = Image.open(image_path)
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    caption = 'Model: Camera: ' + str(exif['Model']) + '\t||Lens: ' + str(exif['LensModel']) + '\nFocal length: ' + str(exif['FocalLength']) + '\nExposure Time:' + str(exif['ExposureTime']) +'| Iso: ' + str(exif['ISOSpeedRatings']) + '| F number: f/' + str(exif['FNumber'])
    return caption