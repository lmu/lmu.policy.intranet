# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys

from DateTime import DateTime

from plone import api
from plone.app.textfield.value import RichTextValue
from plone.namedfile import NamedBlobImage

from zExceptions import BadRequest

from lmu.policy.intranet.config import base_content
from lmu.policy.intranet.config import required_groups

from lmu.policy.intranet.demo_content import demo_users
from lmu.policy.intranet.demo_content import demo_blog_entries
from lmu.policy.intranet.demo_content import demo_polls
from lmu.policy.intranet.demo_content import demo_pinnwand_entries


def setupVarious(context):
    """Install all additional Things that can't be done via Generic Setup
    """

    if context.readDataFile('lmu.policy.intranet_default.txt') is None:
        return

    _setupGroups(context)
    _setupBaseContent(context)


def _setupGroups(context):
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


def _setupBaseContent(context):
    for oid, oval in base_content.iteritems():
        try:
            container = api.content.get(path=oval['path'])
            if not oid in container.keys():
                folder = api.content.create(
                    id=oid,
                    container=container,
                    type=oval['type'],
                    title=oval['title'],
                    description=oval['description'],
                    text=oval['text']
                )
            else:
                folder = container.get(oid)
                folder.title = oval['title']
                folder.description = oval['description']
                folder.text = oval['text']
            api.content.transition(obj=folder, to_state='published')
        except BadRequest as e:
            print(e.message)
        except Exception as e:
            print(e.message)


def importDemoContent(context):
    """Install Demo Content on Portal"""

    if context.readDataFile('lmu.policy.intranet_demo-content.txt') is None:
        return

    #return # seems to be called all the time.
    #portal = api.portal.get()
    _setupDemoUsers(context)
    _setupDemoBlogEntries(context)
    #_setupDemoPolls(context)
    _setupDemoPinnwandEntries(context)


def _setupDemoUsers(context):
    all_users = [user.id for user in api.user.get_users()]
    for uid, udata in demo_users.iteritems():
        if uid not in all_users:
            try:
                api.user.create(
                    email=udata['email'],
                    username=uid,
                    password=udata['password'],
                    roles=udata['roles'],
                    properties=udata['properties']
                )
            except BadRequest as e:
                print(e.message)
            except Exception as e:
                print(e.message)


def _setupDemoBlogEntries(context):
    for oid, oval in demo_blog_entries.iteritems():
        try:
            container = api.content.get(path=oval['path'])
            if oid in container:
                continue
            imageFile = context.openDataFile(os.path.dirname(__file__) + '/' + oval['image'], 'images') if oval['image'] else None
            entry = api.content.create(
                id=oid,
                type='Blog Entry',
                container=container,
                title=oval['title'],
                description=oval['description'],
                text=RichTextValue(oval['text'], 'text/html', 'text/html'),
                image=NamedBlobImage(data=imageFile.read()) if imageFile else '',
                image_caption=oval['image_caption'],
                creators=(oval['author'],),
            )
            api.content.transition(obj=entry, to_state='internally_published')
            entry.modification_date = DateTime(oval['modification_date'])
        except BadRequest as e:
            print(e.message)
        except Exception as e:
            print(e.message)


def _setupDemoPolls(context):
    for oid, oval in demo_polls.iteritems():
        try:
            container = api.content.get(path=oval['path'])
            if oid in container:
                continue
            entry = api.content.create(
                id=oid,
                type='Poll',
                container=container,
                title=oval['title'],
                description=oval['description'],
                creators=(oval['author'],),
            )
            api.content.transition(obj=entry, to_state='internally_published')
            entry.modification_date = DateTime(oval['modification_date'])
        except BadRequest as e:
            print(e.message)
        except Exception as e:
            print(e.message)
            #import ipdb; ipdb.set_trace()


def _setupDemoPinnwandEntries(context):
    for oid, oval in demo_pinnwand_entries.iteritems():
        try:
            container = api.content.get(path=oval['path'])
            if oid in container:
                continue
            imageFile = context.openDataFile(os.path.dirname(__file__) + '/' + oval['image'], 'images') if oval['image'] else None
            entry = api.content.create(
                id=oid,
                type='Pinnwand Entry',
                container=container,
                title=oval['title'],
                #description=oval.get('description', ''),
                text=RichTextValue(oval['text'], 'text/html', 'text/html'),
                image=NamedBlobImage(data=imageFile.read()) if imageFile else '',
                image_caption=oval['image_caption'],
                creators=(oval['author'],),
            )
            api.content.transition(obj=entry, to_state='internally_published')
            entry.modification_date = DateTime(oval['modification_date'])
        except BadRequest as e:
            print(e.message)
        except Exception as e:
            print(e.message)
            import ipdb; ipdb.set_trace()
