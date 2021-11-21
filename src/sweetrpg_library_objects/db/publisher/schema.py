# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields
from sweetrpg_library_objects.model.publisher import Publisher
from sweetrpg_model_core.schema.base import BaseSchema


class PublisherSchema(BaseSchema):
    model_class = Publisher

    name = fields.String(required=True)  # , load_only=True)
    tags = fields.List(fields.Dict(keys=fields.String(required=True), values=fields.String()))