import datetime
from flask import url_for
from Architect import db

class ArchitectDocument(db.Document):
    # at some point inherit from vermongo
    # _version
    # _deleted

    @property
    def class_name(self):
        return self.__class__.__name__

    meta = {
        'abstract': True
    }

class ChannelInstance(ArchitectDocument):
    part = db.StringField(max_length=255, required=True) # should be a foriegn key

    meta = {
        'allow_inheritance': True
    }

class NativeChannelInstance(ChannelInstance):
    channel_type = db.StringField(max_length=255, required=True) # should be a foriegn key
    name = db.StringField(max_length=255, required=True)
    note = db.StringField()

class ExposedChannelInstance(ChannelInstance):
    child_channel = db.StringField(max_length=255, required=True) # should be a foriegn key
    channel_instance = db.StringField(max_length=255, required=True) # should be a foriegn key






class Post(db.DynamicDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    slug = db.StringField(max_length=255, required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

class BlogPost(Post):
    body = db.StringField(required=True)


class Video(Post):
    embed_code = db.StringField(required=True)


class Image(Post):
    image_url = db.StringField(required=True, max_length=255)


class Quote(Post):
    body = db.StringField(required=True)
    author = db.StringField(verbose_name="Author Name", required=True, max_length=255)


class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)