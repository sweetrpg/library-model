# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_objects.db.volume.document import VolumeDocument
from sweetrpg_library_objects.db.embedded.tag.document import TagDocument
from sweetrpg_library_objects.db.publisher.document import PublisherDocument
from sweetrpg_library_objects.db.system.document import SystemDocument
from sweetrpg_library_objects.db.embedded.property.document import PropertyDocument


def test_volume_document_setup():
    t = TagDocument(name="tag", value="value")
    p = PublisherDocument(name="Pub Lisher")
    pr = PropertyDocument(name="value", value="1", kind="int")
    s = SystemDocument(game_system="dnd", edition="5")
    v = VolumeDocument(
        title="Bob's Book",
        description="Descriptive",
        slug="bob",
        system=s,
        tags=[t],
        publisher=p,
        properties=[pr],
    )
    assert v is not None
    assert v.title == "Bob's Book"
    assert v.description == "Descriptive"
    assert v.slug == "bob"
    assert v.system.game_system == "dnd"
    assert v.publisher.name == "Pub Lisher"
    assert len(v.properties) == 1
    pr = v.properties[0]
    assert pr.name == "value"
    assert pr.value == "1"
    assert pr.kind == "int"
    assert len(v.tags) == 1
    t = v.tags[0]
    assert t.name == "tag"
    assert t.value == "value"
