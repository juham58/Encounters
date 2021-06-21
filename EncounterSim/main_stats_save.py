from Stats_Module import MainStats
import random

save = MainStats()
save.set_main_stats("Goblin", ac=15, hp=7, attack_mod=4)
save.add_avg_dmg(1, 6, 2)
save.set_abilities(-1, 2, 0, 0, -1, -1)
save.set_saves(-1, 2, 0, 0, -1, -1)
save.set_action(action_type="melee", name="Scimitar", dice_rolls=[(1,6,2)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Skeleton", ac=13, hp=13, attack_mod=4)
save.add_avg_dmg(1, 6, 2)
save.set_abilities(0, 2, 2, -2, -1, -3)
save.set_saves(0, 2, 2, -2, -1, -3)
save.set_action(action_type="melee", name="Shortsword", dice_rolls=[(1,6,2)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("John", ac=17, hp=92, dc=15, ini_mod=5, attack_mod=10, number_of_attacks=2, is_monster=False)
save.add_avg_dmg(1, 8, 8)
save.add_avg_dmg(1, 6, 0) # Rite of the dawn
save.set_abilities(0, 5, 1, 3, 0, -1)
save.set_saves(0, 9, 1, 7, 0, -1)
save.set_action(action_type="melee", name="Rapier, +1", dice_rolls=[(1,8,8), (1,6,0)])
save.set_action(action_type="melee", name="Rapier, +1", dice_rolls=[(1,8,8), (1,6,0)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Faramir", ac=18, hp=87, dc=16, ini_mod=0, attack_mod=10, number_of_attacks=2, is_monster=False)
save.add_avg_dmg(1, 10, 4)
save.add_avg_dmg(2, 8, 0) # Si divine smite lvl 1 à chaque attaque
save.set_abilities(4, 0, 2, 0, -1, 4)
save.set_saves(8, 4, 6, 4, 7, 12)
save.set_action(action_type="melee", name="Meteor Core Halberd", dice_rolls=[(1,10,6), (2,8,0)])
save.set_action(action_type="melee", name="Meteor Core Halberd", dice_rolls=[(1,10,6), (2,8,0)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Augustin", ac=23, hp=61, dc=17, ini_mod=2, attack_mod=10, number_of_attacks=2, is_monster=False)
save.add_avg_dmg(1, 6, 6)
save.add_avg_dmg(0, 0, 5) # Estimation du dommage bonus pour sharpshooter
save.set_abilities(4, 2, 1, 5, 0, 1)
save.set_saves(4, 2, 5, 9, 0, 1)
save.set_action(action_type="melee", name="Lightning Launcher", dice_rolls=[(1,6,11)])
save.set_action(action_type="melee", name="Lightning Launcher", dice_rolls=[(1,6,11)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Rand al'Thor", ac=16, hp=88, dc=17, ini_mod=3, attack_mod=10, number_of_attacks=2, is_monster=False)
save.add_avg_dmg(2, 6, 6)
save.add_avg_dmg(1, 10, 0) # estimation du bonus dommage pour différents spells de warlock i guess
save.set_abilities(-1, 3, 2, -1, 1, 5)
save.set_saves(-1, 3, 2, -1, 5, 9)
save.set_action(action_type="melee", name="Greatsword, +1", dice_rolls=[(2,6,6), (1,10,0)])
save.set_action(action_type="melee", name="Greatsword, +1", dice_rolls=[(2,6,6), (1,10,0)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Victoriana", ac=16, hp=60, dc=17, ini_mod=8, attack_mod=10, number_of_attacks=1, is_monster=False) # avec mage armor
save.add_avg_dmg(7, 8, 0) # basé sur Chromatic orb lvl 5
save.set_abilities(-1, 3, 1, 5, 1, 0)
save.set_saves(-1, 3, 1, 9, 5, 0)
save.set_action(action_type="ranged", name="Level 4 Scorching Ray", dice_rolls=[(2,6,0)])
save.set_action(action_type="ranged", name="Level 4 Scorching Ray", dice_rolls=[(2,6,0)])
save.set_action(action_type="ranged", name="Level 4 Scorching Ray", dice_rolls=[(2,6,0)])
save.set_action(action_type="ranged", name="Level 4 Scorching Ray", dice_rolls=[(2,6,0)])
save.set_action(action_type="ranged", name="Level 4 Scorching Ray", dice_rolls=[(2,6,0)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Dorran", ac=15, hp=107, dc=12, ini_mod=1, attack_mod=4, number_of_attacks=3, is_monster=False) # basé sur Giant Scorpion
save.add_avg_dmg(1, 8, 2)
save.add_avg_dmg(2, 10, 0) # estimation du 4d10 si la moitié du monde save le jet de con
save.set_abilities(2, 1, 2, 3, 4, -1)
save.set_saves(2, 1, 2, 7, 8, -1)
save.set_action(action_type="melee", name="Claw", dice_rolls=[(1,8,2)], condition="Grappled", auto_success=True, dc_type="str")
save.set_action(action_type="melee", name="Claw", dice_rolls=[(1,8,2)], condition="Grappled", auto_success=True, dc_type="str")
save.set_action(action_type="melee", name="Sting", dice_rolls=[(1,10,2)], has_dc_effect_on_hit=True, dc_type="con", dc_effect_on_hit=[(4,10,0)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Hobgoblin Captain", ac=17, hp=39, attack_mod=6, number_of_attacks=2)
save.add_avg_dmg(2, 6, 2)
save.add_avg_dmg(2, 4, 0)
save.set_abilities(2, 2, 2, 1, 0, 1)
save.set_saves(2, 2, 2, 1, 0, 1)
save.set_action(action_type="melee", name="Greatsword", dice_rolls=[(2,6,2), (3,6,0)])
save.set_action(action_type="melee", name="Greatsword", dice_rolls=[(2,6,2)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Core Spawn Seer", ac=17, hp=153, ini_mod=1, attack_mod=8, number_of_attacks=2, dc=19)
save.add_avg_dmg(1, 6, 6+2) # Utilise seulement son attaque melee. +2 pour prendre en compte les debuff
save.add_avg_dmg(4, 8, 0)
save.set_abilities(2, 1, 4, 6, 4, 3)
save.set_saves(2, 6, 2, 11, 9, 8)
save.set_action(action_type="melee", name="Fission Staff", dice_rolls=[(1,6,6), (4,8,0), (1,6,0)], condition="Prone", auto_success=True)
save.set_action(action_type="ranged", name="Psychedelic Orb", dice_rolls=[(5,10,0)], has_dc=True, has_attack_mod=False, dc_type="wis", condition=random.choice(["Blinded", "Frightened", "Stunned"]), if_save="no_damage")
save.save_main_stats()

save = MainStats()
save.set_main_stats("Core Spawn Crawler", ac=12, hp=21, ini_mod=2, attack_mod=4, number_of_attacks=4, dc=11)
save.add_avg_dmg(1, 4, 2) # Dommage moyen un peu moins bon que l'attaque Tail
save.set_abilities(-2, 2, 0, -1, 1, -2)
save.set_saves(-2, 2, 0, -1, 1, -2)
save.set_action(action_type="melee", name="Bite", dice_rolls=[(1,4,2)], has_dc_effect_on_hit=True, dc_effect_on_hit=[(0,0,0)], condition="Frightened", dc_type="wis", has_advantage=True)
save.set_action(action_type="melee", name="Claws", dice_rolls=[(1,4,2)], has_advantage=True)
save.set_action(action_type="melee", name="Claws", dice_rolls=[(1,4,2)], has_advantage=True)
save.set_action(action_type="melee", name="Tail", dice_rolls=[(1,6,2)], has_advantage=True)
save.save_main_stats()

save = MainStats()
save.set_main_stats("Gorgak Gro'brah", ac=17, hp=155, ini_mod=5, attack_mod=11, number_of_attacks=2, is_monster=False)
save.add_avg_dmg(1, 10, 16) # Bonus de rage + dvivine fury divisée par 2
save.set_abilities(5, 2, 5, 1, 1, 2)
save.set_saves(9, 2, 9, 1, 1, 2)
save.set_action(action_type="melee", name="Meteor Core Halberd", dice_rolls=[(1,10,10), (1,6,4)])
save.set_action(action_type="melee", name="Meteor Core Halberd", dice_rolls=[(1,10,10)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Ewyn", ac=17, hp=18, ini_mod=-1, attack_mod=5, number_of_attacks=1, is_monster=False)
save.add_avg_dmg(1, 12, 3)
save.set_abilities(3, -1, 3, 0, 0, 2)
save.set_saves(3, -1, 3, 0, 2, 4)
save.set_action(action_type="melee", name="Greataxe", dice_rolls=[(1,12,3)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Gowon", ac=13, hp=18, ini_mod=2, attack_mod=5, number_of_attacks=1, is_monster=False, dc=13)
save.add_avg_dmg(1, 10, 0)
save.set_abilities(0, 2, 3, -1, 1, 3)
save.set_saves(0, 2, 3, -1, 3, 5)
save.set_action(action_type="range", name="Eldritch Blast", dice_rolls=[(1,10,0)]) # Eyldritch Bleaaaaassssttt
save.save_main_stats()

save = MainStats()
save.set_main_stats("Iaachus", ac=15, hp=26, ini_mod=2, attack_mod=5, number_of_attacks=1, is_monster=False)
save.add_avg_dmg(2, 6, 3)
save.set_abilities(3, 2, 3, -1, -1, 1)
save.set_saves(5, 2, 5, -1, -1, 1)
save.set_action(action_type="melee", name="Greatsword", dice_rolls=[(2,6,3)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Melvin", ac=13, hp=22, ini_mod=0, attack_mod=5, number_of_attacks=1, is_monster=False)
save.add_avg_dmg(4, 6, 0)
save.set_abilities(-1, 0, 1, 3, 3, 1)
save.set_saves(-1, 0, 1, 3, 5, 3)
save.set_action(action_type="ranged", name="Guiding Bolt", dice_rolls=[(4,6,0)], damage_type="radiant")
save.save_main_stats()

save = MainStats()
save.set_main_stats("Reaghan", ac=12, hp=22, ini_mod=1, attack_mod=5, number_of_attacks=1, is_monster=False, dc=13)
save.add_avg_dmg(3, 6, 0)
save.set_abilities(0, 1, 3, 0, -1, 3)
save.set_saves(0, 3, 3, 0, -1, 5)
save.set_action(action_type="ranged", name="Dissonant Whispers", dice_rolls=[(3,6,0)], has_dc=True, dc_type="wis", has_attack_mod=False, damage_type="psychic")
save.save_main_stats()

save = MainStats()
save.set_main_stats("Vilgefortz", ac=14, hp=13, ini_mod=3, attack_mod=5, number_of_attacks=1, is_monster=False)
save.add_avg_dmg(1, 8, 3)
save.add_avg_dmg(1, 6, 0)
save.set_abilities(-1, 3, 0, 2, 0, 3)
save.set_saves(-1, 5, 0, 4, 0, 3)
save.set_action(action_type="melee", name="Rapier", dice_rolls=[(1,8,3),(1,6,0)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Thug", ac=11, hp=32, attack_mod=4)
save.add_avg_dmg(1, 6, 2)
save.set_abilities(2, 0, 2, 0, 0, 0)
save.set_saves(2, 0, 2, 0, 0, 0)
save.set_action(action_type="melee", name="Mace", dice_rolls=[(1,6,2)], has_advantage=True) # approx que Pack Tactics est toujours vrai
save.save_main_stats()

save = MainStats()
save.set_main_stats("Stone Golem", ac=17, hp=178, attack_mod=10, number_of_attacks=2)
save.add_avg_dmg(3, 8, 6)
save.set_abilities(6, -1, 5, -4, 0, -5)
save.set_saves(6, -1, 5, -4, 0, -5)
save.set_action(action_type="melee", name="Slam", dice_rolls=[(3,8,6)]) # on oublie l'abilité Slow
save.set_action(action_type="melee", name="Slam", dice_rolls=[(3,8,6)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Iron Golem", ac=20, hp=210, attack_mod=13, number_of_attacks=2)
save.add_avg_dmg(3, 8, 7)
save.set_abilities(6, -1, 5, -4, 0, -5)
save.set_saves(6, -1, 5, -4, 0, -5)
save.set_action(action_type="melee", name="Slam", dice_rolls=[(3,8,7)]) # on oublie l'abilité Poison Breath
save.set_action(action_type="melee", name="Sword", dice_rolls=[(3,10,7)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Gold-Forged Sentinel", ac=16, hp=76, attack_mod=7, number_of_attacks=2)
save.add_avg_dmg(3, 8, 7)
save.set_abilities(4, 1, 4, -4, 3, 0)
save.set_saves(4, 1, 4, -4, 3, 0)
save.set_action(action_type="melee", name="Ram", dice_rolls=[(2,8,4)]) # on oublie l'abilité Fire Breath, Charge et Spell Turning
save.set_action(action_type="melee", name="Ram", dice_rolls=[(2,8,4)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Shadow Rand", ac=16, hp=38, dc=17, ini_mod=3, attack_mod=10, number_of_attacks=2)
save.add_avg_dmg(2, 6, 6)
save.add_avg_dmg(1, 10, 0) # estimation du bonus dommage pour différents spells de warlock i guess
save.set_abilities(-1, 5, -1, -1, 0, 5)
save.set_saves(-1, 5, -1, -1, 4, 9)
save.set_action(action_type="melee", name="Ruin's Wake", dice_rolls=[(3,8,9)]) # 3d8 sur chaque attaque pour approximer l'attaque en réaction
save.set_action(action_type="melee", name="Ruin's Wake", dice_rolls=[(3,8,9)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Demetriu", ac=18, hp=40, dc=15, ini_mod=5, attack_mod=9, number_of_attacks=4)
save.add_avg_dmg(2, 6, 6)
save.set_abilities(-1, 5, 3, 0, 3, 2)
save.set_saves(3, 9, 3, 0, 3, 2)
save.set_action(action_type="melee", name="Mace", dice_rolls=[(1,6,3)], has_advantage=True)
save.set_action(action_type="melee", name="Mace", dice_rolls=[(1,6,3)])
save.set_action(action_type="melee", name="Unarmed Strike", dice_rolls=[(1,6,3)])
save.set_action(action_type="melee", name="Unarmed Strike", dice_rolls=[(1,6,3)])
save.save_main_stats()

save = MainStats()
save.set_main_stats("Loup Garou", ac=16, hp=170, dc=17, ini_mod=4, attack_mod=9, number_of_attacks=2, regeneration=10, legend_actions_charges=3)
save.add_avg_dmg(2, 6, 6)
save.set_abilities(4, 4, 4, 2, 3, 3)
save.set_saves(4, 9, 9, 2, 3, 8)
save.set_action(action_type="melee", name="Bite", dice_rolls=[(2,8,4), (4,6,0)], has_advantage=True)
save.set_action(action_type="melee", name="Claws", dice_rolls=[(2,6,4)], has_advantage=True, has_dc_effect_on_hit=True, condition="Prone", dc_type="str")
save.set_legend_action(action_type="melee", charge_cost=1, name="Swipe", dice_rolls=[(2,6,4)], has_advantage=True, has_dc_effect_on_hit=True, condition="Prone", dc_type="str")
save.save_main_stats()

save = MainStats()
save.set_main_stats("Werewolf", ac=12, hp=58, dc=12, ini_mod=1, attack_mod=4, number_of_attacks=2)
save.add_avg_dmg(2, 6, 6)
save.set_abilities(2, 1, 2, 0, 0, 0)
save.set_saves(2, 1, 2, 0, 0, 0)
save.set_action(action_type="melee", name="Bite", dice_rolls=[(1,8,2)])
save.set_action(action_type="melee", name="Claws", dice_rolls=[(2,4,2)])
save.save_main_stats()