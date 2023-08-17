from PIL import Image
from PIL.ExifTags import TAGS

class Pollen():
    def __init__(self):
        # Basic Pollen properties
        self.pixmap = ""
        self.path = ""
        self.class_ = ""
        self.confidence = 0
        self.comment = ""
        self.user = ""
        self.is_senior = False
        self.metadata = {}
        self.labelled = False
        #-----------Review Properties-----------#
        self.annotation_id = 0
        self.previous_class = ""
        self.previous_confidence = 0
        self.previous_comment = ""
        self.previous_user = ""
        self.previous_is_senior = False
        self.previous_timestamp = ""
        self.reviewer = ""
        self.review_decision = 0
        self.review_comment = ""

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

    def __str__(self):
        attrs = vars(self)
        return (', '.join("%s: %s" % item for item in attrs.items()))


