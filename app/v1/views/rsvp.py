"""
    This module contains resource views for the
    rsvp Resource
"""

from flask_restful import Resource

from app.v1.models.rsvp import RsvpModel


class Rsvps(Resource):
