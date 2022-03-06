from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class aam181(Page):
    form_model = 'player'
    form_fields = ['Consented', 'IsMobile']

    def error_message(self, values):
        self.participant.vars['is_mobile'] = values['IsMobile']

    def before_next_page(self):
        self.player.Prolific_id = self.participant.label


class abq112(Page):
    pass


page_sequence = [
    aam181,
    abq112
]
