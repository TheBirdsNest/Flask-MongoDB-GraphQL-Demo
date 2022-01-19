from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

class Region(Document):
    meta = {'collection': 'regions'}
    name = StringField()

class Template(Document):
    meta = {'collection': 'templates'}
    name = StringField()
    region = ReferenceField(Region)
    mpls_count = IntField()
    dia_count = IntField()
    isp_count = IntField()
    high_availability = BooleanField()
