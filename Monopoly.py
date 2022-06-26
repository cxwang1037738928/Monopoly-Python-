import random
eric = 'awesome'
prison_count = 0
prison = 22
prison_rent = 50
player_1 = 2000
player_2 = 2000
player_3 = 2000
player_4 = 2000
player_input_1 = 0
player_input = 0
player_1_land = []
player_2_land = []
player_3_land = []
player_4_land = []
steps = []
player_timer_1 = 100
player_timer_2 = 100
player_timer_3 = 100
player_timer_4 = 100
all_steps = 0
steps_2 = []
all_steps_2 = 0
steps_3 = []
all_steps_3 = 0
steps_4 = []
all_steps_4 = 0
old_kent_road, cost, rents = 1, 60, 10
white_chapel_road, cost_1, rents_1 = 2, 60, 20
The_angle_islinton, cost_2, rents_2 = 3, 100, 30
Euston_Road, cost_3, rents_3 = 4, 100, 30
Pentonville_Road, cost_4, rents_4 = 5, 100, 40
Pall_mall, cost_5, rents_5 = 6, 120, 50
white_chapel_hall, cost_6, rents_6 = 7, 140, 60
Northumberland_Avenue, cost_7, rents_7 = 8, 140, 70
bow_street, cost_8, rents_8 = 9, 160, 70
Marlborough_street, cost_9, rents_9 = 10, 180, 80
Vine_Street, cost_10, rents_10 = 11, 180, 90
the_stand, cost_11, rents_11 = 12, 220, 90
fleet_street, cost_12, rents_12 = 13, 220, 100
Trafalgar_Square, cost_13, rents_13 = 14, 240, 110
Leicester_Square, cost_14, rents_14 = 15, 260, 110
Coventry_Street, cost_15, rents_15 = 16, 260, 120
Piccadilly, cost_16, rents_16 = 17, 280, 130
Regent_Street, cost_17, rents_17 = 18, 300, 130
Oxford_Street, cost_18, rents_18 = 19, 300, 130
Bond_Street, cost_19, rents_19 = 20, 320, 150
park_space, cost_20, rents_20 = 30, 350,175
board_walk, cost_21, rents_21 = 38, 400, 200
all_houses = [old_kent_road, white_chapel_road, The_angle_islinton, Euston_Road, Pentonville_Road, Pall_mall,
white_chapel_hall,
Northumberland_Avenue,
bow_street,
Marlborough_street,
Vine_Street,
the_stand,
fleet_street,
Trafalgar_Square,
Leicester_Square,
Coventry_Street,
Piccadilly ,
Regent_Street,
Oxford_Street,
Bond_Street,
park_space,
board_walk,]
all_houses_name = ['old_kent_road', 'white_chapel_road', 'The_angle_islinton', 'Euston_Road', 'Pentonville_Road', 'Pall_mall',
'white_chapel_hall',
'Northumberland_Avenue',
'bow_street',
'Marlborough_street',
'Vine_Street',
'the_stand',
'fleet_street',
'Trafalgar_Square',
'Leicester_Square',
'Coventry_Street',
'Piccadilly' ,
'Regent_Street',
'Oxford_Street',
'Bond_Street',
'park_space',
'board_walk',]
all_cost = [
   cost,
   cost_1,
   cost_2,
   cost_3,
   cost_4,
   cost_5,
   cost_6,
   cost_7,
   cost_8,
   cost_9,
   cost_10,
   cost_11,
   cost_12,
   cost_13,
   cost_14,
   cost_15,
   cost_16,
   cost_17,
   cost_18,
   cost_19,
   cost_20,
   cost_21,
   prison,
]
all_rents = [
   rents,
   rents_1,
   rents_2,
   rents_3,
   rents_4,
   rents_5,
   rents_6,
   rents_7,
   rents_8,
   rents_9,
   rents_10,
   rents_11,
   rents_12,
   rents_13,
   rents_14,
   rents_15,
   rents_16,
   rents_17,
   rents_18,
   rents_19,
   rents_20,
   rents_21,
   prison_rent,
]
brown_set = [
   old_kent_road,
   white_chapel_road
]
blue_set = [
   The_angle_islinton,
   Euston_Road,
   Pentonville_Road
]
pink_set = [
   Pall_mall,
   white_chapel_hall,
   Northumberland_Avenue
]
orange_set = [
   bow_street,
   Vine_Street,
   Marlborough_street
]
red_set = [
   the_stand,
   fleet_street,
   Trafalgar_Square
]
yellow_set = [
   Leicester_Square,
   Coventry_Street,
   Piccadilly
]
green_set = [
   Regent_Street,
   Oxford_Street,
   Bond_Street
]
dark_blue_set = [
   park_space,
   board_walk
]
houses_x = 36
its_my_birthday, price, name = 3, 300, 'its my birthday card'
forced_deal_2, price_1, names = 2, 500, 'forced deal card'
sly_deal, price_2, name_1 = 2, 500, 'slydeal card'
pass_go_2, price_3, name4_2 = 5, 250, 'pass go card'
debt_collector_2, price_4, names3 = 3, 200, 'debt collector card'
double_rent_2, price_5, names4 = 4, 100, 'double rent card'
prison_cards, price_6, names5 = 5, 200, 'prison card'
cards = [
   its_my_birthday,
   forced_deal_2,
   sly_deal,
   pass_go_2,
   debt_collector_2,
   double_rent_2,
]
player_1_card_collection = []
player_2_card_collection = []
player_3_card_collection = []
player_4_card_collection = []
player_1_points = 0
player_2_points = 0
player_3_points = 0
player_4_points = 0
player_1_auction_points = 0
player_2_auction_points = 0
player_3_auction_points = 0
player_4_auction_points = 0
player_1_auction_chances = 5
player_2_auction_chances = 5
player_3_auction_chances = 5
player_4_auction_chances = 5
houses_auctioned = []
houses_auctioning = 0
player_1_giveup = 1
player_2_giveup = 1
player_3_giveup = 1
player_4_giveup = 1
player_input_2 = 1
player_input_3 = 1
player_input_4 = 1
player_input_5 = 1
player_input_6 = 1
auction_won = 0
highest_score = 0
max_house = 0
house_1, house_2, house_3, house_4, hotels = 'house'
house_upgrades = [
   house_1, house_2, house_3, house_4, hotels
]
player_1_all_houses = 0
player_2_all_houses = 0
player_3_all_houses = 0
player_4_all_houses = 0
highest_bet = 0
count_down = 0
count_down_2 = 0
count_down_3 = 0
count_down_4 = 0
starts = 0
starts_2 = 0
starts_3 = 0
starts_4 = 0
house_fix_x = 0
choice_x = 0
prison_timer = 3
get_out_prison = 0


def prison_card():
   global all_steps
   global all_steps_2
   global all_steps_3
   global all_steps_4
   global prison_cards
   global player_input
   while prison_cards in player_1_card_collection > 0:
       try:
           player_input = int(input('who do you want to sent to prison'))
       except ValueError:
           print('type 1 2 or 3')
       if player_input == 1:
           prisons(1)
       elif player_input == 2:
           prisons(2)
       elif player_input == 3:
           prisons(3)
       elif player_input == 4:
           prisons(4)
       else:
           prisons('that is not a player')
   while prison_cards in player_2_card_collection > 0:
       try:
           player_input = int(input('who do you want to sent to prison'))
       except ValueError:
           print('type 1 2 or 3')
       if player_input == 1:
           prisons(1)
       elif player_input == 2:
           prisons(2)
       elif player_input == 3:
           prisons(3)
       elif player_input == 4:
           prisons(4)
       else:
           prisons('that is not a player')
   while prison_cards in player_3_card_collection > 0:
       try:
           player_input = int(input('who do you want to sent to prison'))
       except ValueError:
           print('type 1 2 or 3')
       if player_input == 1:
           prisons(1)
       elif player_input == 2:
           prisons(2)
       elif player_input == 3:
           prisons(3)
       elif player_input == 4:
           prisons(4)
       else:
           prisons('that is not a player')
   while prison_cards in player_4_card_collection > 0:
       try:
           player_input = int(input('who do you want to sent to prison'))
       except ValueError:
           print('type 1 2 or 3')
       if player_input == 1:
           prisons(1)
       elif player_input == 2:
           prisons(2)
       elif player_input == 3:
           prisons(3)
       elif player_input == 4:
           prisons(4)
       else:
           prisons('that is not a player')


def prisons(choice):
   global all_steps
   global all_steps_2
   global all_steps_3
   global all_steps_4
   global prison_timer
   global get_out_prison
   global player_1
   global player_2
   global player_3
   global player_4
   while choice == 1:
       while prison_timer <= 0:
           print('player 1 have been thrown into prison')
           all_steps += all_steps - all_steps - all_steps + 22
           player_1 -= 50
           prison_timer -= 1
           return all_steps
   while choice == 2:
       while prison_timer <= 0:
           print('player 2 have been thrown into prison')
           all_steps_2 += all_steps_2 - all_steps_2 - all_steps_2 + 22
           player_2 -= 50
           prison_timer -= 1
           return all_steps_2
   while choice == 3:
       while prison_timer <= 0:
           print('player 3 have been thrown into prison')
           all_steps_3 += all_steps_3 - all_steps_3 - all_steps_3 + 22
           player_3 -= 50
           prison_timer -= 1
           return all_steps_3
   while choice == 4:
       while prison_timer <= 0:
           print('player 4 have been thrown into prison')
           all_steps_4 += all_steps_4 - all_steps_4 - all_steps_4 + 22
           player_4 -= 50
           prison_timer -= 1
       return all_steps_4


