"""Definition of the Publication content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from isaw.publications import publicationsMessageFactory as _
from isaw.publications.interfaces import IPublication
from isaw.publications.config import PROJECTNAME

PublicationSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

PublicationSchema['title'].storage = atapi.AnnotationStorage()
PublicationSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    PublicationSchema,
    folderish=True,
    moveDiscussion=False
)


class Publication(folder.ATFolder):
    """An ISAW Publication"""
    implements(IPublication)

    meta_type = "Publication"
    schema = PublicationSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Publication, PROJECTNAME)
