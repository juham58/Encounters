from CR_Finder import CR_Finder
from EncounterBuilder import EncounterBuilder


def find_cr_atk_bonus(ac=10, hp=10, atk_bonus=3):
    finder = CR_Finder()
    finder.avg_dice(2, 6, 0)
    finder.avg_dice_collector()
    finder.cr_from_hp(hp)
    finder.cr_from_ac(ac)
    finder.cr_from_dmg()
    finder.cr_from_atk_bonus(atk_bonus)
    return finder.get_final_cr()


def find_cr_save_dc(ac=10, hp=10, save_dc=10, tier=1, resistances=False, immunities=False):
    finder = CR_Finder()
    finder.avg_dice(3, 6, 5)
    finder.avg_dice_collector()
    finder.set_tier(1)
    finder.set_immunities(True)
    finder.cr_from_hp(hp)
    finder.cr_from_ac(ac)
    finder.cr_from_dmg()
    finder.cr_from_atk_bonus(save_dc)
    return finder.get_final_cr()


test = EncounterBuilder()
players_dmg = CR_Finder()
players_dmg.avg_dice(1, 8, 3)
players_dmg.avg_dice(1, 6, 3)
players_dmg.avg_dice(1, 12, 0)
players_dmg.avg_dice(1, 10, 3)
players_dmg.avg_dice(1, 10, 3)
players_dmg.avg_dice(1, 6, 0)
players_dmg.avg_dice(1, 6, 0)
players_dmg.avg_dice_collector()

#test.add_party(1, 6)

#  test.add_monster(find_cr_save_dc(ac=18, hp=300, save_dc=18, tier=3, immunities=True))
#test.add_monster(find_cr_atk_bonus(ac=18, hp=100, atk_bonus=7))
#test.get_difficulty()