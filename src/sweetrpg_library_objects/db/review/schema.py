# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow import fields, INCLUDE
from sweetrpg_library_objects.model.review import Review
from sweetrpg_model_core.schema.base import BaseSchema
from sweetrpg_model_core.schema.lang import LangString


class ReviewSchema(BaseSchema):
    model_class = Review

    title = LangString(required=True)  # , load_only=True)
    text = LangString(required=True)  # , load_only=True)
    volume = fields.Str(required=True)
    tags = fields.List(fields.Dict(keys=fields.String(required=True), values=fields.String()))
