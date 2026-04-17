from PIL import ExifTags, Image
import glob, os


def clearthumbs():
    thumb = str(os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/'))
    filelist = glob.glob(thumb+"*.jpg")
    for f in filelist:
        os.remove(f)


def tviewer(filename, size,rotation):
    thumb = str(os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/thumb'+str(size)+"x"+str(size)+'.jpg'))
    img = Image.open(filename)
    exif = dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
    if (rotation == True):
        try:
            #if exif['Orientation']:
                #img = img.rotate(180, expand=True)
            for tag, value in exif.items():
                decoded = ExifTags.TAGS.get(tag, tag)
                if decoded == 'Orientation':
                    if value == 3: img = img.transpose(Image.ROTATE_180)
                    if value == 6: img = img.transpose(Image.ROTATE_270)
                    if value == 8: img = img.transpose(Image.ROTATE_90)
        except:
            pass
    img.thumbnail((size, size), Image.ANTIALIAS)
    img.save(thumb, "JPEG")

    return thumb
