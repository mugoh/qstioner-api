from .abstract_model import AbstractModel

rsvps = []


class RsvpModel(AbstractModel):

    def __init__(self, **kwargs):
        super().__init__(rsvps)
        self.user = kwargs['user']
        self.meetup = kwargs['meetup']
        self.response = kwargs['response']
