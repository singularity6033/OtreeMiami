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


author = 'Erwin Wong'

doc = """
Survey.
"""


def set_scale_choices_list(length):
    choices_list = []
    for i in range(length):
        choices_list.append((i + 1, str(i + 1)))
    return choices_list


def make_scale_field(label_string, length):
    return models.FloatField(
        choices=set_scale_choices_list(length),
        widget=widgets.RadioSelectHorizontal,
        label=label_string,
        blank=Constants.test_env
    )


class Constants(BaseConstants):
    name_in_url = 'cdd129'
    players_per_group = None
    num_rounds = 1
    test_env = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    GameTheoryFamiliar = models.IntegerField(
        choices=[
            [1, "Yes"],
            [0, "No"]
        ],
        label="Are you familiar with game theory?",
        widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    AgeCategory = models.StringField(
        choices=[
            "20 and younger",
            "20 - 29",
            "30 - 39",
            "40 - 49",
            "50 - 59",
            "60 and older"
        ],
        label="Which category below includes your age?",
        # widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    Gender = models.StringField(
        choices=[
            "Male",
            "Female",
            "I prefer not to answer",
            "Other"
        ],
        label="What is your gender?",
        widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    RaceEthnicity = models.StringField(
        choices=[
            "White or Caucasian",
            "Black or African American",
            "Native American or American Indian",
            "Hispanic or Latino",
            "Asian or Pacific Islander",
            "Others or Multiracial"
        ],
        label="What is your race/ethnicity?",
        # widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    MaritalStatus = models.StringField(
        choices=[
            "Single and never married",
            "Cohabiting (or Domestic Partnership)",
            "Married",
            "Widowed",
            "Divorced",
            "Separated"
        ],
        label="What is your marital status?",
        # widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    NumChildren = models.StringField(
        choices=[
            "None",
            "1",
            "2",
            "3",
            "4",
            "5 or more"
        ],
        label="Do you have any children aged from 0 to 17 living at home with you, or to whom you have regular "
              "responsibility for? If so, how many?",
        # widget=widgets.RadioSelect,
        blank=Constants.test_env
    )
    # Next page
    Employment = models.StringField(
        choices=[
            "Employed for wages",
            "Self-employed",
            "Out of work and looking for work",
            "Out of work but not currently looking for work",
            "Homemaker",
            "Student",
            "Military",
            "Retired",
            "Unable to work"
        ],
        label="What is your current employment status?",
        # widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    PoliticalOrientation = models.StringField(
        choices=[
            "Very liberal",
            "Slightly liberal",
            "Neutral",
            "Slightly conservative",
            "Very conservative"
        ],
        label="What is your political orientation?",
        widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    PoliticalParty = models.StringField(
        choices=[
            "Democratic Party",
            "Republican Party",
            "Independent",
            "None of the above",
            "I prefer not to say"
        ],
        label="Which political party do you support?",
        widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    Education = models.StringField(
        choices=[
            "No schooling completed",
            "Nursery school to 8th grade",
            "Some high school, no diploma",
            "High school graduate, diploma or equivalent",
            "Some college, have a diploma but no degree",
            "College degree",
            "Master degree",
            "Doctorate (Ph.D)"
        ],
        label="What is the highest level of education you have completed?",
        # widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    MedicalConditions = models.StringField(
        label="Do you have any existing medical conditions prior to the COVID-19 pandemic? If so, please state them."
              " If not, please write \"None\".",
        blank=Constants.test_env
    )

    Residence = models.StringField(
        choices=[
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming"
        ],
        label="In which state do you currently reside?",
        blank=Constants.test_env
    )

    HouseholdIncome = models.StringField(
        choices=[
            "Less than $10,000",
            "$10,000 - $19,999",
            "$20,000 - $29,999",
            "$30,000 - $39,999",
            "$40,000 - $49,999",
            "$50,000 - $59,999",
            "$60,000 - $69,999",
            "$70,000 - $79,999",
            "$80,000 - $89,999",
            "$90,000 - $99,999",
            "$100,000 - $124,999",
            "$125,000 - $149,999",
            "$150,000 and above"
        ],
        label="Which category includes your entire household income in the previous year before taxes?",
        # widget=widgets.RadioSelect,
        blank=Constants.test_env
    )

    InstructionsEasy = make_scale_field("The instructions for each section were easy to understand.", 7)
    QuestionsEasy = make_scale_field("The questions in each section were easy to understand.", 7)
    Discomfort = make_scale_field("The images in the experiment were discomforting.", 7)

    DifficultyComment = models.StringField(
        label="Please indicate any part(s) of the experiment which you found difficult to understand."
              " If there are none, please write \"None\".",
        blank=Constants.test_env
    )

    Feedback = models.StringField(
        label="We value the feedback of all our participants. Please leave any comments you may have about the"
              " experiment. If you do not wish to comment, please write \"None\".",
        blank=Constants.test_env
    )

    def vars_for_template(self, other_identity):
        mask_wearer = self.participant.vars["MaskWearer"]
        own_identity = "mask wearer" if mask_wearer == 1 else "non-mask wearer"

        return(dict(
            own_identity=own_identity,
            other_identity=other_identity,
            range=Constants.BeliefsRange,
            FOB_ECU=Constants.FOB_ECU,
            SOB_ECU=Constants.SOB_ECU
        ))
    pass
