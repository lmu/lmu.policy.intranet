# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys

from plone import api
from plone.app.textfield.value import RichTextValue
from plone.namedfile import NamedBlobImage

from zExceptions import BadRequest

from lmu.policy.intranet.config import required_groups
from lmu.policy.intranet.demo_content import content


def setupVarious(context):
    """Install all additional Things that can't be done via Generic Setup
    """

    if context.readDataFile('lmu.policy.intranet_default.txt') is None:
        return

    #portal = apit.portal.get()
    gtool = api.portal.get_tool(name='portal_groups')
    groups = api.group.get_groups()
    for gid, gdata in required_groups.iteritems():
        if not gid in groups:
            api.group.create(
                groupname=gid,
                title=gdata['title'],
                roles=gdata['roles'],
                description=gdata['description']
            )
        else:
            gtool.editGroup(
                gid,
                title=gdata['title'],
                roles=gdata['roles'],
                description=gdata['description']
            )


def importDemoContent(context):
    """Install Demo Content on Portal"""

    if context.readDataFile('lmu.policy.intranet_demo-content.txt') is None:
        return

    #return # seems to be called all the time.
    #portal = api.portal.get()

    for elem in content:
        (oid, oval) = elem
        try:
            container = api.content.get(path=oval['path'])
            if oval['type'] == 'Blog Folder':
                folder = api.content.create(
                    id=oid,
                    type='Blog Folder',
                    container=container,
                    title=oval['title'],
                    description=oval['description']
                )
                api.content.transition(obj=folder, to_state='published')
            elif oval['type'] == 'Blog Entry':
                imageFile = context.openDataFile(os.path.dirname(__file__) + '/' + oval['image'], 'images') if oval['image'] else None
                entry = api.content.create(
                    id=oid,
                    type='Blog Entry',
                    container=container,
                    title=oval['title'],
                    description=oval['description'],
                    text=RichTextValue(oval['text'], 'text/html', 'text/html'),
                    image=NamedBlobImage(data=imageFile.read()) if imageFile else '',
                    image_caption=oval['image_caption']
                )
                import ipdb; ipdb.set_trace()
                api.content.transition(obj=entry, to_state='internally_published')
            elif oval['type'] == 'Folder':
                folder = api.content.create(
                    id=oid,
                    type='Folder',
                    container=container,
                    title=oval['title'],
                    description=oval['description']
                )
                api.content.transition(obj=folder, to_state='published')
        #except AttributeError as e:
        #    print(sys.exc_info()[0])
        except BadRequest as e:
            print(e.message)
        except Exception as e:
            print(e.message)
        #except:
            print(sys.exc_info()[0])
            import ipdb; ipdb.set_trace()
