server_config = {
    "天空岛 + 米哈游通行证": 1,
    "世界树 + BiliBili账号": 2,
    # "tw/hk/mo + HoYoverse通行证": 3,
}

channels = {
    1 : {"cps": "hyp_mihoyo", "channel": 1, "sub_channel": 0,
         "uapc": '{"hk4e_cn":{"uapc":""},"hyp":{"uapc":""}}'}, # 天空岛 + 米哈游通行证
    2 : {"cps": "bilibili", "channel": 14, "sub_channel": 1,
         "uapc": '{"hk4e_cn":{"uapc":""},"hyp":{"uapc":""}}'}, # 世界树 + BiliBili账号
    # 3 : {"cps": "hoyoverse", "channel": 1, "sub_channel": 0,
    #      "uapc": '{"hk4e_global":{"uapc":"f8a4a729f5bd_"},"hyp":{"uapc":"f8a4a729f5bd_"}}'}, # TW/HK/MO + HoYoverse通行证
}

file_name_set ={
    0 : {"_Data_folder": "YuanShen_Data", "game.exe": "YuanShen.exe", "game.exe.lnk": "YuanShen.exe.lnk"},
    1 : {"_Data_folder": "GenshinImpact_Data", "game.exe": "GenshinImpact.exe", "game.exe.lnk": "GenshinImpact.exe.lnk"},
}