def house_auctioning(choice):
   global starts
   global starts_2
   global starts_3
   global starts_4
   while choice == 1:
       if starts <= 0:
           print('player 1 has started a auction on :', all_houses_name[all_steps - 1])
           print('the original value of the house is :', all_cost[all_steps - 1])
           starts += 1
           return starts
   while choice == 2:
       if starts_2 <= 0:
           print('player 2 has started a auction on :', all_houses_name[all_steps_2 - 1])
           print('the original value of the house is :', all_cost[all_steps_2 - 1])
           starts_2 += 1
           return starts_2
   while choice == 3:
       if starts_3 <= 0:
           print('player 3 has started a auction on :', all_houses_name[all_steps_3 - 1])
           print('the original value of the house is :', all_cost[all_steps_3 - 1])
           starts_3 += 1
           return starts_3
   while choice == 4:
       if starts_4 <= 0:
           print('player 4 has started a auction on :', all_houses_name[all_steps_4 - 1])
           print('the original value of the house is :', all_cost[all_steps_4 - 1])
           starts_4 += 1
           return starts_4


def auction_house(choice):
   global player_1_auction_points
   global player_2_auction_points
   global player_3_auction_points
   global player_4_auction_points
   global player_1
   global player_2
   global player_3
   global player_4
   global player_1_land
   global player_2_land
   global player_3_land
   global player_4_land
   global houses_auctioned
   global player_1_giveup
   global player_2_giveup
   global player_3_giveup
   global player_4_giveup
   global player_input_2
   global auction_won
   global player_input_6
   global player_input_3
   global player_input_4
   global player_input_5
   global highest_score
   global player_input
   global highest_bet
   global count_down
   global count_down_2
   global count_down_3
   global choice_x
   global count_down_4
   if player_input == 'auction':
       if count_down == 0:
           try:
               player_input_3 = int(input('input your bet here player 1:\n'))
               highest_bet += player_input_3
           except ValueError:
               print('put a number please')
           if player_input_3 <= 0:
               print('player 1 has given up the auction')
               count_down += 1
           elif player_input_3 > player_1:
               print('your bet is too high')
       if count_down_2 == 0:
           try:
               player_input_4 = int(input('input your bet here player 2:\n'))
               highest_bet += player_input_4
           except ValueError:
               print('put a number please')
           if player_input_4 <= 0:
               print('player 4 has given up the auction')
               count_down_2 += 1
           elif player_input_4 > player_2:
               print('your bet is too high')
       if count_down_3 == 0:
           try:
               player_input_5 = int(input('input your bet here player 3:\n'))
               highest_bet += player_input_5
           except ValueError:
               print('put a number please')
           if player_input_5 <= 0:
               print('player 3 has given up the auction')
               count_down_3 += 1
           elif player_input_5 > player_3:
               print('your bet is too high')
       if count_down_4 == 0:
           try:
               player_input_6 = int(input('input your bet here player 4:\n'))
               highest_bet += player_input_6
           except ValueError:
               print('put a number please')
           if player_input_6 <= 0:
               print('player 4 has given up the auction')
               count_down_4 += 1
           elif player_input_6 > player_4:
               print('your bet is too high')
       if count_down_2 and count_down_3 and count_down_4 == 1:
           print('player 1 has won the auction, the end price was:', highest_bet)
           player_1 -= highest_bet
           auction_won += 1
       if count_down and count_down_3 and count_down_4 == 1:
           print('player 2 has won the auction, the end price was:', highest_bet)
           player_2 -= highest_bet
           auction_won += 1
       if count_down and count_down_2 and count_down_4 == 1:
           print('player 3 has won the auction, the end price was:', highest_bet)
           player_3 -= highest_bet
           auction_won += 1
       if count_down and count_down_2 and count_down_3 == 1:
           print('player 4 has won the auction, the end price was:', highest_bet)
           player_4 -= highest_bet
           auction_won += 1
   if auction_won > 0:
       if choice == 1:
           Monopoly_2()
           Monopoly_3()
           Monopoly_4()
           Monopoly_1()
       elif choice == 2:
           Monopoly_3()
           Monopoly_4()
           Monopoly_1()
           Monopoly_2()
       elif choice == 3:
           Monopoly_4()
           Monopoly_1()
           Monopoly_2()
           Monopoly_3()
       elif choice == 4:
           Monopoly_1()
           Monopoly_2()
           Monopoly_3()
           Monopoly_4()


