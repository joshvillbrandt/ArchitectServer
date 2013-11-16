import datetime
from flask import url_for
from ArchitectServer import db
#from flask.ext.restful import fields, marshal_with, Resource

class VersionedDocument(db.Document):
    # unversioned - this is duplicated data (its also in the first version as "modified"), but this is probably the only piece of not current-version information that we want readily
    _versions = db.ListField(db.DictField())
    created_by = db.IntField(required=True)
    created_at = db.DateTimeField(required=True)

    # versioned properties
    modified_by = db.IntField(required=True)
    modified_at = db.DateTimeField(required=True)
    deleted = db.BooleanField(required=True, default=False)

    def clean(self):
        """Verifies that we are making a change only to the latest version and
        automatically pushes the new information into the versions list."""

        # set current time
        self.modified_at = datetime.datetime.now

        if id == None:
            # set created_* attributes if this is the first version
            self.created_by = self.modified_by
            self.created_at = self.modified_at
        else:
            # load existing document
            obj = self.objects.get(id=self.id)

            # verify that we are chaing the latest version
            if self.version != len(obj._versions):
                msg = 'The document has been modified since you begin editing it.'
                raise ValidationError(msg)

            # set current time (so we can easily access these properties)

            # push back old version
            ver = {}
            #obj.

            return obj


# class VersionedReference(db.EmbeddedDocument):
#     id = db.ReferenceField(required=True, reverse_delete_rule=db.DENY)
#     version = db.IntField(required=True)

# class ThingOne(VersionedDocument):
#     field_a = db.StringField()

# class ThingTwo(VersionedDocument):
#     field_b = db.StringField()
#     thing_one = db.EmbddedDocumentField(VersionedReference)

# class VersionedResouce(Resource):

    # def get(id, version = None):
    #     obj = self.objects.get(_id = id)

    #     if version == len(self._versions):
    #         del obj._versions
    #         return obj
    #     else:
    #         #TODO
    #         return version

#     def get(self):
#         pass

#     def add_resources(self, base_url, api):
#         api.add_resource(VersionedResourceList,        base_url,                                               endpoint=resource_name + '-list')
#         api.add_resource(VersionedResource,            base_url + '/<ObjectId:obj_id>',                        endpoint=resource_name + '-single');
#         api.add_resource(VersionedResourceVersionList, base_url + '/<ObjectId:obj_id>/versions',               endpoint=resource_name + '-versions');
#         api.add_resource(VersionedResourceVersion,     base_url + '/<ObjectId:obj_id>/versions/<int:version>', endpoint=resource_name + '-version');

#     #.save(cascade=True)
        
# class ThingOneResource(VersionedResouce):


# class ArchitectDocument(db.Document):
#     # at some point inherit from vermongo
#     #version = db.IntField(required=True)
#     #created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
#     #modified = db.DateTimeField(default=datetime.datetime.now, required=True)

#     # _version
#     # _deleted

#     @property
#     def class_name(self):
#         return self.__class__.__name__

#     meta = {
#         'abstract': True
#     }

########################################################################################
# parts
########################################################################################

# class Part(ArchitectDocument):
#     root = db.StringField(max_length=255, required=True)
#     version = db.StringField(max_length=255, required=True)
#     description = db.StringField(max_length=255, required=True)
#     shape_json = db.StringField() # this is for the enclosure
#     depreciated = db.BooleanField(default=False)

#     def __unicode__(self):
#         return self.root + ' ' + self.major_version

########################################################################################
# connectors
########################################################################################

########################################################################################
# channels
########################################################################################

# class ChannelType(ArchitectDocument):
#     name = db.StringField(max_length=255, required=True, unique=True) # like "RS422, Asynchronous"
#     summary = db.StringField()
#     depreciated = db.BooleanField(default=False)
#     def __unicode__(self):
#         return self.name

# class ChannelSignalType(ArchitectDocument):
#     channel_type = db.ReferenceField(ChannelType, reverse_delete_rule=CASCADE)
#     name = db.StringField(max_length=255, required=True) # like "TX-P"
#     order = db.IntField(required=True) # description is always "1"
#     def __unicode__(self):
#         return self.channel_type.__unicode__() + ' [' + self.name + ']'

# class ChannelSignalInstance(models.Model):
#     channel_instance = db.ReferenceField(NativeChannelInstance, reverse_delete_rule=CASCADE)
#     channel_signal_type = db.ReferenceField(ChannelSignalType, reverse_delete_rule=CASCADE)
#     # the signal instance is inherently named by the channel instance name and the channel type signal name
#     #connector_instance = db.ReferenceField(ConnectorInstance, reverse_delete_rule=CASCADE)
#     #connector_contact_instance = db.ReferenceField(ConnectorContactInstance, reverse_delete_rule=CASCADE)
#     def __unicode__(self):
#         return self.channel_instance.__unicode__() + ' ' + self.channel_signal_type.name

########################################################################################
# part instances
########################################################################################

# class PartInstance(ArchitectDocument):
#     parent = db.ReferenceField(Part)
#     part = db.ReferenceField(Part)
#     name = db.StringField(max_length=255, unique=True) # like "mycomponent1"
#     note = db.TextField(blank=True)
#     def __unicode__(self):
#         return self.name

# class ChannelInstance(ArchitectDocument):
#     part = db.StringField(max_length=255, required=True) # should be a foriegn key
#     meta = {
#         'allow_inheritance': True
#     }

# class NativeChannelInstance(ChannelInstance):
#     channel_type = db.StringField(max_length=255, required=True) # should be a foriegn key
#     name = db.StringField(max_length=255, required=True)
#     note = db.StringField()

# class ExposedChannelInstance(ChannelInstance):
#     child_channel = db.StringField(max_length=255, required=True) # should be a foriegn key
#     channel_instance = db.StringField(max_length=255, required=True) # should be a foriegn key

# class PartInstanceChannelInstance(ArchitectDocument):
#     part_instance = db.ReferenceField(PartInstance)
#     channel_instance = db.ReferenceField(ChannelInstance)

# class ChannelMate(ArchitectDocument):
#     part = db.ReferenceField(Part)
#     channels = db.ListField(db.ReferenceField(PartInstanceChannelInstance))

# TODO add notion of a manual channel mate
#AutomaticChannelMate
#ManualChannelMate

