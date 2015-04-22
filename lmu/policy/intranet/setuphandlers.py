# -*- coding: utf-8 -*-

from plone import api

from lmu.policy.intranet.demo_content import content


def importDemoContent(context):
    """Install Demo Content on Portal"""

    if context.readDataFile('lmu.policy.serviceportal_content.txt') is None:
        return

    #return # seems to be called all the time.
    portal = api.portal.get()

    import ipdb; ipdb.set_trace()
    for oid, oval in content.iteritems():
        container = api.content.get(path=oval['path'])
        if oval['type'] == 'Blog Folder':
            folder = api.content.create(
                id=oid,
                type='Blog Folder',
                container=container,
                title=oval['title'],
                description=oval['description']
            )
            state = api.content.transition(obj=folder, to_state='published')
        elif oval['type'] == 'Blog Entry':
            entry = api.content.create(
                id=oid,
                type='Blog Entry',
                container=container,
                title=oval['title'],
                description=oval['description'],
                text=oval['text'],
                image_caption=oval['image_caption']
            )
            state = api.content.transition(obj=entry, to_state='internally_published')