def more_houses(choice):
   global player_1_land
   global player_2_land
   global player_3_land
   global player_4_land
   global player_1
   global player_2
   global player_3
   global player_4
   global max_house
   global houses_x
   global hotels
   global house_upgrades
   global player_input_1
   global player_1_all_houses
   global player_2_all_houses
   global player_3_all_houses
   global player_4_all_houses
   while choice == 1:
       try:
           player_input_1 = str(input('do you want to upgrade this land'))
       except ValueError:
           print('type house please')
       except ZeroDivisionError:
           print('type house please')
       while all_houses[all_steps - 1] in player_1_land:
           if player_input_1 == 'house 1':
               player_1_all_houses += 1
               all_houses[all_steps - 1].append(house_upgrades[player_1_all_houses - 1])
               if house_1 in all_houses[all_steps - 1]:
                   player_1 -= all_cost[all_steps - 1] / 3
                   all_rents[all_steps - 1] = all_rents[all_steps - 1] * 1.5
                   print('player 1 has upgraded', all_houses_name[all_steps - 1], 'to level 1',
                         'the new rent is now :', all_rents[all_steps - 1])
           return player_1, all_rents[all_steps - 1], all_cost[all_steps - 1]
       while all_houses[all_steps - 1] in player_1_land:
           if house_1 in all_houses[all_steps - 1]:
               if player_input_1 == 'house 2':
                   player_1_all_houses += 1
                   all_houses[all_steps - 1].append(house_upgrades[player_1_all_houses - 1])
                   if house_2 in all_houses[all_steps - 1]:
                       player_1 -= all_cost[all_steps - 1] / 3
                       all_rents[all_steps - 1] = all_rents[all_steps - 1] * 1.5
                       print('player 1 has upgraded', all_houses_name[all_steps - 1], 'to level 2',
                             'the new rent is now :', all_rents[all_steps - 1])
               return player_1, all_rents[all_steps - 1], all_cost[all_steps - 1]
       while all_houses[all_steps - 1] in player_1_land:
           if house_2 in all_houses[all_steps - 1]:
               if player_input_1 == 'house 3':
                   player_1_all_houses += 1
                   all_houses[all_steps - 1].append(house_upgrades[player_1_all_houses - 1])
                   if house_3 in all_houses[all_steps - 1]:
                       player_1 -= all_cost[all_steps - 1] / 3
                       all_rents[all_steps - 1] = all_rents[all_steps - 1] * 1.5
                       print('player 1 has upgraded', all_houses_name[all_steps - 1], 'to level 3',
                             'the new rent is now :', all_rents[all_steps - 1])
               return player_1, all_rents[all_steps - 1], all_cost[all_steps - 1]
       while all_houses[all_steps - 1] in player_1_land:
           if house_3 in all_houses[all_steps - 1]:
               if player_input_1 == 'house 4':
                   player_1_all_houses += 1
                   all_houses[all_steps - 1].append(house_upgrades[player_1_all_houses - 1])
                   if house_4 in all_houses[all_steps - 1]:
                       player_1 -= all_cost[all_steps - 1] / 3
                       all_rents[all_steps - 1] = all_rents[all_steps - 1] * 1.5
                       print('player 1 has upgraded', all_houses_name[all_steps - 1], 'to level 4',
                             'the new rent is now :', all_rents[all_steps - 1])
               return player_1, all_rents[all_steps - 1], all_cost[all_steps - 1]
       while all_houses[all_steps - 1] in player_1_land:
           if house_4 in all_houses[all_steps - 1]:
               if player_input_1 == 'hotel':
                   player_1_all_houses += 1
                   all_houses[all_steps - 1].append(house_upgrades[player_1_all_houses - 1])
                   if hotels in all_houses[all_steps - 1]:
                       player_1 -= all_cost[all_steps - 1] / 3
                       all_rents[all_steps - 1] = all_rents[all_steps - 1] * 1.5
                       print('player 1 has upgraded', all_houses_name[all_steps - 1], 'to level 2',
                             'the new rent is now :', all_rents[all_steps - 1])
                   return player_1, all_rents[all_steps - 1], all_cost[all_steps - 1]
   while choice == 2:
       try:
           player_input_1 = str(input('do you want to upgrade this land'))
       except ValueError:
           print('type house please')
       except ZeroDivisionError:
           print('type house please')
       while all_houses[all_steps_2 - 1] in player_2_land:
           if player_input_1 == 'house 1':
               player_2_all_houses += 1
               all_houses[all_steps_2 - 1].append(house_upgrades[player_2_all_houses - 1])
               if house_1 in all_houses[all_steps_2 - 1]:
                   player_2 -= all_cost[all_steps_2 - 1] / 3
                   all_rents[all_steps_2 - 1] = all_rents[all_steps_2 - 1] * 1.5
                   print('player 2 has upgraded', all_houses_name[all_steps_2 - 1], 'to level 1',
                         'the new rent is now :', all_rents[all_steps_2 - 1])
               return player_2, all_rents[all_steps_2 - 1], all_cost[all_steps_2 - 1]
       if house_1 in all_houses[all_steps_2 - 1]:
           if player_input_1 == 'house 2':
               player_2_all_houses += 1
               all_houses[all_steps_2 - 1].append(house_upgrades[player_2_all_houses - 1])
               if house_2 in all_houses[all_steps_2 - 1]:
                   player_2 -= all_cost[all_steps_2 - 1] / 3
                   all_rents[all_steps_2 - 1] = all_rents[all_steps_2 - 1] * 1.5
                   print('player 2 has upgraded', all_houses_name[all_steps_2 - 1], 'to level 2',
                         'the new rent is now :', all_rents[all_steps_2 - 1])
               return player_2, all_rents[all_steps_2 - 1], all_cost[all_steps_2 - 1]
       if house_2 in all_houses[all_steps_2 - 1]:
           if player_input_1 == 'house 3':
               player_2_all_houses += 1
               all_houses[all_steps_2 - 1].append(house_upgrades[player_2_all_houses - 1])
               if house_3 in all_houses[all_steps_2 - 1]:
                   player_2 -= all_cost[all_steps_2 - 1] / 3
                   all_rents[all_steps_2 - 1] = all_rents[all_steps_2 - 1] * 1.5
                   print('player 2 has upgraded', all_houses_name[all_steps_2 - 1], 'to level 3',
                         'the new rent is now :', all_rents[all_steps_2 - 1])
               return player_2, all_rents[all_steps_2 - 1], all_cost[all_steps_2 - 1]
       if house_3 in all_houses[all_steps_2 - 1]:
           if player_input_1 == 'house 4':
               player_2_all_houses += 1
               all_houses[all_steps_2 - 1].append(house_upgrades[player_2_all_houses - 1])
               if house_4 in all_houses[all_steps_2 - 1]:
                   player_2 -= all_cost[all_steps_2 - 1] / 3
                   all_rents[all_steps_2 - 1] = all_rents[all_steps_2 - 1] * 1.5
                   print('player 2 has upgraded', all_houses_name[all_steps_2 - 1], 'to level 4',
                         'the new rent is now :', all_rents[all_steps_2 - 1])
               return player_2, all_rents[all_steps_2 - 1], all_cost[all_steps_2 - 1]
       if house_4 in all_houses[all_steps_2 - 1]:
           if player_input_1 == 'hotel':
               player_2_all_houses += 1
               all_houses[all_steps_2 - 1].append(house_upgrades[player_2_all_houses - 1])
               if hotels in all_houses[all_steps_2 - 1]:
                   player_2 -= all_cost[all_steps_2 - 1] / 3
                   all_rents[all_steps_2 - 1] = all_rents[all_steps_2 - 1] * 1.5
                   print('player 2 has upgraded', all_houses_name[all_steps_2 - 1], 'to level 2',
                         'the new rent is now :', all_rents[all_steps_2 - 1])
               return player_2, all_rents[all_steps_2 - 1], all_cost[all_steps_2 - 1]
   while choice == 3:
       try:
           player_input_1 = str(input('do you want to upgrade this land'))
       except ValueError:
           print('type house please')
       except ZeroDivisionError:
           print('type house please')
       while all_houses[all_steps_3 - 1] in player_3_land:
           if player_input_1 == 'house 1':
               player_3_all_houses += 1
               all_houses[all_steps_3 - 1].append(house_upgrades[player_3_all_houses - 1])
               if house_1 in all_houses[all_steps_3 - 1]:
                   player_3 -= all_cost[all_steps_3 - 1] / 3
                   all_rents[all_steps_3 - 1] = all_rents[all_steps_3 - 1] * 1.5
                   print('player 3 has upgraded', all_houses_name[all_steps_3 - 1], 'to level 1',
                         'the new rent is now :', all_rents[all_steps_3 - 1])
               return player_3, all_rents[all_steps_3 - 1], all_cost[all_steps_3 - 1]
       if house_1 in all_houses[all_steps_3 - 1]:
           if player_input_1 == 'house 2':
               player_3_all_houses += 1
               all_houses[all_steps_3 - 1].append(house_upgrades[player_3_all_houses - 1])
               if house_2 in all_houses[all_steps_3 - 1]:
                   player_3 -= all_cost[all_steps_3 - 1] / 3
                   all_rents[all_steps_3 - 1] = all_rents[all_steps_3 - 1] * 1.5
                   print('player 3 has upgraded', all_houses_name[all_steps_3 - 1], 'to level 2',
                         'the new rent is now :', all_rents[all_steps_3 - 1])
               return player_3, all_rents[all_steps_3 - 1], all_cost[all_steps_3 - 1]
       if house_2 in all_houses[all_steps_3 - 1]:
           if player_input_1 == 'house 3':
               player_3_all_houses += 1
               all_houses[all_steps_3 - 1].append(house_upgrades[player_3_all_houses - 1])
               if house_3 in all_houses[all_steps_3 - 1]:
                   player_3 -= all_cost[all_steps_3 - 1] / 3
                   all_rents[all_steps_3 - 1] = all_rents[all_steps_3 - 1] * 1.5
                   print('player 3 has upgraded', all_houses_name[all_steps_3 - 1], 'to level 3',
                         'the new rent is now :', all_rents[all_steps_3 - 1])
               return player_3, all_rents[all_steps_3 - 1], all_cost[all_steps_3 - 1]
       if house_3 in all_houses[all_steps_3 - 1]:
           if player_input_1 == 'house 4':
               player_3_all_houses += 1
               all_houses[all_steps_3 - 1].append(house_upgrades[player_3_all_houses - 1])
               if house_4 in all_houses[all_steps_3 - 1]:
                   player_3 -= all_cost[all_steps_3 - 1] / 3
                   all_rents[all_steps_3 - 1] = all_rents[all_steps_3 - 1] * 1.5
                   print('player 3 has upgraded', all_houses_name[all_steps_3 - 1], 'to level 4',
                         'the new rent is now :', all_rents[all_steps_3 - 1])
               return player_3, all_rents[all_steps_3 - 1], all_cost[all_steps_3 - 1]
       if house_4 in all_houses[all_steps_3 - 1]:
           if player_input_1 == 'hotel':
               player_2_all_houses += 1
               all_houses[all_steps_3 - 1].append(house_upgrades[player_3_all_houses - 1])
               if hotels in all_houses[all_steps_3 - 1]:
                   player_3 -= all_cost[all_steps_3 - 1] / 3
                   all_rents[all_steps_3 - 1] = all_rents[all_steps_3 - 1] * 1.5
                   print('player 3 has upgraded', all_houses_name[all_steps_3 - 1], 'to level 2',
                         'the new rent is now :', all_rents[all_steps_3 - 1])
               return player_3, all_rents[all_steps_3 - 1], all_cost[all_steps_3 - 1]
   if choice == 4:
       try:
           player_input_1 = str(input('do you want to upgrade this land'))
       except ValueError:
           print('type house please')
       except ZeroDivisionError:
           print('type house please')
       while all_houses[all_steps_4 - 1] in player_4_land:
           if player_input_1 == 'house 1':
               player_4_all_houses += 1
               all_houses[all_steps_4 - 1].append(house_upgrades[player_4_all_houses - 1])
               if house_1 in all_houses[all_steps_4 - 1]:
                   player_4 -= all_cost[all_steps_4 - 1] / 3
                   all_rents[all_steps_4 - 1] = all_rents[all_steps_4 - 1] * 1.5
                   print('player 4 has upgraded', all_houses_name[all_steps_4 - 1], 'to level 1',
                         'the new rent is now :', all_rents[all_steps_4 - 1])
               return player_4, all_rents[all_steps_4 - 1], all_cost[all_steps_4 - 1]
       if house_1 in all_houses[all_steps_4 - 1]:
           if player_input_1 == 'house 2':
               player_4_all_houses += 1
               all_houses[all_steps_4 - 1].append(house_upgrades[player_4_all_houses - 1])
               if house_2 in all_houses[all_steps_4 - 1]:
                   player_4 -= all_cost[all_steps_4 - 1] / 3
                   all_rents[all_steps_4 - 1] = all_rents[all_steps_4 - 1] * 1.5
                   print('player 4 has upgraded', all_houses_name[all_steps_4 - 1], 'to level 2',
                         'the new rent is now :', all_rents[all_steps_4 - 1])
               return player_4, all_rents[all_steps_4 - 1], all_cost[all_steps_4 - 1]
       if house_2 in all_houses[all_steps_4 - 1]:
           if player_input_1 == 'house 3':
               player_4_all_houses += 1
               all_houses[all_steps_4 - 1].append(house_upgrades[player_4_all_houses - 1])
               if house_3 in all_houses[all_steps_4 - 1]:
                   player_4 -= all_cost[all_steps_4 - 1] / 3
                   all_rents[all_steps_4 - 1] = all_rents[all_steps_4 - 1] * 1.5
                   print('player 4 has upgraded', all_houses_name[all_steps_4 - 1], 'to level 3',
                         'the new rent is now :', all_rents[all_steps_4 - 1])
               return player_4, all_rents[all_steps_4 - 1], all_cost[all_steps_4 - 1]
       if house_3 in all_houses[all_steps_4 - 1]:
           if player_input_1 == 'house 4':
               player_4_all_houses += 1
               all_houses[all_steps_4 - 1].append(house_upgrades[player_4_all_houses - 1])
               if house_4 in all_houses[all_steps_4 - 1]:
                   player_3 -= all_cost[all_steps_4 - 1] / 3
                   all_rents[all_steps_4 - 1] = all_rents[all_steps_4 - 1] * 1.5
                   print('player 4 has upgraded', all_houses_name[all_steps_4 - 1], 'to level 4',
                         'the new rent is now :', all_rents[all_steps_4 - 1])
               return player_4, all_rents[all_steps_4 - 1], all_cost[all_steps_4 - 1]
       if house_4 in all_houses[all_steps_4 - 1]:
           if player_input_1 == 'hotel':
               player_4_all_houses += 1
               all_houses[all_steps_4 - 1].append(house_upgrades[player_4_all_houses - 1])
               if hotels in all_houses[all_steps_4 - 1]:
                   player_1 -= all_cost[all_steps_4 - 1] / 3
                   all_rents[all_steps_4 - 1] = all_rents[all_steps_4 - 1] * 1.5
                   print('player 4 has upgraded', all_houses_name[all_steps_4 - 1], 'to level 2',
                         'the new rent is now :', all_rents[all_steps_4 - 1])
               return player_4, all_rents[all_steps_4 - 1], all_cost[all_steps_4 - 1]


