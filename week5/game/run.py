
from g_classes import *

from util_classes import SupTools


# --- define ntry point function
def run_game():

    print('-------------------------------Welcome to the game!---------------------------\n')

    # set amount of troops
    total_army_qnt = SupTools.set_army_qnt()

    user_army = Army(Recruiter().recruite_for_user(total_army_qnt), 'User')
    opp_army = Army(Recruiter().recruite_for_NPC(total_army_qnt), 'NPC')

    Fight = Battle(user_army, opp_army)
    Fight.begin()

# -------------------- Run main function ------------------
run_game()
