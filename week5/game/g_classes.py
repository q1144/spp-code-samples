import random, time, math

from copy import deepcopy

from util_classes import SupTools


class Units_sq(object):

    """Base class for all classes"""
    def __init__(self):
        
        self.name = 'Base Unit'
        self.group_size = 0
        self.is_alive = True
        # can be replaced by method


    def apply_losses(self, lost_amount):

        group_loss = math.ceil(lost_amount / self.health_points)
        
        if group_loss >= self.group_size:
            self.group_size = 0
            self.is_alive = False
        else:
            self.group_size = self.group_size - group_loss


class Archers_sq(Units_sq):

    def __init__(self, size=0, ap = 10, hp = 10):      
        
        self.name = 'Archers'
        self.label = 'ar'
        self.is_alive = True
        self.atack_points = ap
        self.health_points = hp
        self.group_size = size


class Mages_sq(Units_sq):

    def __init__(self, size=0, ap = 10, hp = 10):
        self.name = 'Mages'
        self.label = 'mg'
        self.is_alive = True
        self.atack_points = ap
        self.health_points = hp
        self.group_size = size


class Warriors_sq(Units_sq):

    def __init__(self, size=0,  ap = 10, hp = 10):
        self.name = 'Warriors'
        self.label = 'wr'
        self.is_alive = True
        self.atack_points = ap
        self.health_points = hp
        self.group_size = size


class Recruiter():
    '''  Recruite a collection of squads '''

    def __init__(self, sq_types=['archers','mages', 'warriors']):
        
        self.squad_types = sq_types

    def create_squad(self, sq_name, sq_size):
        
        sq_name = sq_name.lower()
        if sq_name in self.squad_types and sq_size>=0:
            if sq_name == 'archers':
                sq = Archers_sq(sq_size)              
            elif sq_name == 'mages':
                sq = Mages_sq(sq_size)
            elif sq_name == 'warriors':
                sq = Warriors_sq(sq_size)
        else:
            sq = None
            
        return sq

    def _army_dict_to_lst(self, army_dict):
        army_troops_l = []
        for sq, size in army_dict.items():
            squad = self.create_squad(sq, size)
            if isinstance(squad, Units_sq):
                army_troops_l.append(squad)
        return army_troops_l


    def recruite_for_user(self, army_size = 0):

        army = {sq:None for sq in self.squad_types}
        army_max_limit = army_size if army_size >0 else 0
        army_is_set = False
        army_troops = []

        while(army_is_set == False):
            i = 0

            for class_label, qnt in army.items():
                if army_max_limit > 0:

                    if i == len(army.items())-1: # last step of army iteration
                        qnt = army_max_limit
                        army[class_label]  = qnt
                        army_max_limit = 0
                        print ('Quantity of the %s has been atomatically set to %s.' % (class_label , army[class_label]))
                        print('%s -> %s' %(class_label , army[class_label]))

                    if qnt is None:
                        
                        input_is_correct = False

                        while(not input_is_correct):    
                            typed_value = input('Set %s quantity (max: %s)\n%s ->'%(class_label , army_max_limit, class_label))
                            input_is_correct = SupTools.check_int(typed_value)
                        else:
                            typed_value = int(float(typed_value))

                        if typed_value <= army_max_limit:
                            army[class_label] = typed_value
                            army_max_limit -= typed_value
                        else:
                            print('Amount of %s can`t be greater than army quantity limit (%s)!' % (class_label , army_max_limit))
                            break
                else:
                    if qnt is None:
                        army[class_label] = 0
                        print ('Quantity of the %s has been atomatically set to %s.' % (class_label , army[class_label]))
                        print('%s -> %s' %(class_label , army[class_label]))
                i += 1

            army_is_set = True if army_max_limit == 0 else False
        
        army_troops = self._army_dict_to_lst(army)

        return army_troops


    def recruite_for_NPC(self, army_size = 0):
        
        army = {sq:None for sq in self.squad_types}
        army_clases_l = [sq for sq in self.squad_types]
        army_max_limit = army_size if army_size >0 else 0
        army_troops = []

        i = 0
        while (i < len(army_clases_l)):
            class_label = army_clases_l[i]
            if i == len(army_clases_l)-1:
                if army_max_limit >= 0:
                    army[class_label] = army_max_limit
                    army_max_limit = 0
                break

            if army_max_limit >0:
                r = random.randint(0, army_max_limit)
                army[class_label] = r
                army_max_limit -= r
            else:
                army[class_label] = 0
            
            i += 1

        army_troops = self._army_dict_to_lst(army)

        return army_troops


