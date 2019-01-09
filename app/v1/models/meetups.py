"""
    Holds the model for the meetup resource
"""

from app.v1.models.abstract_model import AbstractModel

meetups = []  # Holds all meetups records


class MeetUpModel(AbstractModel):

    def __init__(self, **kargs):

        super().__init__(meetups)
        self.location = kargs.get('location')
        self.images = kargs.get('images')
        self.topic = kargs.get('topic')
        self.happeningOn = kargs.get('happeningOn')
        self.tags = kargs.get('tags')
