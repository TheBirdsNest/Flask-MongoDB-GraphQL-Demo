import os
import yaml

from mongoengine import connect
from models import Template, Region

__DATABASE = 'templates'
__PASSWORD = os.environ.get("MONGO_DEVELOPER_PASSWORD")

__client = connect(
    __DATABASE,
    host=f"mongodb+srv://developer:{__PASSWORD}@devcluster.25vmv.mongodb.net/{__DATABASE}?retryWrites=true&w=majority",
    alias="default"
)

def insert(model: str) -> None:

    with open("sample.yml", "r") as file:
        data = yaml.load(file.read(), yaml.Loader)

        for row in data[model]:
            if model == 'templates':
                template = Template(
                    name=row['name'],
                    region=row['region'],
                    mpls_count=row['mpls_count'],
                    isp_count=row['isp_count'],
                    dia_count=row['dia_count'],
                    high_availability=row['high_availability']
                )
                template.save()
            elif model == 'regions':
                region = Region(
                    name=row['name']
                )
                region.save()

insert('regions')
insert('templates')
