#from import_export import resources
#from addcsvdataproject.models test
#resources.py
from import_export import resources
from addcsvdataproject.models import test,booth
 
class testResource(resources.ModelResource):
    class Meta:
        model = test

class boothResource(resources.ModelResource):
    class Meta:
        model = booth       