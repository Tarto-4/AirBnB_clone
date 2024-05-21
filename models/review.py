#!/usr/bin/python3
"""
Module that creates review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class representing a Review
    """

    place_id = str
    user_id = str
    text = str

    def __init__(self, *args, **kwargs):
