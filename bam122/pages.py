import time
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class img_qn_page(Page):
    form_model = 'player'
    form_fields = ['GoodLooking', 'Overweight', 'Fair', 'Masculine', 'Friendly', 'Repentant']

    def is_displayed(self):
        self.player.start_time_per_question = time.time()
        # attention_check_list = self.participant.vars["attention_check_list"]
        # return self.round_number <= Constants.num_rounds and self.round_number not in attention_check_list
        return self.round_number < Constants.num_rounds

    def vars_for_template(self):
        round_number = self.round_number
        img = self.participant.vars["urls"][round_number]
        self.player.normal_pic_url = img
        return dict(
            img='https://images.weserv.nl/?url=' + img,
            round_number=self.round_number,
            is_mobile=self.participant.vars["is_mobile"]
        )

    def before_next_page(self):
        self.player.time_spent_per_question = time.time() - self.player.start_time_per_question


class ac_qn_page(Page):
    form_model = 'player'
    form_fields = []
    qn_ids = random.sample(range(Constants.num_attention_check_qn), k=Constants.num_qn_per_ac)
    print('qn_ids', qn_ids)
    for qn_id in qn_ids:
        form_fields.append('AC_Q' + str(qn_id))

    def is_displayed(self):
        attention_check_list = self.participant.vars["attention_check_list"]
        return self.round_number in attention_check_list

    def vars_for_template(self):
        img = random.sample(self.participant.vars["ac_urls"], k=1)[0]
        self.player.attention_check_pic_url = img
        return dict(
            img=img,
            round_number=self.round_number,
            is_mobile=self.participant.vars["is_mobile"]
        )

    def error_message(self, values):
        num_correct_qn = 0
        for val in values.items():
            qn_name, answer = val
            if answer == Constants.attention_check_answers[qn_name]:
                num_correct_qn += 1
        self.player.AC_QN_Correctness = num_correct_qn / Constants.num_qn_per_ac
        # if we fail one or more questions in attention check round, this ac round should be
        # considered as a failed one, but we have several ac rounds in total
        if not num_correct_qn < Constants.num_qn_per_ac:
            self.player.AC_Correct_Status = True

    def before_next_page(self):
        player_all_rounds = self.player.in_all_rounds()
        self.player.AC_Round_Num = self.round_number
        self.player.AC_QN_Selected = self.form_fields
        num_correct_ac = 0
        for player_all_round in player_all_rounds:
            if (not player_all_round.AC_Round_Num == -1) and player_all_round.AC_Correct_Status:
                num_correct_ac += 1
        self.player.AC_Correctness = num_correct_ac / Constants.num_attention_check
        self.participant.vars['AC_Correctness'] = self.player.AC_Correctness


class result_page(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    img_qn_page,
    ac_qn_page,
    result_page
]
