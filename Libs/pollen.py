from PIL import Image
from PIL.ExifTags import TAGS

class Pollen():
    def __init__(self):
        # Basic Pollen properties
        self.pixmap = ""
        self.path = ""
        # self.path = "C:/users/horva/Pictures/IMG_1234.jpeg"
        self.class_ = ""
        self.confidence = 0
        self.comment = ""
        self.user = ""
        self.is_senior = False
        self.metadata = {}


    def get_image_metadata(self):
        self.image = Image.open(self.path)
        exifdata = self.image.getexif()
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            self.metadata[tag] = data


