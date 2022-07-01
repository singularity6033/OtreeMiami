import os
import random
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


def random_select_csv():
    # connect mongodb
    client = MongoClient(
        'mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
    db = client['test-database']
    csv_collection = db['csv']
    record_collection = db['record']
    # session_collection = db['session']

    # session_query = {"name": session_code}
    # session_record = session_collection.find_one(session_query)
    # if session_record:
    #     num_csv_per_session = session_record['num']
    # else:
    #     session_in_db = {
    #         "name": session_code,
    #         "num": 0,
    #     }
    #     session_collection.insert_one(session_in_db)
    #     num_csv_per_session = 0

    # if num_csv_per_session >= 174:
    #     csv_list = []
    #     for x in record_collection.find({"session_code": session_code}):
    #         if x['count'] < 3:
    #             csv_list.append(x['name'])
    # else:
    #     csv_list = []
    #     for x in record_collection.find({"session_code": -1}):
    #         csv_list.append(x['name'])

    csv_list = ['list_' + str(i + 1) + '.csv' for i in range(697)]

    selected_csv = random.choice(csv_list)
    # print(selected_csv)
    query = {"name": selected_csv}
    record = record_collection.find_one(query)
    selected_csv_times = record['count']
    # session_code_in_db = record['session_code']

    if selected_csv_times < 3:
        # update count value
        new_value_c = {"$set": {
            "count": selected_csv_times + 1,
            # "session_code": session_code
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
        # if session_code_in_db == -1:
        #     if num_csv_per_session < 174:
        #         # update session count value
        #         new_value_s = {"$set": {
        #             "name": session_code,
        #             "num": num_csv_per_session + 1
        #         }}
        #         session_collection.update_one(session_query, new_value_s)
        #     else:
        #         # exceed the maximum num of csv files per session
        #         return random_select_csv(session_code)
        # elif not session_code_in_db == session_code:
        #     # wrong session code
        #     return random_select_csv(session_code)
    else:
        # exceed the maximum num of replication
        return random_select_csv()


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
            # print(self.session.code)
            player.participant.vars["csv_file_used"], player.participant.vars["urls"] = random_select_csv()
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
