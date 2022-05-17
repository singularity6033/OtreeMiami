from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Erwin Wong, Zishuo Yang'

doc = """
"""


class Constants(BaseConstants):
    name_in_url = 'aas140'
    num_rounds = 1
    test_env = 0
    players_per_group = None

    # PDExplanation = "aas140/PDExplanation.html"
    # PDTable = "aas140/PDTable.html"
    # PDExplanationText = "aas140/PDExplanationText.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Consented = models.BooleanField()
    IsMobile = models.IntegerField()
    Prolific_id = models.StringField(default=str(" "))
