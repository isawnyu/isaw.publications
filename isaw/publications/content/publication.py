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

    atapi.ImageField(
    name='publication_Logo',
    widget=atapi.ImageWidget(
        label=u'Publication Logo',
        description=_(u'publication_logo', default=u'Optional image associated with this publication.'),
        label_msgid='ISAW_Publication_logo',
        il8n_domain='ISAW_Publications',
        ),

    required=False,
    searchable=False),


    atapi.FileField(
    name='publication_File',
    widget=atapi.FileWidget(
        label=u'Publication file',
        description=_(u'publication_file', default=u'Optional file that contains the publication.'),
        label_msgid='ISAW_Publication_file',
        il8n_domain='ISAW_Publications',
        ),

    required=False,
    searchable=False),


    atapi.TextField(
    name='publication_Information',
    widget=atapi.RichWidget(
        label=u'Publication Information',
        description=_(u'publication_info', default=u'Publication information.'),
        label_msgid='ISAW_Publication_info',
        il8n_domain='ISAW_Publications',
        ),

    required=False,
    searchable=False),

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
