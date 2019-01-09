from .abstract_model import AbstractModel


class QuestionModel(AbstractModel):

    def __init__(self, **kwargs):

        super().__init__(questions)
        self.title = kwargs['title']
        self.body = kwargs['body']
        self.votes = kwargs['votes']
        self.question = kwargs['question']
        self.created_by = kwargs['created_by']

    def save(self):
        """
            Saves question instance to the present record
            holding all questions
        """
        questions.append(self)

    def dictify(self):
        """
            Returns a dictionary of the question instance
        """

        return {
            "title": self.title,
            "body": self.body,
            "question": self.question,
            "user": self.tags,
        }

        #
        # Searches

    @classmethod
    def get_all_questions(cls):
        """
            Converts all present question objects to a
            dictionary and sends them in a list envelope
        """
        return [question.dictify() for question in questions]

    @classmethod
    def get_by_id(cls, given_id):
        """
            Searches and returns a question instance
            with an 'id' attribute matching the given id.
            Default return value is None.
        """
        that_question = [question.dictify() for question in questions
                         if getattr(question, 'id') == given_id]

        return that_question[0] if that_question else None

    @classmethod
    def verify_existent(cls, question_object):
        """
            Helps minimize on  questions duplicity.
            Ensures that for each meetup, a question
            isn't re-created with the same data
        """
        return any([question for question in questions
                    if repr(question) == repr(question_object)])

    def __repr__(self):
        return '{title} {tags} {location}'.format(**self.dictify())


questions = []
