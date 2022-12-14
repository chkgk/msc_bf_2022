
from otree.api import *
c = cu

import random

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Questionaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    
    
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    
    iban = models.StringField(required=True, label="Your IBAN:")
    iban_repeat = models.StringField(required=True, label="Your IBAN (repeat):")
    name = models.StringField(required=True, label="Your name:")
    
    F1111 = models.StringField(blank=True, label='1. In your own words describe what an ETF is, if you do not know'
                                                 ' answer with "Do not know"')
    F1 = models.IntegerField(choices=[[1, 'More than today with the money in this account'], [2, 'Exactly the same as'
    ' today with the money in this account'], [3, 'Less than today with the money in this account'],
    [4, 'I do not know'], [5, 'I do not want to answer this question']], label='2. Imagine that the interest rate on '
    'your savings account is 1% per year and inflation is 2% per year. After 1 year would you be able to buy:',
                             widget=widgets.RadioSelect)
    F2 = models.IntegerField(choices=[[1, 'True'], [2, 'False'], [3, 'I do not know'],
    [4, 'I do not want to answer this question']], label='3. "Bonds are normally riskier than stocks." Do you think the'
    ' statement is true or false?', widget=widgets.RadioSelect)
    F3 = models.IntegerField(choices=[[1, 'A savings account'], [2, 'Stocks'], [3, 'Bonds'], [4, 'I do not know'],
    [5, 'I do not want to answer']], label='4. Considering a long time period (e.g. 10 or 20 years), which asset '
    'described below normally yields the highest return?', widget=widgets.RadioSelect)
    F4 = models.IntegerField(choices=[[1, 'A savings account'], [2, 'Stocks'], [3, 'Bonds'], [4, 'I do not know'],
    [5, 'I do not want to answer']], label='5. Normally, which asset described below displays the highest fluctuations'
    ' over time?', widget=widgets.RadioSelect)
    F5 = models.IntegerField(choices=[[1, 'Increase'], [2, 'Decrease'], [3, 'Stay the same'], [4, 'I do not know'],
    [5, 'I do not want to answer']], label='6. If an investor spreads his money among different assets, does the risk'
                                           ' of losing a lot of money:', widget=widgets.RadioSelect)
    F55 = models.StringField(choices=[[1, 'A'], [2, 'B'], [3, 'C'], [4, 'I do not know'], [5, 'I do not want to answer']],
                             label='7. Please choose option C',widget=widgets.RadioSelect)
    F6 = models.IntegerField(choices=[[1, 'True'], [2, 'False'], [3, 'I do not know'], [4, 'I do not want to answer']],
                             label='8. "If you invest €1,000 in stocks , would it be possible to have less than €1,000'
    ' if you want to sell the stocks again?" Do you think this statement is true or false?', widget=widgets.RadioSelect)
    F7 = models.IntegerField(choices=[[1, 'True'], [2, 'False'], [3, 'I do not know'], [4, 'I do not want to answer']],
    label='9. "A stock mutual fund combines the money of many investors to buy a variety of stocks." Do you think the'
    ' statement is true or false?', widget=widgets.RadioSelect)
    F8 = models.IntegerField(choices=[[1, 'True'], [2, 'False'], [3, 'I do not know'], [4, 'I do not want to answer']],
    label='10. "A 15-year mortgage typically requires higher monthly interest payments than a 30-year mortgage, but the'
    ' total interest paid over the life of the loan will be less." Do you think this statement is true or false?',
                             widget=widgets.RadioSelect)
    F9 = models.IntegerField(choices=[[1, 'More than €200'], [2, 'Exactly €200'], [3, 'Less than €200'],
    [4, 'I do not know'], [5, 'I do not want to answer']], label='11. Suppose you have €100 in a savings account and'
    ' the interest rate is 20% per year and you never withdraw money or interest payments. After 5 years, how much would'
                                                    ' you have in this account in totalt?', widget=widgets.RadioSelect)
    F10 = models.IntegerField(choices=[[1, 'He owns a part of Firm B'], [2, 'He has lent money to Firm B'],
    [3, "He is liable for Firm B's debts"], [4, 'None of the above'], [6, 'I do not know'],
    [5, 'I do not want to answer']], label='12. Which of the following statements is correct? If somebody buys a bond'
                                           ' of Firm B:', widget=widgets.RadioSelect)
    F101 = models.IntegerField(choices=[[1, 'Less than 5 years'], [2, 'Between 5 and 10 years'],
                                       [3, "Between 10 and 15 years"], [4, 'Never'],
                                       [6, 'I do not know'],
                                       [5, 'I do not want to answer']],
                              label='13. Suppose you owe €3,000 on your credit card. You pay a minimum payment of €30 '
    'each month. At an annual percentage rate of 12% (or 1% per month), how many years would it take to eliminate your'
    'credit card debt if you made no additional new charges?', widget=widgets.RadioSelect)
    F1112 = models.IntegerField(label='14. Imagine that we roll a fair, six-sided die 1,000 times. Out of 1,000 rolls, how'
    ' many times do you think the die would come up even (2,4, or 6)?', max=2000, min=1)
    F111 = models.IntegerField(label='15. In the BIG BUCKS LOTTERY, the chances of winning a €10 prize are 1%. What is your best guess about how many people would win a €10 prize if 1,000 people each buy a single ticket from BIG BUCKS?',
                              max=2000, min=1)
    F11 = models.IntegerField(label='1. How old are you?', max=99, min=15)
    F12 = models.IntegerField(choices=[[1, 'Female'], [2, 'Male'], [3, 'Diverse'],
    [4, 'I do not feel represented by the above']], label='2. What is your sex?', widget=widgets.RadioSelect)
    F13 = models.IntegerField(choices=[[1, 'I did not graduate school'], [2, 'Apprenticeship'],
    [3, 'General education compulsory school / Vocational secondary school'],
    [4, 'General secondary school / Vocational secondary school'], [5, 'Bachelors or equal degree'],
    [6, 'Masters or higher degree'], [7, 'I do not want to answer']],
                    label='3. What is your highest level of education?', widget=widgets.RadioSelect)
    F14 = models.StringField(blank=True, label='4. What is your main subject of study?')
    F15 = models.StringField(choices=[['1', 'Yes'], ['2', 'No'], ['3', 'I do not want to answer']],
                             label='5. Do you invest in the stock market?',  widget=widgets.RadioSelect)



class AnleitungFragebogen(Page):
    pass

class Fernandes1(Page):
    form_model = 'player'
    form_fields = ['F1111', 'F1', 'F2', 'F3', 'F4', 'F5', 'F55', 'F6', 'F7', 'F8', 'F9', 'F10', 'F101', 'F1112','F111']

class Fernandes2(Page):
    form_model = 'player'
    form_fields = ['F11', 'F12', 'F13','F14', 'F15']

class Payments(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.vars.get('selected_for_payment', False)

    form_model = 'player'
    form_fields = ['name', 'iban', 'iban_repeat']

    @staticmethod
    def error_message(player, values):
        if values['iban'] != values['iban_repeat']:
            return 'The IBANs do not match.'


    def vars_for_template(player: Player):
        return {
            'final_pay': player.participant.payoff_plus_participation_fee()
        }

class Credit(Page):
    @staticmethod
    def is_displayed(player: Player):
        return not player.participant.vars.get('selected_for_payment', False)

    form_model = 'player'
    form_fields = ['name']


class LastPage(Page):
    pass
    
page_sequence = [AnleitungFragebogen, Fernandes1, Fernandes2, Credit, Payments, LastPage]