class Army():

    def __init__(self, squads_collection, a_name):

        self.squads = [sq for sq in squads_collection]
        self._set_dmg_map()
        self._load_dmg_map()
        self.shuffle_squads()
        self.tr_name = a_name
        #self.is_viable = True
  
    
    def _set_dmg_map(self):

        sq_labels = {sq.label : None for sq in self.squads}

        damage_map = {sq.name : deepcopy(sq_labels) for sq in self.squads}
        # set Archers dmg                
        damage_map ['Archers']['ar'] = 1.0
        damage_map ['Archers']['mg'] = 1.2
        damage_map ['Archers']['wr'] = 0.9
        # set Mages dmg
        damage_map ['Mages']['ar'] = 2.0
        damage_map ['Mages']['mg'] = 1.0
        damage_map ['Mages']['wr'] = 1.5
        # set Warriors dmg
        damage_map ['Warriors']['ar'] = 1.3
        damage_map ['Warriors']['mg'] = 1.5
        damage_map ['Warriors']['wr'] = 1.0

        self.damage_map = damage_map
         

    def _load_dmg_map (self):
        
        for squad in self.squads:
            squad.dmg = self.damage_map[squad.name]


    def shuffle_squads(self):
        random.shuffle(self.squads)


class Battle():

    def __init__(self, army1, army2):

        self.army1 = army1
        self.army2 = army2
        self.r_num = 0


    def begin(self):

        print ('\n\n\t\t Battle has started! Let the strongest team wins!\n \t\t\t-== Deus vult! ==-')
        A1 = self.army1
        A2 = self.army2

        battle_finished = False
        i = 0

        while(not battle_finished):
            i +=1

            both_armys_alive = True if (A1.squads and A2.squads) else False

            if both_armys_alive:
                self.start_round()
            else:
                battle_finished = True

        if A1.squads or A2.squads:
            winner = A1 if A1.squads else A2
            winner_is = winner.tr_name
        else:
            winner_is = 'Peace & Friendship'  # Fight end in a draw

        print ('\nBattle finished! %s wins!' % winner_is)
        return winner_is


    def start_round (self):

        self.r_num += 1
        print ('\n\t\t------------------- Round %s! ------------------- ' % self.r_num)
        print ('\t\t------------------- Fight! -------------------')
        
        self.show_positions()

        SQ1_side = self.army1.tr_name
        SQ2_side = self.army2.tr_name

        A1 = self.army1.squads
        A2 = self.army2.squads
    
        SQ1 = A1.pop()
        SQ2 = A2.pop()

        
        sq1_losses = SQ2.dmg[SQ1.label] * SQ2.atack_points*SQ2.group_size
        sq2_losses = SQ1.dmg[SQ2.label] * SQ1.atack_points*SQ1.group_size

        SQ1.apply_losses(sq1_losses)
        SQ2.apply_losses(sq2_losses)

        print('<Action>: Group of %s %s hits %s %s for %s dmg!\n\t %s %s %s has alived!\n' % (SQ1_side, SQ1.name, SQ2_side,SQ2.name, sq2_losses, SQ2.group_size, SQ2_side, SQ2.name))
        time.sleep(2)  # sleep
        print('<Action>: Group of %s %s hits %s %s for %s dmg!\n\t %s %s %s has alived!' % (SQ2_side, SQ2.name, SQ1_side,SQ1.name, sq1_losses, SQ1.group_size, SQ1_side, SQ1.name))

        if SQ1.is_alive:
            A1.append(SQ1)

        if SQ2.is_alive:
            A2.append(SQ2)

        time.sleep(4) # sleep
    

    def show_positions(self):

        A1_name = self.army1.tr_name
        A2_name = self.army2.tr_name
        A1_pos = [(sq.name, sq.group_size) for sq in self.army1.squads]
        A2_pos = [(sq.name, sq.group_size) for sq in self.army2.squads]

        print('\t\t Positions: ')
        print('<%s>: %s' % (A1_name, A1_pos) )
        print('<%s>: %s\n' % (A2_name, A2_pos) )
