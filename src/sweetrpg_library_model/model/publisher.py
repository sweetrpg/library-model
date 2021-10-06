# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import logging
from sweetrpg_model_core.model.base import BaseModel


class Publisher(BaseModel):
    """A model object representing RPG publishers."""

    def __init__(self, *args, **kwargs):
        """Creates a new Publisher object.

        :key str name: The name of the publisher.
        """
        logging.debug("args: %s, kwargs: %s", args, kwargs)

        super().__init__(*args, **kwargs)

        self.name = kwargs.get("name")
