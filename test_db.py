from ArchitectServer.models import *
import datetime

# try listing all versions
print VersionedDocument.objects

doc = VersionedDocument()

print dir(doc)

# try adding a new document
#doc = VersionedDocument()

# try getting current version
#VersionedDocument.get(1)

# try getting first version

# try listing all versions again!
#print VersionedDocument.objects