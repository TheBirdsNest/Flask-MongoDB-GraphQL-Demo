import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType

from models import Template as TemplateModel
from models import Region as RegionModel

class Template(MongoengineObjectType):
    class Meta:
        description = "Template"
        model = TemplateModel
        interfaces = (Node,)

class Region(MongoengineObjectType):
    class Meta:
        description = "Region"
        model = RegionModel
        interfaces = (Node,)

class Query(graphene.ObjectType):
    node = Node.Field()

    templates = MongoengineConnectionField(Template)
    regions = MongoengineConnectionField(Region)

schema = graphene.Schema(query=Query, types=[Template, Region])