def debt_collector():
   global player_2
   global player_3
   global player_4
   global player_1
   global debt_collector_2
   global player_1_card_collection
   global player_2_card_collection
   global player_3_card_collection
   global player_4_card_collection
   global player_1_points
   global player_2_points
   global player_3_points
   global player_4_points
   global player_input_2
   if all_steps == 16:
       player_1_points += 100
       print('you received 100 points')
       if debt_collector_2 in player_1_card_collection > 0:
           try:
               player_input_2 = str(input('do you want to use the debt collector card'))
           except ValueError:
               print('type yes or no')
           if player_input_2 == 'yes':
               player_1 -= 150
               player_3 -= 150
               player_4 -= 150
               player_2 += 150
               player_2_card_collection.remove(debt_collector_2)
           elif player_input_2 == 'no':
               return player_1, player_2, player_3, player_4
   elif all_steps_2 == 16:
       player_2_points += 100
       print('you received 100 points')
       if debt_collector_2 in player_2_card_collection > 0:
           try:
               player_input_2 = str(input('do you want to use the debt collector card'))
           except ValueError:
               print('type yes or no')
           if player_input_2 == 'yes':
               player_2 -= 150
               player_3 -= 150
               player_4 -= 150
               player_1 += 150
               player_1_card_collection.remove(debt_collector_2)
           elif player_input_2 == 'no':
               return player_1, player_2, player_3, player_4
   elif all_steps_3 == 16:
       player_3_points += 100
       print('you received 100 points')
       if debt_collector_2 in player_3_card_collection > 0:
           try:
               player_input_2 = str(input('do you want to use the debt collector card'))
           except ValueError:
               print('type yes or no')
           if player_input_2 == 'yes':
               player_2 -= 150
               player_1 -= 150
               player_4 -= 150
               player_3 += 150
               player_3_card_collection.remove(debt_collector_2)
           elif player_input_2 == 'no':
               return player_1, player_2, player_3, player_4
   elif all_steps_4 == 16:
       player_4_points += 100
       print('you received 100 points')
       if debt_collector_2 in player_4_card_collection > 0:
           try:
               player_input_2 = str(input('do you want to use the debt collector card'))
           except ValueError:
               print('type yes or no')
           if player_input_2 == 'yes':
               player_2 -= 150
               player_3 -= 150
               player_1 -= 150
               player_4 += 150
               player_4_card_collection.remove(debt_collector_2)
           elif player_input_2 == 'no':
               return player_1, player_2, player_3, player_4


def forced_deal():
   global player_1_land
   global player_2_land
   global player_3_land
   global player_4_land
   global player_1
   global player_2
   global player_3
   global player_4
   global forced_deal_2
   global player_4_card_collection
   global player_3_card_collection
   global player_2_card_collection
   global player_1_card_collection
   global player_1_points
   global player_2_points
   global player_3_points
   global player_4_points
   global player_input_2
   while forced_deal_2 in player_1_card_collection > 0:
       try:
           player_input_2 = int(input('type a number of house where you want to get'))
       except ValueError:
           print('type a number')
       except ZeroDivisionError:
           print('not zero please')
       a = (random.choice(player_2_land[player_input_2], player_3_land[player_input_2], player_4_land[player_input_2]))
       player_1_land.append(a)
       print('you took', all_houses_name[player_input_2])
       player_2_land.remove(all_houses[player_input_2])
       player_3_land.remove(all_houses[player_input_2])
       player_4_land.remove(all_houses[player_input_2])
       player_1 -= 1
   if all_steps == 8:
       player_1_points += 150
       return player_1_points
   while forced_deal_2 in player_2_card_collection > 0:
       try:
           player_input_2 = int(input('type a number of house where you want to get'))
       except ValueError:
           print('type a number')
       except ZeroDivisionError:
           print('not zero please')
       a = (random.choice(player_2_land[player_input_2], player_3_land[player_input_2], player_4_land[player_input_2]))
       player_2_land.append(a)
       print('you took', all_houses_name[player_input_2])
       player_2_land.remove(all_houses[player_input_2])
       player_3_land.remove(all_houses[player_input_2])
       player_4_land.remove(all_houses[player_input_2])
       player_2 -= 1
   if all_steps_2 == 8:
       player_2_points += 150
       return player_2_points
   while forced_deal_2 in player_3_card_collection > 0:
       try:
           player_input_2 = int(input('type a number of house where you want to get'))
       except ValueError:
           print('type a number')
       except ZeroDivisionError:
           print('not zero please')
       a = (random.choice(player_2_land[player_input_2], player_3_land[player_input_2], player_4_land[player_input_2]))
       player_3_land.append(a)
       print('you took', all_houses_name[player_input_2])
       player_2_land.remove(all_houses[player_input_2])
       player_3_land.remove(all_houses[player_input_2])
       player_4_land.remove(all_houses[player_input_2])
       player_3 -= 1
   if all_steps_3 == 8:
       player_3_points += 150
       return player_3_points
   while forced_deal_2 in player_4_card_collection > 0:
       try:
           player_input_2 = int(input('type a number of house where you want to get'))
       except ValueError:
           print('type a number')
       except ZeroDivisionError:
           print('not zero please')
       a = (random.choice(player_2_land[player_input_2], player_3_land[player_input_2], player_4_land[player_input_2]))
       player_4_land.append(a)
       print('you took', all_houses_name[player_input_2])
       player_2_land.remove(all_houses[player_input_2])
       player_3_land.remove(all_houses[player_input_2])
       player_4_land.remove(all_houses[player_input_2])
       player_4 -= 1
   if all_steps_4 == 8:
       player_4_points += 150
       return player_4_points


def pass_go():
   global all_steps
   global all_steps_2
   global all_steps_3
   global all_steps_4
   global player_1_card_collection
   global player_2_card_collection
   global player_3_card_collection
   global player_4_card_collection
   global player_1_points
   global player_2_points
   global player_3_points
   global player_4_points
   all_steps = sum(steps)
   all_steps_2 = sum(steps_2)
   all_steps_3 = sum(steps_3)
   all_steps_4 = sum(steps_4)
   global player_input_2
   global player_input_3
   global player_input_4
   while pass_go_2 in player_1_card_collection:
           try:
               player_input_3 = int(input('how many steps do you want to go, max 25'))
           except ValueError:
               print('type a number')
           except ZeroDivisionError:
               print('except zero')
           if player_input_3 > 25:
               print('you\'re pass your limit')
               return player_input_3, all_steps, player_input_2
           elif player_input_3 < 25:
               steps.append(player_input_3)
               print('you advanced', player_input_3, 'steps')
   if all_steps == 16:
       player_1_points += 200
       print('you\'ve received 200 points')
       return player_1_points
   while pass_go_2 in player_2_card_collection:
           try:
               player_input_3 = int(input('how many steps do you want to go, max 25'))
           except ValueError:
               print('type a number')
           except ZeroDivisionError:
               print('except zero')
           if player_input_3 > 25:
               print('you\'re pass your limit')
               return player_input_3, all_steps_2, player_input_2
           elif player_input_3 < 25:
               steps_2.append(player_input_3)
               print('you advanced', player_input_3, 'steps')
   if all_steps == 16:
       player_2_points += 200
       print('you\'ve received 200 points')
       return player_2_points
   while pass_go_2 in player_3_card_collection:
           try:
               player_input_3 = int(input('how many steps do you want to go, max 25'))
           except ValueError:
               print('type a number')
           except ZeroDivisionError:
               print('except zero')
           if player_input_3 > 25:
               print('you\'re pass your limit')
               return player_input_3, all_steps_2, player_input_2
           elif player_input_3 < 25:
               steps_3.append(player_input_3)
               print('you advanced', player_input_3, 'steps')
   if all_steps == 16:
       player_3_points += 200
       print('you\'ve received 200 points')
       return player_3_points
   while pass_go_2 in player_4_card_collection:
           try:
               player_input_3 = int(input('how many steps do you want to go, max 25'))
           except ValueError:
               print('type a number')
           except ZeroDivisionError:
               print('except zero')
           if player_input_3 > 25:
               print('you\'re pass your limit')
               return player_input_3, all_steps_4, player_input_2
           elif player_input_3 < 25:
               steps_4.append(player_input_3)
               print('you advanced', player_input_3, 'steps')
   if all_steps == 16:
       player_4_points += 200
       print('you\'ve received 200 points')
       return player_4_points


