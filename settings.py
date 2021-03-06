from os import environ
import os

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

STATIC_URL = '/_static/'
SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

SESSION_CONFIGS = [
    dict(
        name='Otree_Miami',
        display_name='Otree Miami',
        num_demo_participants=None,
        app_sequence=[
            'aas140',
            'bam122',
            'cdd129'
        ],
        treatment=1,  # page sequence [X, Y, Z]
        completion_link='https://app.prolific.co/submissions/complete?cc=3E55FFEE',
        ac_failed_link='https://app.prolific.co/submissions/complete?cc=132E2332'
    )
]
# see the end of this file for the inactive session configs


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ROOMS = [
    dict(
        name='otree_miami_08',
        display_name='oTree Miami GMT-08',
    ),
    dict(
        name='otree_miami_07',
        display_name='oTree Miami GMT-07',
    ),
    dict(
        name='otree_miami_06',
        display_name='oTree Miami GMT-06',
    ),
    dict(
        name='otree_miami_05',
        display_name='oTree Miami GMT-05',
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = 'pihjpwj63+h$v)!)#fu1@a+^r$xx3f&yzue1rmsz)=h_rpaxnw'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
