from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class caa122(Page):
    form_model = 'player'
    form_fields = [
        "AgeCategory",
        "Gender",
        "RaceEthnicity",
        "MaritalStatus",
        "NumChildren"
    ]
    pass


class cab213(Page):
    form_model = 'player'
    form_fields = [
        "Employment",
        "PoliticalOrientation",
        "PoliticalParty",
        "Education",
        # "MedicalConditions",
        "Residence",
        "HouseholdIncome",
    ]
    pass


class cbb239(Page):
    form_model = 'player'
    form_fields = [
        "InstructionsEasy",
        "QuestionsEasy",
        "Discomfort",
        "DifficultyComment",
        "Feedback"
    ]


class cty731(Page):
    def is_displayed(self):
        return self.participant.vars['AC_Correctness'] >= 0.5

    def vars_for_template(self):
        if self.participant.vars['AC_Correctness'] >= 0.5:
            self.player.attention_check_pass = True
        return dict(
            completionlink=self.player.subsession.session.config['completion_link']
        )


class ac_failed_page(Page):
    def is_displayed(self):
        return self.participant.vars['AC_Correctness'] < 0.5

    def vars_for_template(self):
        if self.participant.vars['AC_Correctness'] < 0.5:
            self.player.attention_check_pass = False
        return dict(
            acfailedlink=self.player.subsession.session.config['ac_failed_link']
        )


page_sequence = [
    caa122,
    cab213,
    cbb239,
    cty731,
    ac_failed_page
]