def double_rent():
   global all_rents
   global all_steps
   global all_steps_2
   global all_steps_3
   global all_steps_4
   global double_rent_2
   global player_1_points
   global player_2_points
   global player_3_points
   global player_4_points
   global all_houses
   global player_1_land
   global player_2_land
   global player_3_land
   global player_4_land
   global player_input_2
   global player_input_3
   while pass_go_2 in player_1_card_collection:
       try:
           player_input_2 = int(input('which property do you want to use double rent card on'))
       except ValueError:
           print('type use which property you want to use it on or skip')
       except ZeroDivisionError:
           print('type which property you want to use it on or skip')
       if all_houses[player_input_2] not in player_1_land:
           print('the house you picked wasn\'t your property')
           return player_1_card_collection
       elif all_houses[player_input_2] in player_1_land:
           print('you have doubled the rent of', all_houses_name[player_input_2])
           all_rents[player_input_2] = all_rents[player_input_2] * 2
           return player_1_card_collection
   while pass_go_2 in player_2_card_collection:
       try:
           player_input_2 = int(input('which property do you want to use double rent card on'))
       except ValueError:
           print('type use which property you want to use it on or skip')
       except ZeroDivisionError:
           print('type which property you want to use it on or skip')
       if all_houses[player_input_2] not in player_2_land:
           print('the house you picked wasn\'t your property')
           return player_2_card_collection
       elif all_houses[player_input_2] in player_2_land:
           print('you have doubled the rent of', all_houses_name[player_input_2])
           all_rents[player_input_2] = all_rents[player_input_2] * 2
           return player_2_card_collection
   while pass_go_2 in player_3_card_collection:
       try:
           player_input_2 = int(input('which property do you want to use double rent card on'))
       except ValueError:
           print('type use which property you want to use it on or skip')
       except ZeroDivisionError:
           print('type which property you want to use it on or skip')
       if all_houses[player_input_2] not in player_3_land:
           print('the house you picked wasn\'t your property')
           return player_3_card_collection
       elif all_houses[player_input_2] in player_3_land:
           print('you have doubled the rent of', all_houses_name[player_input_2])
           all_rents[player_input_2] = all_rents[player_input_2] * 2
           return player_3_card_collection
   while pass_go_2 in player_4_card_collection:
       try:
           player_input_2 = int(input('which property do you want to use double rent card on'))
       except ValueError:
           print('type use which property you want to use it on or skip')
       except ZeroDivisionError:
           print('type which property you want to use it on or skip')
       if all_houses[player_input_2] not in player_4_land:
           print('the house you picked wasn\'t your property')
           return player_4_card_collection
       elif all_houses[player_input_2] in player_4_land:
           print('you have doubled the rent of', all_houses_name[player_input_2])
           all_rents[player_input_2] = all_rents[player_input_2] * 2
           return player_4_card_collection


def card_shops(choice):
   global player_1_points
   global player_2_points
   global player_3_points
   global player_3_land
   global player_4_points
   global all_steps
   global all_steps_2
   global all_steps_3
   global all_steps_4
   global player_1_card_collection
   global player_2_card_collection
   global player_3_card_collection
   global player_4_card_collection
   global double_rent_2
   global forced_deal_2
   global debt_collector_2
   global pass_go_2
   global player_input_2
   global player_input_3
   while choice == 1:
       if all_steps == 21:
           print('you have entered the card shop\n')
           print('your total points are: ', player_1_points)
           try:
               player_input_2 = str(input('type the card you would like to purchase'))
           except ValueError:
               print('type a card or skip')
           for a, b, c in cards:
               if a > 0:
                   if player_1_points >= b:
                       print('your card options are: ', c)
           if player_input_2 == 'pass go':
               if player_1_points < 250:
                   print('you don\'t have enough points')
                   print('player 1 points: ', player_1_points)
               elif player_1_points > 250:
                   print('you have successfully purchased the pass go card')
                   player_1_points -= 250
                   player_1_card_collection.append(pass_go_2)
                   pass_go_2 -= 1
           elif player_input_2 == 'double rent':
               if player_1_points < 100:
                   print('you don\'t have enough points')
                   print('player 1 points: ', player_1_points)
               elif player_1_points > 100:
                   print('you have successfully purchased the double rent card')
                   player_1_points -= 100
                   player_1_card_collection.append(double_rent_2)
                   double_rent_2 -= 1
           elif player_input_2 == 'forced deal':
               if player_1_points < 500:
                   print('you don\'t have enough points')
                   print('player 1 points: ', player_1_points)
               elif player_1_points > 500:
                   print('you have successfully purchased the forced deal card')
                   player_1_points -= 500
                   player_1_card_collection.append(forced_deal_2)
                   forced_deal_2 -= 1
           elif player_input_2 == 'debt collector':
               if player_1_points < 200:
                   print('you don\'t have enough points')
                   print('player 1 points: ', player_1_points)
               elif player_1_points > 200:
                   print('you have successfully purchased the debt collector card')
                   player_1_points -= 200
                   player_1_card_collection.append(debt_collector_2)
                   debt_collector_2 -= 1
           elif player_input_2 == 'prison card':
               if player_1_points < 200:
                   print('you don\'t have enough points')
                   print('player 1 points: ', player_1_points)
               elif player_1_points > 200:
                   print('you have successfully purchased the debt collector card')
                   player_1_points -= 200
                   player_1_card_collection.append(prison_cards)
                   debt_collector_2 -= 1
           elif player_input_2 == 'skip':
               roll_dice(random.randrange(1, 6), 1)
               roll_dice_2(random.randrange(1, 6), 1)
       return player_1_card_collection, player_1_points, all_steps
   while choice == 2:
       if all_steps_2 == 21:
           print('you have entered the card shop\n')
           print('your total points are: ', player_2_points)
           try:
               player_input_2 = str(input('type the card you would like to purchase'))
           except ValueError:
               print('type a card or skip')
           for a, b, c in cards:
               if a > 0:
                   if player_2_points >= b:
                       print('your card options are: ', c)
           if player_input_2 == 'pass go':
               if player_2_points < 250:
                   print('you don\'t have enough points')
                   print('player 2 points: ', player_2_points)
               elif player_2_points > 250:
                   print('you have successfully purchased the pass go card')
                   player_2_points -= 250
                   player_2_card_collection.append(pass_go_2)
                   pass_go_2 -= 1
               elif player_input_2 == 'double rent':
                   if player_2_points < 100:
                       print('you don\'t have enough points')
                       print('player 2 points: ', player_2_points)
                   elif player_2_points > 100:
                       print('you have successfully purchased the double rent card')
                       player_2_points -= 100
                       player_2_card_collection.append(double_rent_2)
                       double_rent_2 -= 1
               elif player_input_2 == 'forced deal':
                   if player_2_points < 500:
                       print('you don\'t have enough points')
                       print('player 2 points: ', player_2_points)
                   elif player_2_points > 500:
                       print('you have successfully purchased the forced deal card')
                       player_2_points -= 500
                       player_2_card_collection.append(forced_deal_2)
                       forced_deal_2 -= 1
               elif player_input_2 == 'debt collector':
                   if player_2_points < 200:
                       print('you don\'t have enough points')
                       print('player 2 points: ', player_2_points)
                   elif player_2_points > 200:
                       print('you have successfully purchased the debt collector card')
                       player_2_points -= 200
                       player_2_card_collection.append(debt_collector_2)
                       debt_collector_2 -= 1
               elif player_input_2 == 'prison card':
                   if player_2_points < 200:
                       print('you don\'t have enough points')
                       print('player 1 points: ', player_2_points)
                   elif player_2_points > 200:
                       print('you have successfully purchased the debt collector card')
                       player_2_points -= 200
                       player_2_card_collection.append(prison_cards)
                       debt_collector_2 -= 1
           elif player_input_2 == 'skip':
               roll_dice(random.randrange(1, 6), 2)
               roll_dice_2(random.randrange(1, 6), 2)
       return player_2_card_collection, player_2_points, all_steps_2
   while choice == 3:
       if all_steps_3 == 21:
           print('you have entered the card shop\n')
           print('your total points are: ', player_3_points)
           try:
               player_input_2 = str(input('type the card you would like to purchase'))
           except ValueError:
               print('type a card or skip')
           for a, b, c in cards:
               if a > 0:
                   if player_3_points >= c:
                       print('your card options are: ', c)
           if player_input_2 == 'pass go':
               if player_3_points < 250:
                   print('you don\'t have enough points')
                   print('player 3 points: ', player_3_points)
               elif player_3_points > 250:
                   print('you have successfully purchased the pass go card')
                   player_3_points -= 3
                   player_3_card_collection.append(pass_go_2)
                   pass_go_2 -= 1
           elif player_input_2 == 'double rent':
               if player_3_points < 100:
                   print('you don\'t have enough points')
                   print('player 3 points: ', player_3_points)
               elif player_3_points > 100:
                   print('you have successfully purchased the double rent card')
                   player_3_points -= 100
                   player_3_card_collection.append(double_rent_2)
                   double_rent_2 -= 1
           elif player_input_2 == 'forced deal':
               if player_3_points < 500:
                   print('you don\'t have enough points')
                   print('player 3 points: ', player_3_points)
               elif player_3_points > 500:
                   print('you have successfully purchased the forced deal card')
                   player_3_points -= 500
                   player_3_card_collection.append(forced_deal_2)
                   forced_deal_2 -= 1
           elif player_input_2 == 'debt collector':
               if player_3_points < 200:
                   print('you don\'t have enough points')
                   print('player 3 points: ', player_3_points)
               elif player_3_points > 200:
                   print('you have successfully purchased the debt collector card')
                   player_3_points -= 200
                   player_3_card_collection.append(debt_collector_2)
                   debt_collector_2 -= 1
           elif player_input_2 == 'prison card':
               if player_3_points < 200:
                   print('you don\'t have enough points')
                   print('player 1 points: ', player_3_points)
               elif player_3_points > 200:
                   print('you have successfully purchased the debt collector card')
                   player_3_points -= 200
                   player_3_card_collection.append(prison_cards)
                   debt_collector_2 -= 1
           elif player_input_2 == 'skip':
               roll_dice(random.randrange(1, 6), 3)
               roll_dice_2(random.randrange(1, 6), 3)
       return player_3_card_collection, player_3_points, all_steps_3
   while choice == 4:
       if all_steps_4 == 21:
           print('you have entered the card shop\n')
           print('your total points are: ', player_4_points)
           try:
               player_input_2 = str(input('type the card you would like to purchase'))
           except ValueError:
               print('type a card or skip')
           for a, b, c in cards:
               if a > 0:
                   if player_4_points >= b:
                       print('your card options are: ', c)
           if player_input_2 == 'pass go':
               if player_4_points < 250:
                   print('you don\'t have enough points')
                   print('player 4 points: ', player_4_points)
               elif player_4_points > 250:
                   print('you have successfully purchased the pass go card')
                   player_4_points -= 250
                   player_4_card_collection.append(pass_go_2)
                   pass_go_2 -= 1
           elif player_input_2 == 'double rent':
               if player_4_points < 100:
                   print('you don\'t have enough points')
                   print('player 4 points: ', player_4_points)
               elif player_4_points > 100:
                   print('you have successfully purchased the double rent card')
                   player_4_points -= 100
                   player_4_card_collection.append(double_rent_2)
                   double_rent_2 -= 1
           elif player_input_2 == 'forced deal':
               if player_4_points < 500:
                   print('you don\'t have enough points')
                   print('player 4 points: ', player_4_points)
               elif player_4_points > 500:
                   print('you have successfully purchased the forced deal card')
                   player_4_points -= 500
                   player_4_card_collection.append(forced_deal_2)
                   forced_deal_2 -= 1
           elif player_input_2 == 'debt collector':
               if player_4_points < 200:
                   print('you don\'t have enough points')
                   print('player 4 points: ', player_4_points)
               elif player_4_points > 200:
                   print('you have successfully purchased the debt collector card')
                   player_4_points -= 200
                   player_4_card_collection.append(debt_collector_2)
                   debt_collector_2 -= 1
           elif player_input_2 == 'prison card':
               if player_4_points < 200:
                   print('you don\'t have enough points')
                   print('player 1 points: ', player_4_points)
               elif player_4_points > 200:
                   print('you have successfully purchased the debt collector card')
                   player_4_points -= 200
                   player_4_card_collection.append(prison_cards)
                   debt_collector_2 -= 1
           elif player_input_2 == 'skip':
               roll_dice(random.randrange(1, 6), 4)
               roll_dice_2(random.randrange(1, 6), 4)
       return player_4_card_collection, player_4_points, all_steps_4


