from os import environ

SESSION_CONFIGS = [
    dict(
        name='combination',
        display_name="Combined experiment",
        app_sequence=['combination', 'fernandes_fin_lit', 'questionnaires'],
        num_demo_participants=4
    ),
    # dict(
    #     name='questionnaires',
    #     display_name="Demographics / common questions",
    #     app_sequence=['questionnaires'],
    #     num_demo_participants=4
    # ),
    # dict(
    #     name='fernandes',
    #     display_name="Fernandes et al. 2014 - Financial Literacy",
    #     app_sequence=['fernandes_fin_lit'],
    #     num_demo_participants=4
    # )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4730327570942'

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
        use_secure_urls=False
    ),
    dict(
        name='econ_lab',
        display_name='Experimental Economics Lab'
    ),
]