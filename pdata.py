from thinc.mypy import plugin

server_config = {
    "天空岛 + 米哈游通行证": 1,
    "世界树 + BiliBili账号": 2,
    # "tw/hk/mo + HoYoverse通行证": 3,
}

channels = {
    1 : {"channel": 1,
         "sub_channel": 1,
         "cps": "mihoyo PC",
         "uapc": '{"hk4e_cn":{"uapc":""},"hyp":{"uapc":""}}',
         "plugin sdk version": ""}, # 天空岛 + 米哈游通行证
    2 : {"channel": 14,
         "sub_channel": 0,
         "cps": "bilibili",
         "uapc": '{"hk4e_cn":{"uapc":""},"hyp":{"uapc":""}}',
         "plugin sdk version": "5.0.4"}, # 世界树 + BiliBili账号
}

file_name_set ={
    0 : {"_Data_folder": "YuanShen_Data", "game.exe": "YuanShen.exe", "game.exe.lnk": "YuanShen.exe.lnk"},
    1 : {"_Data_folder": "GenshinImpact_Data", "game.exe": "GenshinImpact.exe", "game.exe.lnk": "GenshinImpact.exe.lnk"},
}