def roll_dice(possible_rolls, choice_5):
   while choice_5 == 1:
       if possible_rolls == 1:
           steps.append(1)
           print('you walked 1 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 2:
           steps.append(2)
           print('you walked 2 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 3:
           steps.append(3)
           print('you walked 3 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 4:
           steps.append(4)
           print('you walked 4 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 5:
           steps.append(5)
           print('you walked 5 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 6:
           steps.append(6)
           print('you walked 6 step')
           print('total steps:', all_steps, '/ 25')
       return steps, all_steps
   while choice_5 == 2:
       if possible_rolls == 1:
           steps_2.append(1)
           print('you walked 1 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 2:
           steps_2.append(2)
           print('you walked 2 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 3:
           steps_2.append(3)
           print('you walked 3 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 4:
           steps_2.append(4)
           print('you walked 4 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 5:
           steps_2.append(5)
           print('you walked 5 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 6:
           steps_2.append(6)
           print('you walked 6 step')
           print('total steps:', all_steps_2, '/ 25')
       return steps_2, all_steps_2
   while choice_5 == 3:
       if possible_rolls == 1:
           steps_3.append(1)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 2:
           steps_3.append(2)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 3:
           steps_3.append(3)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 4:
           steps_3.append(4)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 5:
           steps_3.append(5)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 6:
           steps_3.append(6)
           print('total steps:', all_steps_3, '/ 25')
       return steps_3, all_steps_3
   while choice_5 == 4:
       if possible_rolls == 1:
           steps_4.append(1)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 2:
           steps_4.append(2)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 3:
           steps_4.append(3)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 4:
           steps_4.append(4)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 5:
           steps_4.append(5)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 6:
           steps_4.append(6)
           print('total steps:', all_steps_4, '/ 25')
       return steps_4, all_steps_4


def roll_dice_2(possible_rolls, choice_5):
   while choice_5 == 1:
       if possible_rolls == 1:
           steps.append(1)
           print('you walked 1 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 2:
           steps.append(2)
           print('you walked 2 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 3:
           steps.append(3)
           print('you walked 3 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 4:
           steps.append(4)
           print('you walked 4 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 5:
           steps.append(5)
           print('you walked 5 step')
           print('total steps:', all_steps, '/ 25')
       elif possible_rolls == 6:
           steps.append(6)
           print('you walked 6 step')
           print('total steps:', all_steps, '/ 25')
       return steps, all_steps
   while choice_5 == 2:
       if possible_rolls == 1:
           steps_2.append(1)
           print('you walked 1 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 2:
           steps_2.append(2)
           print('you walked 2 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 3:
           steps_2.append(3)
           print('you walked 3 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 4:
           steps_2.append(4)
           print('you walked 4 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 5:
           steps_2.append(5)
           print('you walked 5 step')
           print('total steps:', all_steps_2, '/ 25')
       elif possible_rolls == 6:
           steps_2.append(6)
           print('you walked 6 step')
           print('total steps:', all_steps_2, '/ 25')
       return steps_2, all_steps_2
   while choice_5 == 3:
       if possible_rolls == 1:
           steps_3.append(1)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 2:
           steps_3.append(2)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 3:
           steps_3.append(3)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 4:
           steps_3.append(4)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 5:
           steps_3.append(5)
           print('total steps:', all_steps_3, '/ 25')
       elif possible_rolls == 6:
           steps_3.append(6)
           print('total steps:', all_steps_3, '/ 25')
       return steps_3, all_steps_3
   while choice_5 == 4:
       if possible_rolls == 1:
           steps_4.append(1)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 2:
           steps_4.append(2)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 3:
           steps_4.append(3)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 4:
           steps_4.append(4)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 5:
           steps_4.append(5)
           print('total steps:', all_steps_4, '/ 25')
       elif possible_rolls == 6:
           steps_4.append(6)
           print('total steps:', all_steps_4, '/ 25')
       return steps_4, all_steps_4


def buy_houses(choice):
   global steps
   global all_houses
   global all_steps
   global all_steps_2
   global all_steps_3
   global all_steps_4
   global steps_2
   global steps_3
   global steps_4
   global player_1_land
   global player_2_land
   global player_3_land
   global player_4_land
   global player_1
   global player_2
   global player_3
   global player_4
   global player_input
   global all_houses
   global houses_auctioning
   global houses_auctioned
   while choice == 1:
       all_steps = sum(steps)
       if all_houses[all_steps - 1] in player_2_land or player_3_land or player_4_land:
           print('you are on other peoples property, you have to pay rent now')
           player_1 -= all_rents[all_steps - 1]
           print('you paid', all_rents[all_steps - 1], 'dollars of rent\n')
       if all_steps == all_houses[all_steps - 1]:
           try:
               player_input = str(input('do you want to purchase this piece of land, type yes or auction:\n'))
           except ValueError:
               print('type yes or auction please')
           if all_houses[all_steps - 1] not in player_2_land or player_3_land or player_4_land or player_1_land:
               if player_input == 'yes':
                   player_1_land.append(all_houses[all_steps - 1])
                   player_1 -= all_cost[all_steps - 1]
                   print('you have purchased:', str(all_houses_name[all_steps - 1]))
                   print('you have', player_1, 'dollars left')
                   return player_1
               while all_houses[all_steps - 1] not in player_2_land or player_3_land or player_4_land or player_1_land:
                   if player_input == 'auction':
                           house_auctioning(1)
                           auction_house(1)
                           houses_auctioning += 1
                           houses_auctioned.append(all_houses[all_steps - 1])
       elif all_steps == 22:
           prisons(1)
       return all_steps, steps, player_1_land
   while choice == 2:
       all_steps_2 = sum(steps_2)
       if all_houses[all_steps_2 - 1] in player_1_land or player_3_land or player_4_land:
           print('you are on other peoples property,  you have to pay rent')
           player_2 -= all_rents[all_steps_2 - 1]
           print('you paid', all_rents[all_steps_2 - 1], 'dollars of rent\n')
       if all_steps_2 == all_houses[all_steps_2 - 1]:
           try:
               player_input = str(input('do you want to purchase this land, type yes or auction: \n'))
           except ValueError:
                   print('type yes or auction please')
           if all_houses[all_steps_2 - 1] not in player_1_land or player_3_land or player_4_land:
               if player_input == 'yes':
                   player_2_land.append(all_houses[all_steps_2 - 1])
                   player_2 -= all_cost[all_steps_2 - 1]
                   print('you have purchased:', str(all_houses_name[all_steps_2 - 1]))
                   print('you have', player_2, 'dollars left')
                   return player_2
               while all_houses[all_steps_2 - 1] not in player_1_land or player_3_land or player_4_land or player_2_land:
                   if player_input == 'auction':
                           house_auctioning(1)
                           auction_house(2)
                           houses_auctioning += 1
                           houses_auctioned.append(all_houses[all_steps_2 - 1])
           elif all_steps_2 == 22:
               prisons(2)
       return all_steps_2, steps_2, player_2_land
   while choice == 3:
       all_steps_3 = sum(steps_3)
       if all_houses[all_steps_3 - 1] in player_2_land or player_1_land or player_4_land:
           print('you are on other peoples property,  you have to pay rent')
           player_3 -= all_rents[all_steps_3 - 1]
           print('you paid', all_rents[all_steps_3 - 1], 'dollars of rent\n')
       if all_steps_3 == all_houses[all_steps_3 - 1]:
           try:
               player_input = str(input('do you want to purchase this land, type yes or auction: \n'))
           except ValueError:
               print('type yes or auction please')
           if all_houses[all_steps_3 - 1] not in player_2_land or player_3_land or player_4_land or player_1_land:
               if player_input == 'yes':
                   player_3_land.append(all_houses[all_steps_3 - 1])
                   player_3 -= all_cost[all_steps_3 - 1]
                   print('you have purchased:', str(all_houses_name[all_steps_3 - 1]))
                   print('you have', player_3, 'dollars left')
                   return player_3
           while all_houses[all_steps_3 - 1] not in player_2_land or player_3_land or player_4_land:
               if player_input == 'auction':
                   while all_houses[all_steps_3 - 1] not in player_2_land or player_3_land or player_4_land or player_1_land:
                       house_auctioning(3)
                       auction_house(3)
                       houses_auctioning += 1
                       houses_auctioned.append(all_houses[all_steps_3 - 1])
       elif all_steps_3 == 22:
           prisons(3)
       return all_steps_3, steps_3, player_3_land
   while choice == 4:
       all_steps_4 = sum(steps_4)
       if all_houses[all_steps_4 - 1] in player_1_land or player_2_land or player_3_land:
           print('you are or other people\'s property, you have to pay rent')
           player_4 -= all_rents[all_steps_4 - 1]
           print('you paid', all_rents[all_steps_4 - 1], 'dollars of rent')
       if all_steps_4 == all_houses[all_steps_4 - 1]:
           try:
               player_input = str(input('do you want to purchase this land, type yes or auction: \n'))
           except ValueError:
               print('type yes or auction please')
           if all_houses[all_steps_4 - 1] not in player_1_land or player_2_land or player_3_land or player_4_land:
               if player_input == 'yes':
                   player_4 -= all_cost[all_steps_4 - 1]
                   player_4_land.append(all_houses[all_steps_4 - 1])
                   print('you have purchased:', str(all_houses_name[all_steps_4 - 1]))
                   print('you have', player_4, 'dollars left')
                   return player_4
           while all_houses[all_steps_4 - 1] not in player_1_land or player_2_land or player_3_land:
               if player_input == 'auction':
                   while all_houses[all_steps_4 - 1] not in player_1_land or player_2_land or player_3_land or player_4_land:
                       house_auctioning(4)
                       auction_house(4)
                       houses_auctioning += 1
                       houses_auctioned.append(all_houses[all_steps_4 - 1])
       elif all_steps_4 == 22:
           prisons(4)
   return all_steps_4, steps_4, player_4_land


def houses(choice):
   global brown_set
   global blue_set
   global green_set
   global yellow_set
   global pink_set
   global red_set
   global dark_blue_set
   global orange_set
   global all_rents
   global all_steps
   global houses_x
   global player_1
   global player_2
   global player_3
   global player_4
   global player_input_2
   while choice == 1:
       while player_timer_1 > 0:
           try:
               player_input_2 = str(input('do you want to put a house on this piece of land for'))
           except ValueError:
               print('type house or auction')
           if player_input_2 == 'house':
               sets_1()
               more_houses(1)
               houses_x -= 1
               print('player_1 now have a house on', all_houses_name[all_steps - 1])
               print('there\'s only', houses_x, 'left')
       return all_rents, all_steps, player_1, houses_x
   while choice == 2:
       while player_timer_2 > 0:
           try:
               player_input_2 = str(input('do you want to put a house on this piece of land for'))
           except ValueError:
               print('type house or auction')
           if player_input_2 == 'house':
               sets_2()
               more_houses(2)
               houses_x -= 1
               print('player_2 now have a house on', all_houses_name[all_steps_2 - 1])
               print('there\'s only', houses_x, 'left')
       return all_rents, all_steps_2, player_2, houses_x
   while choice == 3:
       while player_timer_3 > 0:
           try:
               player_input_2 = str(input('do you want to put a house on this piece of land for'))
           except ValueError:
               print('type house or auction')
           if player_input_2 == 'house':
               sets_3()
               more_houses(3)
               houses_x -= 1
               print('player_3 now have a house on', all_houses_name[all_steps_3 - 1])
               print('there\'s only', houses_x, 'left')
       return all_rents, all_steps_3, player_3, houses_x
   while choice == 4:
       while player_timer_4 > 0:
           try:
               player_input_2 = str(input('do you want to put a house on this piece of land for'))
           except ValueError:
               print('type house or auction')
           if player_input_2 == 'house':
               sets_4()
               more_houses(4)
               houses_x -= 1
               print('player_4 now have a house on', all_houses_name[all_steps_4 - 1])
               print('there\'s only', houses_x, 'left')
       return all_rents, all_steps_4, player_4, houses_x


def sets_1():
   global brown_set
   global blue_set
   global green_set
   global yellow_set
   global pink_set
   global red_set
   global dark_blue_set
   global orange_set
   global player_1_land
   while True:
       while player_timer_1 > 0:
           if list(set(brown_set) - set(player_1_land)) == old_kent_road or white_chapel_road:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           elif list(set(blue_set) - set(player_1_land)) == The_angle_islinton or Pentonville_Road or Euston_Road:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           elif list(set(pink_set) - set(player_1_land)) == Pall_mall or white_chapel_hall or Northumberland_Avenue:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           elif list(set(orange_set) - set(player_1_land)) == bow_street or Vine_Street or Marlborough_street:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           elif list(set(red_set) - set(player_1_land)) == the_stand or fleet_street or Trafalgar_Square:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           elif list(set(yellow_set) - set(player_1_land)) == Leicester_Square or Coventry_Street or Piccadilly:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           elif list(set(green_set) - set(player_1_land)) == Regent_Street or Oxford_Street or Bond_Street:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           elif list(set(dark_blue_set) - set(player_1_land)) == park_space or board_walk:
               print('you can\'t put a house on this land yet')
               Monopoly_2()
               return player_1_land, all_steps
           else:
               houses(1)
       return player_1_land, all_steps


def sets_2():
   global brown_set
   global blue_set
   global green_set
   global yellow_set
   global pink_set
   global red_set
   global dark_blue_set
   global orange_set
   global player_2_land
   while True:
       while player_timer_2 > 0:
           if list(set(brown_set) - set(player_2_land)) == old_kent_road or white_chapel_road:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
               return player_2_land, all_steps_2
           elif list(set(blue_set) - set(player_2_land)) == The_angle_islinton or Pentonville_Road or Euston_Road:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
               return player_2_land, all_steps_2
           elif list(set(pink_set) - set(player_2_land)) == Pall_mall or white_chapel_hall or Northumberland_Avenue:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
               return player_2_land, all_steps_2
           elif list(set(orange_set) - set(player_2_land)) == bow_street or Vine_Street or Marlborough_street:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
               return player_2_land, all_steps_2
           elif list(set(red_set) - set(player_2_land)) == the_stand or fleet_street or Trafalgar_Square:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
               return player_2_land, all_steps_2
           elif list(set(yellow_set) - set(player_2_land)) == Leicester_Square or Coventry_Street or Piccadilly:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
               return player_2_land, all_steps_2
           elif list(set(green_set) - set(player_2_land)) == Regent_Street or Oxford_Street or Bond_Street:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
               return player_2_land, all_steps_2
           elif list(set(dark_blue_set) - set(player_2_land)) == park_space or board_walk:
               print('you can\'t put a house on this land yet')
               Monopoly_3()
           else:
               houses(2)
       return player_2_land, all_steps_2


def sets_3():
   global brown_set
   global blue_set
   global green_set
   global yellow_set
   global pink_set
   global red_set
   global dark_blue_set
   global orange_set
   global player_3_land
   while True:
       while player_timer_3 > 0:
           if list(set(brown_set) - set(player_3_land)) == old_kent_road or white_chapel_road:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           elif list(set(blue_set) - set(player_3_land)) == The_angle_islinton or Pentonville_Road or Euston_Road:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           elif list(set(pink_set) - set(player_3_land)) == Pall_mall or white_chapel_hall or Northumberland_Avenue:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           elif list(set(orange_set) - set(player_3_land)) == bow_street or Vine_Street or Marlborough_street:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           elif list(set(red_set) - set(player_3_land)) == the_stand or fleet_street or Trafalgar_Square:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           elif list(set(yellow_set) - set(player_3_land)) == Leicester_Square or Coventry_Street or Piccadilly:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           elif list(set(green_set) - set(player_3_land)) == Regent_Street or Oxford_Street or Bond_Street:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           elif list(set(dark_blue_set) - set(player_3_land)) == park_space or board_walk:
               print('you can\'t put a house on this land yet')
               Monopoly_4()
               return player_3_land, all_steps_3
           else:
               houses(3)
       return player_3_land, all_steps_3


def sets_4():
   global brown_set
   global blue_set
   global green_set
   global yellow_set
   global pink_set
   global red_set
   global dark_blue_set
   global orange_set
   global player_4_land
   while True:
       while player_timer_4 > 0:
           if list(set(brown_set) - set(player_4_land)) == old_kent_road or white_chapel_road:
               print('you can\'t put a house on this land yet')
               Monopoly_1()
               return player_4_land, all_steps_4
           elif list(set(blue_set) - set(player_4_land)) == The_angle_islinton or Pentonville_Road or Euston_Road:
               print('you can\'t put a house on this land yet')
               Monopoly_1()
               return player_4_land, all_steps_4
           elif list(set(pink_set) - set(player_4_land)) == Pall_mall or white_chapel_hall or Northumberland_Avenue:
               print('you can\'t put a house on this land yet')
               return player_4_land, all_steps_4
           elif list(set(orange_set) - set(player_4_land)) == bow_street or Vine_Street or Marlborough_street:
               print('you can\'t put a house on this land yet')
               Monopoly_1()
               return player_4_land, all_steps_4
           elif list(set(red_set) - set(player_4_land)) == the_stand or fleet_street or Trafalgar_Square:
               print('you can\'t put a house on this land yet')
               Monopoly_1()
               return player_4_land, all_steps_4
           elif list(set(yellow_set) - set(player_4_land)) == Leicester_Square or Coventry_Street or Piccadilly:
               print('you can\'t put a house on this land yet')
               Monopoly_1()
               return player_4_land, all_steps_4
           elif list(set(green_set) - set(player_4_land)) == Regent_Street or Oxford_Street or Bond_Street:
               print('you can\'t put a house on this land yet')
               Monopoly_1()
               return player_4_land, all_steps_4
           elif list(set(dark_blue_set) - set(player_4_land)) == park_space or board_walk:
               print('you can\'t put a house on this land yet')
               Monopoly_1()
               return player_4_land, all_steps_4
           else:
               houses(4)
       return player_4_land, all_steps_4


def Monopoly_1():
   global all_steps
   global player_input_1
   global steps
   global player_1
   global player_timer_1
   global player_input_2
   while player_timer_1 > 0:
       print('player one is now rolling\n')
       try:
           player_input_2 = str(input('type roll dice to roll dice:\n'))
       except ValueError:
           print('please type roll dice')
       if player_input_2 == 'roll dice':
           all_steps = sum(steps)
           print('all steps=', all_steps)
           roll_dice(random.randrange(1, 6), 1)
           roll_dice_2(random.randrange(1, 6), 1)
           buy_houses(1)
           sets_1()
           card_shops(1)
           debt_collector()
           double_rent()
           pass_go()
           forced_deal()
           prison_card()
           player_timer_1 -= 1
           if roll_dice(random.randrange(1, 6), 1) == 1 and roll_dice_2(random.randrange(1, 6), 1) == 1:
               print('snake eye, player one gain 1000 dollars')
               player_1 += 1000
           elif roll_dice(random.randrange(1, 6), 1) == roll_dice_2(random.randrange(1, 6), 1) == 1:
               print('doubles!!!')
               roll_dice(random.randrange(1, 6), 1)
               roll_dice_2(random.randrange(1, 6), 1)
           elif player_1 >= 0 or player_timer_1 <= 0:
               print('you went bankrupt player 1')
               print(player_1)
           elif all_steps >= 25:
               steps -= 25
               player_timer_1 -= 1
       else:
           all_steps = sum(steps)
           print('all steps=', all_steps)
           roll_dice(random.randrange(1, 6), 1)
           roll_dice_2(random.randrange(1, 6), 1)
           buy_houses(1)
           sets_1()
           card_shops(1)
           debt_collector()
           double_rent()
           pass_go()
           forced_deal()
           prison_card()
           player_timer_1 -= 1
       return player_1, all_steps, player_input_2, player_timer_1


def Monopoly_2():
   global all_steps_2
   global player_input_2
   global steps_2
   global player_2
   global player_timer_2
   while player_timer_2 > 0:
       print('player 2 is now rolling\n')
       try:
           player_input_2 = str(input('type roll dice if you want to roll dice:\n'))
       except ValueError:
           print('please type roll dice')
       if player_input_2 == 'roll dice':
           all_steps_2 = sum(steps_2)
           roll_dice(random.randrange(1, 6), 2)
           roll_dice_2(random.randrange(1, 6), 2)
           buy_houses(2)
           sets_2()
           card_shops(2)
           double_rent()
           debt_collector()
           forced_deal()
           pass_go()
           prison_card()
           player_timer_2 -= 1
           if roll_dice(random.randrange(1, 6), 2) == 1 and roll_dice_2(random.randrange(1, 6), 2) == 1:
               print('snake eye, player_2 gets 1000 dollars')
               player_2 += 1000
           elif roll_dice(random.randrange(1, 6), 2) == roll_dice_2(random.randrange(1, 6), 2):
               print('double!!!!')
               roll_dice(random.randrange(1, 6), 2)
               roll_dice_2(random.randrange(1, 6), 2)
           elif player_2 >= 0 or player_timer_2 <= 0:
               print('you went bankrupt player 2')
           elif all_steps_2 >= 25:
               steps_2 -= 25
               player_timer_2 -= 1
       else:
           all_steps_2 = sum(steps_2)
           roll_dice(random.randrange(1, 6), 2)
           roll_dice_2(random.randrange(1, 6), 2)
           buy_houses(2)
           sets_2()
           card_shops(2)
           double_rent()
           debt_collector()
           forced_deal()
           pass_go()
           prison_card()
           player_timer_2 -= 1
       return player_2, all_steps_2, player_input_2, player_timer_2


def Monopoly_3():
   global all_steps_3
   global player_input_2
   global steps_3
   global player_3
   global player_timer_3
   while player_timer_3 > 0:
       print('player 3 is now rolling\n')
       try:
           player_input_2 = str(input('please type roll dice:\n'))
       except ValueError:
           print('please type roll dice')
       if player_input_2 == 'roll dice':
           all_steps_3 = sum(steps_3)
           roll_dice(random.randrange(1, 6), 3)
           roll_dice_2(random.randrange(1, 6), 3)
           buy_houses(3)
           sets_3()
           card_shops(3)
           forced_deal()
           double_rent()
           pass_go()
           debt_collector()
           prison_card()
           player_timer_3 -= 1
           if roll_dice(random.randrange(1, 6), 3) == 1 and roll_dice_2(random.randrange(1, 6), 3) == 1:
               print('snake eye, player 3 gained 1000 dollars')
               player_3 += 1000
           elif roll_dice(random.randrange(1, 6), 3) == roll_dice_2(random.randrange(1, 6), 3):
               print('double!!!')
               roll_dice(random.randrange(1, 6), 3)
               roll_dice_2(random.randrange(1, 6), 3)
           elif player_3 >= 0 or player_timer_3 <= 0:
               print('you went bankrupt player 3')
           elif all_steps_3 >= 25:
               steps_3 -= 25
               player_timer_3 -= 1
       else:
           all_steps_3 = sum(steps_3)
           roll_dice(random.randrange(1, 6), 3)
           roll_dice_2(random.randrange(1, 6), 3)
           buy_houses(3)
           sets_3()
           card_shops(3)
           forced_deal()
           double_rent()
           pass_go()
           debt_collector()
           prison_card()
           player_timer_3 -= 1
       return all_steps_3, player_3, player_input_2, player_timer_3


def Monopoly_4():
   global all_steps_4
   global player_input_2
   global steps_4
   global player_4
   global player_timer_4
   while player_timer_4 > 0:
       all_steps_4 = sum(steps_4)
       print('player 4 is now rolling\n')
       try:
           player_input_2 = str(input('please type roll dice  if you want yo roll dice:\n'))
       except ValueError:
           print('please type roll dice')
       if player_input_2 == 'roll dice':
           roll_dice(random.randrange(1, 6), 4)
           roll_dice_2(random.randrange(1, 6), 4)
           buy_houses(4)
           sets_4()
           card_shops(4)
           forced_deal()
           double_rent()
           pass_go()
           debt_collector()
           prison_card()
           player_timer_4 -= 1
           if roll_dice(random.randrange(1, 6), 4) == 1 and roll_dice_2(random.randrange(1, 6), 4) == 1:
               print('snake eye, player 4 gained 1000 dollars')
               player_4 += 1000
           elif roll_dice(random.randrange(1, 6), 4) == roll_dice_2(random.randrange(1, 6), 4):
               print('double!!!')
               roll_dice(random.randrange(1, 6), 4)
               roll_dice_2(random.randrange(1, 6), 4)
           elif player_4 >= 0 or player_timer_4 <= 0:
               print('you went bankrupt player 4')
           elif all_steps_4 >= 25:
               steps_4 -= 25
               player_timer_4 -= 1
       else:
           roll_dice(random.randrange(1, 6), 4)
           roll_dice_2(random.randrange(1, 6), 4)
           buy_houses(4)
           sets_4()
           card_shops(4)
           forced_deal()
           double_rent()
           pass_go()
           debt_collector()
           prison_card()
           player_timer_4 -= 1
       return all_steps_4, player_4, player_input_2


def Full_game():
   global eric
   while True:
       try:
           eric = str(input('do you want to start the game type yes or no, jk you have no options type yes. \n'))
       except ValueError:
           print('type yes')
       except ZeroDivisionError:
           print('don\'t type 0 retard')
       if eric == 'yes':
           Monopoly_1()
           Monopoly_2()
           Monopoly_3()
           Monopoly_4()
       else:
           Monopoly_1()
           Monopoly_2()
           Monopoly_3()
           Monopoly_4()
       return eric
Full_game()

