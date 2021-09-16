# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from marshmallow import post_load
from sweetrpg_library_model.model.studio import Studio
from sweetrpg_common.db.base import BaseDBSchema
import logging


class StudioDBSchema(BaseDBSchema):
    @post_load
    def make_object(self, data, **kwargs):
        logging.info("data: %s", data)
        return Studio(**data)

    name = fields.String(required=True)  # , load_only=True)
