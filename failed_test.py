import time
import random
import color_const
import sys

dummy_plot_list_with_percantage = [
    color_const.pycolor.GREEN + "[Test1]NetworkManager.GetAccessToken" + color_const.pycolor.END,
    ":==                  :10% completed...",
    ":====                :20% completed...",
    ":======              :30% completed...",
    ":========            :40% completed...",
    ":==========          :50% completed...",
    ":============        :60% completed...",
    ":==============      :70% completed...",
    ":================    :80% completed...",
    color_const.pycolor.RED + "FAILED!!\n"
    "Failed to get access token.\n"
    "Valid access token is not found. Please check server status or other environment settings." + color_const.pycolor.END,
    color_const.pycolor.GREEN + "[Test2]PlayerAccountManager.ExistValidAccount" + color_const.pycolor.END,
    ":==                  :10% completed...",
    ":====                :20% completed...",
    ":======              :30% completed...",
    color_const.pycolor.RED + "FAILED!!\n"
    "The given player account does NOT exist in player_db.\n"
    "Kill this process. Try again." + color_const.pycolor.RED,
    color_const.pycolor.GREEN + "[Test3]BattleLogic.DoSpecialAttack" + color_const.pycolor.END,
    ":==                  :10% completed...",
    ":====                :20% completed...",
    ":======              :30% completed...",
    ":========            :40% completed...",
    ":==========          :50% completed...",
    ":============        :60% completed...",
    ":==============      :70% completed...",
    color_const.pycolor.RED + "FAILED!!\n"
    "Uncought exception was detected.\n"
    "There is not skill called battle_special_skill_1 for player_1323." + color_const.pycolor.END,
]

dummy_plot_list_without_percentage = [
    color_const.pycolor.GREEN + "[Test1]NetworkManager.GetAccessToken" + color_const.pycolor.END,
    ":==                  :",
    ":====                :",
    ":======              :",
    ":========            :",
    ":==========          :",
    ":============        :",
    ":==============      :",
    ":================    :",
    color_const.pycolor.RED + "FAILED!!\n"
    "Failed to get access token.\n"
    "Valid access token is not found. Please check server status or other environment settings." + color_const.pycolor.END,
    color_const.pycolor.GREEN + "[Test2]PlayerAccountManager.ExistValidAccount" + color_const.pycolor.END,
    ":==                  :",
    ":====                :",
    ":======              :",
    color_const.pycolor.RED + "FAILED!!\n"
    "The given player account does NOT exist in player_db.\n"
    "Kill this process. Try again." + color_const.pycolor.RED,
    color_const.pycolor.GREEN + "[Test3]BattleLogic.DoSpecialAttack" + color_const.pycolor.END,
    ":==                  :",
    ":====                :",
    ":======              :",
    ":========            :",
    ":==========          :",
    ":============        :",
    ":==============      :",
    color_const.pycolor.RED + "FAILED!!\n"
    "Uncought exception was detected.\n"
    "There is not skill called battle_special_skill_1 for player_1323." + color_const.pycolor.END,
]

dummy_plot_list_only_description = [
    color_const.pycolor.GREEN + "[Test1]NetworkManager.GetAccessToken" + color_const.pycolor.END,
    color_const.pycolor.RED + "FAILED!!\n"
    "Failed to get access token.\n"
    "Valid access token is not found. Please check server status or other environment settings." + color_const.pycolor.END,
    color_const.pycolor.GREEN + "[Test2]PlayerAccountManager.ExistValidAccount" + color_const.pycolor.END,
    color_const.pycolor.RED + "FAILED!!\n"
    "The given player account does NOT exist in player_db.\n"
    "Kill this process. Try again." + color_const.pycolor.RED,
    color_const.pycolor.GREEN + "[Test3]BattleLogic.DoSpecialAttack" + color_const.pycolor.END,
    color_const.pycolor.RED + "FAILED!!\n"
    "Uncought exception was detected.\n"
    "There is not skill called battle_special_skill_1 for player_1323." + color_const.pycolor.END,
]

version = int(sys.argv[1])
if version == 0:
    for i in dummy_plot_list_with_percantage:
        print(i)
        time.sleep(random.random())
elif version == 1:
    for i in dummy_plot_list_without_percentage:
        print(i)
        time.sleep(random.random())
elif version == 2:
    for i in dummy_plot_list_only_description:
        print(i)
        time.sleep(random.random())
else:
    print("その引数に該当する処理はありません。")