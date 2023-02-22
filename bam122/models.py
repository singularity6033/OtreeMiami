import os
import random

import pandas as pd
from jsonfield import JSONField
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)
from pymongo import MongoClient

author = 'Erwin Wong, Zishuo Yang'

doc = """
"""


def make_general_field(trait_n, trait_p, label_string):
    return models.StringField(
        label=label_string,
        choices=[
            "Very {}".format(trait_n),
            trait_n,
            "Slightly {}".format(trait_n),
            "Average/Neutral",
            "Slightly {}".format(trait_p),
            trait_p,
            "Very {}".format(trait_p)
        ],
        widget=widgets.RadioSelect,
        blank=Constants.test_env
    )


def make_felon_extent_field(trait_n, trait_p, norp):
    return make_general_field(trait_n, trait_p, "{}?".format(norp))


def make_attention_check_field(trait_n, trait_p, reqAns):
    return make_general_field(trait_n, trait_p, "{}".format(reqAns))


def random_select_csv(user_id):
    # connect mongodb
    client = MongoClient(
        'mongodb+srv://miami:miami6033626@cluster0.lodffed.mongodb.net/?retryWrites=true&w=majority')
    db = client['miami-database']
    csv_collection = db['csv']
    record_collection = db['record']

    csv_list = ['list_' + str(i + 1) + '.csv' for i in range(697)]

    # in last several sessions the search time will be intensive and may cause request times error
    # this code will try to do random search only on the valid set
    # record_query = {"count": {"$lt": 3}}
    # records = record_collection.find(record_query)
    # csv_names_remained = []
    # for record in records:
    #     csv_names_remained.append(record['name'])
    # random.shuffle(csv_names_remained)
    # selected_csv = csv_names_remained[0]

    selected_csv = random.choice(csv_list)
    query = {"name": selected_csv}
    record = record_collection.find_one(query)
    selected_csv_times = record['count']
    current_users = record['prolific_ids']

    if selected_csv_times < 7:
        # update count value
        current_users.append(user_id)
        new_value_c = {"$set": {
            "count": selected_csv_times + 1,
            "prolific_ids": current_users
        }}
        record_collection.update_one(query, new_value_c)
        urls = csv_collection.find_one(query)['urls']
        # randomly shuffle the sequence of one csv file
        # to make sure urls for each player are different even they are from the same csv list file
        random.shuffle(urls)
        csv_dict = {}
        for i in range(len(urls)):
            csv_dict[i + 1] = urls[i]
        return selected_csv, csv_dict
    else:
        return random_select_csv(user_id)


def get_all_ac_urls():
    urls = []
    names = os.listdir('_static/bam122/static/')
    for name in names:
        urls.append('bam122/static/' + str(name))
    return urls


class Constants(BaseConstants):
    name_in_url = 'bam122'
    players_per_group = None
    test_env = 0
    ImgQnTemplate = "bam122/ImgQnTemplate.html"
    num_rounds = 51  # 50+1 (additional '1' is the end of task for calculating correctness)
    num_attention_check = 5
    num_attention_check_qn = 8
    num_qn_per_normal = 6
    num_qn_per_ac = 3
    attention_check_list = []
    # we select random ac rounds in [1-10], [11-20], ...
    for round_interval in range(1, num_rounds, 10):
        attention_check_list.append(random.sample(range(round_interval, round_interval + 9), k=1)[0])
        # print(attention_check_list)
    attention_check_answers = {"AC_Q0": "Average/Neutral",
                               "AC_Q1": "Exogenous",
                               "AC_Q2": "Versatile",
                               "AC_Q3": "Average/Neutral",
                               "AC_Q4": "Very Aggressive",
                               "AC_Q5": "Dark",
                               "AC_Q6": "Very Overweight",
                               "AC_Q7": "Average/Neutral"}


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            if "urls" in player.participant.vars or 'csv_file_used' in player.participant.vars:
                continue
            player.participant.vars["csv_file_used"], player.participant.vars["urls"] = random_select_csv(user_id=player.participant.label)
            player.participant.vars["ac_urls"] = get_all_ac_urls()
            player.participant.vars["attention_check_list"] = Constants.attention_check_list.copy()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # normal questions
    GoodLooking = make_felon_extent_field("Ugly-looking", "Good-looking", "Ugly looking or Good looking")
    Overweight = make_felon_extent_field("Underweight", "Overweight", "Underweight or Overweight")
    Fair = make_felon_extent_field("Dark", "Fair", "Dark or Fair")
    Masculine = make_felon_extent_field("Feminine", "Masculine", "Feminine or Masculine")
    Friendly = make_felon_extent_field("Aggressive", "Friendly", "Aggressive or Friendly")
    Repentant = make_felon_extent_field("Repentant", "Unrepentant", "Repentant or Unrepentant")

    # attention check questions
    AC_Q0 = make_attention_check_field("Unscientific", "Scientific", "Average/Neutral")
    AC_Q1 = make_attention_check_field("Exogenous", "Endogenous", "Exogenous")
    AC_Q2 = make_attention_check_field("Unversatile", "Versatile", "Versatile")
    AC_Q3 = make_attention_check_field("Repentant", "Unrepentant", "Average/Neutral")
    AC_Q4 = make_attention_check_field("Aggressive", "Friendly", "Very Aggressive")
    AC_Q5 = make_attention_check_field("Dark", "Fair", "Dark")
    AC_Q6 = make_attention_check_field("Underweight", "Overweight", "Very Overweight")
    AC_Q7 = make_attention_check_field("Feminine", "Masculine", "Average/Neutral")

    # attention check related attributes
    AC_QN_Selected = JSONField(default=[])
    AC_QN_Correctness = models.FloatField(default=0)
    AC_Round_Num = models.IntegerField(default=-1)
    AC_Correct_Status = models.BooleanField(default=False)
    AC_Correctness = models.FloatField(default=0)

    # start time
    start_time_per_question = models.FloatField(blank=True)
    # how long subjects take to finish one question (in seconds)
    time_spent_per_question = models.FloatField(blank=True)

    # csv_file
    csv_file_used = models.LongStringField(initial=0)

    # urls used for normal rounds and attention check rounds
    normal_pic_url = models.LongStringField(initial=0)
    attention_check_pic_url = models.LongStringField(initial=0)
