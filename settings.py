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
            # 'aas140',
            # 'bam122',
            'cdd129'
        ],
        treatment=1,  # page sequence [X, Y, Z]
        completion_link='https://app.prolific.co/submissions/complete?cc=11111111',
        non_completion_link='https://www.prolific.co/'
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
        name='otree_miami',
        display_name='otree miami',
    ),
    dict(
        name='otree_miami_prolific',
        display_name='otree miami prolific',
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

# inactive session configs
### dict(name='trust', num_demo_participants=2, app_sequence=['trust']),
### dict(name='prisoner', num_demo_participants=2, app_sequence=['prisoner']),
### dict(name='ultimatum', num_demo_participants=2, app_sequence=['ultimatum']),
### dict(name='ultimatum_strategy', num_demo_participants=2, app_sequence=['ultimatum'], use_strategy_method=True),
### dict(name='ultimatum_non_strategy', num_demo_participants=2, app_sequence=['ultimatum'], use_strategy_method=False),
### dict(name='vickrey_auction', num_demo_participants=3, app_sequence=['vickrey_auction']),
### dict(name='volunteer_dilemma', num_demo_participants=3, app_sequence=['volunteer_dilemma']),
### dict(name='cournot', num_demo_participants=2, app_sequence=['cournot']),
### dict(name='principal_agent', num_demo_participants=2, app_sequence=['principal_agent']),
### dict(name='dictator', num_demo_participants=2, app_sequence=['dictator']),
### dict(name='matching_pennies', num_demo_participants=2, app_sequence=['matching_pennies']),
### dict(name='traveler_dilemma', num_demo_participants=2, app_sequence=['traveler_dilemma']),
### dict(name='bargaining', num_demo_participants=2, app_sequence=['bargaining']),
### dict(name='common_value_auction', num_demo_participants=3, app_sequence=['common_value_auction']),
### dict(name='bertrand', num_demo_participants=2, app_sequence=['bertrand']),
### dict(name='real_effort', num_demo_participants=1, app_sequence=['real_effort']),
### dict(name='lemon_market', num_demo_participants=3, app_sequence=['lemon_market']),
### dict(name='public_goods_simple', num_demo_participants=3, app_sequence=['public_goods_simple']),
### dict(name='trust_simple', num_demo_participants=2, app_sequence=['trust_simple']),
