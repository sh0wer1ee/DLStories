import json

swapLangTable = {"en_us": "ENUS", "ja_jp": "JP", "zh_cn": "ZHCN", "zh_tw": "ZHTW"}
swapLangTable2 = {"ENUS": "en_us", "JP": "ja_jp", "ZHCN": "zh_cn", "ZHTW": "zh_tw"}
storyDataJsonCN = json.load(open("stories_noascii/index.json", "r", encoding="utf-8"))
textlabelJson = json.load(open("TextLabel20220725.json", "r", encoding="utf-8"))
charadataJson = json.load(open("json/CharaData.json", "r", encoding="utf-8"))
dragondataJson = json.load(open("json/DragonData.json", "r", encoding="utf-8"))
specialEventDic = {
    "21001": {
        "zh_cn": "真耶梦加得的试炼",
        "zh_tw": "真‧耶夢加得的試煉",
        "ja_jp": "真ミドガルズオルムの試練",
        "en_us": "High Midgardsormr's Trial",
    },
    "21002": {
        "zh_cn": "真墨丘利的试炼",
        "zh_tw": "真‧墨丘利的試煉",
        "ja_jp": "真マーキュリーの試練",
        "en_us": "High Mercury's Trial",
    },
    "21003": {
        "zh_cn": "真布伦希尔德的试炼",
        "zh_tw": "真‧布倫希爾德的試煉",
        "ja_jp": "真ブリュンヒルデの試練",
        "en_us": "High Brunhilda's Trial",
    },
    "21004": {
        "zh_cn": "真朱庇特的试炼",
        "zh_tw": "真‧朱庇特的試煉",
        "ja_jp": "真ユピテルの試練",
        "en_us": "High Jupiter's Trial",
    },
    "21005": {
        "zh_cn": "真佐迪亚克的试炼",
        "zh_tw": "真‧索狄亞克的試煉",
        "ja_jp": "真ゾディアークの試練",
        "en_us": "High Zodiark's Trial",
    },
    "21601": {
        "zh_cn": "宝龙之挑战",
        "zh_tw": "寶龍的挑戰",
        "ja_jp": "宝竜の挑戦",
        "en_us": "The Mercurial Gauntlet",
    },
    "21900": {
        "zh_cn": "阿基德叛乱战",
        "zh_tw": "咢牙叛逆戰",
        "ja_jp": "アギト叛逆戦",
        "en_us": "The Agito Uprising",
    },
    "21901": {
        "zh_cn": "卢弗·托修卡特尔叛乱战",
        "zh_tw": "路弗‧特修加德魯叛逆戰",
        "ja_jp": "ルヴ・トシュカトル叛逆戦",
        "en_us": "Volk's Wrath",
    },
    "21902": {
        "zh_cn": "凯严叛乱战",
        "zh_tw": "凱嚴叛逆戰",
        "ja_jp": "ガイエン叛逆戦",
        "en_us": "Kai Yan's Wrath",
    },
    "21903": {
        "zh_cn": "谢希耶尔叛乱战",
        "zh_tw": "雪爾希爾叛逆戰",
        "ja_jp": "シェルシエル叛逆戦",
        "en_us": "Ciella's Wrath",
    },
    "21904": {
        "zh_cn": "彩羽&乙羽叛乱战",
        "zh_tw": "彩羽＆乙羽叛逆戰",
        "ja_jp": "アヤハ＆オトハ叛逆戦",
        "en_us": "Ayaha & Otoha's Wrath",
    },
    "21905": {
        "zh_cn": "塔耳塔洛斯叛乱战",
        "zh_tw": "塔爾塔羅斯叛逆戰",
        "ja_jp": "タルタロス叛逆戦",
        "en_us": "Tartarus's Wrath",
    },
    "22801": {
        "zh_cn": "天魔封灭战 风之章",
        "zh_tw": "厄魔封滅戰　風之章",
        "ja_jp": "ディアボロス封滅戦 風の章",
        "en_us": "Jaldabaoth's Piercing Gale",
    },
    "22802": {
        "zh_cn": "天魔封灭战 水之章",
        "zh_tw": "厄魔封滅戰　水之章",
        "ja_jp": "ディアボロス封滅戦 水の章",
        "en_us": "Iblis's Surging Cascade",
    },
    "22803": {
        "zh_cn": "天魔封灭战 火之章",
        "zh_tw": "厄魔封滅戰　火之章",
        "ja_jp": "ディアボロス封滅戦 火の章",
        "en_us": "Surtr's Devouring Flame",
    },
    "22804": {
        "zh_cn": "天魔封灭战 光之章",
        "zh_tw": "厄魔封滅戰　光之章",
        "ja_jp": "ディアボロス封滅戦 光の章",
        "en_us": "Asura's Blinding Light",
    },
    "22805": {
        "zh_cn": "天魔封灭战 暗之章",
        "zh_tw": "厄魔封滅戰　闇之章",
        "ja_jp": "ディアボロス封滅戦 闇の章",
        "en_us": "Lilith's Encroaching Shadow",
    },
    "22800": {
        "zh_cn": "天魔封灭战",
        "zh_tw": "厄魔封滅戰",
        "ja_jp": "ディアボロス封滅戦",
        "en_us": "Rise of the Sinister Dominion",
    },
    "21304": {
        "zh_cn": "情人节·甜美佳肴 追加剧情",
        "zh_tw": "情人節‧精巧甜品　追加劇情",
        "ja_jp": "バレンタイン・アラカルト エクストラ",
        "en_us": "Valentine's Confections Extra",
    },
    "23101": {
        "zh_cn": "梦幻万花宫 华丽迷宫",
        "zh_tw": "萬花筒迷宮 カレイドラビリンス",
        "ja_jp": "夢幻の万華宮",
        "en_us": "Kaleidoscape",
    },
    "23300": {
        "zh_cn": "传奇龙之试炼",
        "zh_tw": "傳奇‧龍族的試煉",
        "ja_jp": "サガドラゴンの試練",
        "en_us": "Primal Dragon Trials",
    },
    "23301": {
        "zh_cn": "传奇耶梦加得的试炼",
        "zh_tw": "傳奇‧耶夢加得的試煉",
        "ja_jp": "ミドガルズオルムサガの試練",
        "en_us": "Primal Midgardsormr's Trial",
    },
    "23302": {
        "zh_cn": "传奇墨丘利的试炼",
        "zh_tw": "傳奇‧墨丘利的試煉",
        "ja_jp": "マーキュリーサガの試練",
        "en_us": "Primal Mercury's Trial",
    },
    "23303": {
        "zh_cn": "传奇布伦希尔德得的试炼",
        "zh_tw": "傳奇‧布倫希爾德的試煉",
        "ja_jp": "ブリュンヒルデサガの試練",
        "en_us": "Primal Brunhilda's Trial",
    },
    "23304": {
        "zh_cn": "传奇朱庇特的试炼",
        "zh_tw": "傳奇‧朱庇特的試煉",
        "ja_jp": "ユピテルサガの試練",
        "en_us": "Primal Jupiter's Trial",
    },
    "23305": {
        "zh_cn": "传奇佐迪亚克的试炼",
        "zh_tw": "傳奇‧索狄亞克的試煉",
        "ja_jp": "ゾディアークサガの試練",
        "en_us": "Primal Zodiark's Trial",
    },
}
speicalStoryDic = {
    "23101001": {
        "en_us": "The Pact of Inception",
        "ja_jp": "はじまりの契約",
        "zh_cn": "起始之约",
        "zh_tw": "起始之約",
    },
    "23101002": {
        "en_us": "The Primordial Dragons",
        "ja_jp": "原初のドラゴン",
        "zh_cn": "原初之龙",
        "zh_tw": "原初之龍",
    },
    "23101003": {
        "en_us": "Dragonblood Kingdom",
        "ja_jp": "竜の血の王国",
        "zh_cn": "龙之血的王国",
        "zh_tw": "龍之血的王國",
    },
    "23101004": {
        "en_us": "Harmony",
        "ja_jp": "人と竜の調和",
        "zh_cn": "人龙和谐",
        "zh_tw": "人與龍之調和",
    },
    "23101005": {
        "en_us": "Corrosive Hatred",
        "ja_jp": "侵食する憎悪",
        "zh_cn": "憎恶侵蚀",
        "zh_tw": "憎恨的侵蝕",
    },
    "23101006": {
        "en_us": "Faeries and Agito",
        "ja_jp": "妖精のアギト",
        "zh_cn": "精灵与阿基德",
        "zh_tw": "妖精與咢牙",
    },
    "23101007": {
        "en_us": "Dragonblood and Fragments of the Mark",
        "ja_jp": "刻印の欠片、竜の血",
        "zh_cn": "刻印残片与龙之血",
        "zh_tw": "刻印碎片、龍之血",
    },
    "23101008": {
        "en_us": "The Many Worlds of the Auspex",
        "ja_jp": "あまた世界の巫女",
        "zh_cn": "万千世界的巫女",
        "zh_tw": "萬千世界的巫女",
    },
    "23101009": {
        "en_us": "The Shogun of Hinomoto",
        "ja_jp": "日ノ下に侍る将軍",
        "zh_cn": "侍日出之将军",
        "zh_tw": "侍奉日下之將軍",
    },
    "23101010": {
        "en_us": "The Era of the Qilin",
        "ja_jp": "キリンの時代",
        "zh_cn": "麒麟族的时代",
        "zh_tw": "麒麟時代",
    },
    "23101011": {
        "en_us": "Those of the Sea",
        "ja_jp": "海竜と海底の民",
        "zh_cn": "海龙与海洋之民",
        "zh_tw": "海龍與海底子民",
    },
    "23101012": {
        "en_us": "The Sandreach Eternal",
        "ja_jp": "永遠なる砂の国",
        "zh_cn": "永恒的沙之国",
        "zh_tw": "永恆的沙之國",
    },
    "23101013": {
        "en_us": "From Automaton to Android",
        "ja_jp": "自動人形から戦闘人形へ",
        "zh_cn": "自动人偶与战斗人偶",
        "zh_tw": "從自動人偶到戰鬥人偶",
    },
    "23101014": {
        "en_us": "Demons of Possibility",
        "ja_jp": "可能性の悪魔",
        "zh_cn": "可能性的恶魔",
        "zh_tw": "可能性的惡魔",
    },
    "23101015": {
        "en_us": "The Archangel Metatron",
        "ja_jp": "大天使メタトロン",
        "zh_cn": "大天使梅塔特隆",
        "zh_tw": "大天使梅塔特隆",
    },
    "23101016": {
        "en_us": "From Love to Perdition",
        "ja_jp": "母の愛は煉獄へ",
        "zh_cn": "母爱与炼狱之名",
        "zh_tw": "母愛淪為煉獄",
    },
    "23101017": {
        "en_us": "Born of Piety",
        "ja_jp": "ディアネルは敬虔なるが故に",
        "zh_cn": "皆因狄涅尔的虔诚",
        "zh_tw": "皆因狄亞內魯虔誠之心",
    },
    "23101018": {
        "en_us": "Tree of Memory",
        "ja_jp": "記憶の樹",
        "zh_cn": "记忆之树",
        "zh_tw": "記憶之樹",
    },
    "23101019": {
        "en_us": "Vessel of Memory",
        "ja_jp": "記憶の器",
        "zh_cn": "记忆之器",
        "zh_tw": "記憶之器",
    },
    "23101020": {
        "en_us": "Master of the Treasury",
        "ja_jp": "宝物庫の主",
        "zh_cn": "宝物库之主",
        "zh_tw": "寶物庫的主人",
    },
}


def fetchEventName(eventID, lang):
    try:
        eventName = textlabelJson[("EVENT_NAME_%s") % eventID][lang]
    except KeyError:
        try:
            eventName = textlabelJson[("QUEST_GROUP_NAME_%s") % eventID][lang]
        except KeyError:
            if eventID in specialEventDic:
                eventName = specialEventDic[eventID][swapLangTable2[lang]]
            else:
                print(eventID)
                exit(-1)
    return eventName


def fetchMainName(mainID, lang):
    try:
        mainName = textlabelJson[("QUEST_GROUP_NAME_%s") % mainID][lang]
    except KeyError:
        print(mainID)
        exit(-1)
    return mainName


def fetchEventStoryName(storyID, lang):
    try:
        storyName = textlabelJson[("STORY_QUEST_NAME_%s") % storyID][lang]
    except KeyError:
        try:
            storyName = speicalStoryDic[storyID][swapLangTable2[lang]]
        except KeyError:
            storyName = storyID
    return storyName


def fetchEpisode(episodeId, lang):
    try:
        episodeName = textlabelJson[("STORY_QUEST_TITLE_%s") % episodeId][lang]
    except KeyError:
        episodeName = ""
    return episodeName


def fetchCharaName(charaId, lang):
    charaBaseID = charaId[:6]
    charaVariationId = charaId[6:]
    charaName = ""
    for cd in charadataJson:
        if (
            charadataJson[cd]["_BaseId"] == int(charaBaseID)
            and charadataJson[cd]["_VariationId"] == int(charaVariationId)
            and str(charadataJson[cd]["_Id"])[0] != "9"
        ):
            # some id begin with 9 match the condition but is not correct.
            try:
                if charadataJson[cd]["_VariationId"] == 1:
                    charaName = textlabelJson[charadataJson[cd]["_Name"]][lang]
                    break
                else:  # Zena(Another Zethia) is special here, she uses Zethia's baseID but VariationId is not 1
                    # And she is technically an alter of Zethia but not with second name.
                    charaName = textlabelJson[charadataJson[cd]["_SecondName"]][lang]
                    break
            except KeyError:
                charaName = textlabelJson[charadataJson[cd]["_Name"]][lang]
                break
    if charaName == "":
        print(charaId)
        exit(-1)
    return charaName


def fetchDragonName(dragonId, lang):
    dragonBaseID = dragonId[:6]
    dragonName = ""
    for dd in dragondataJson:
        if dragondataJson[dd]["_BaseId"] == int(dragonBaseID):
            try:
                dragonName = textlabelJson[dragondataJson[dd]["_SecondName"]][lang]
                break
            except KeyError:
                dragonName = textlabelJson[dragondataJson[dd]["_Name"]][lang]
                break
    if dragonName == "":
        print(dragonId)
        exit(-1)
    return dragonName


def buildIndex():
    storyDataJson = {
        "castlestory": {},  # id: {story_name, path}
        # event_id: {event_name, content: [{story_id, episode, story_name, path}]}
        "queststory_event": {},
        # chapter_id: {chapter_name, content: [{story_id, title, story_name, path}]}
        "queststory_main": {},
        # chara_id: {chara_name, content: [{story_id, episode, story_name, path}]}
        "unitstory_chara": {},
        # dragon_id: {dragon_name, content: [{story_id, story_name, path}]}
        "unitstory_dragon": {},
    }
    for cid in storyDataJsonCN["castlestory"]:
        storyDataJson["castlestory"][cid] = {
            "name": {
                "en_us": textlabelJson[f"STORY_CASTLE_NAME_{cid}"]["ENUS"],
                "ja_jp": textlabelJson[f"STORY_CASTLE_NAME_{cid}"]["JP"],
                "zh_cn": textlabelJson[f"STORY_CASTLE_NAME_{cid}"]["ZHCN"],
                "zh_tw": textlabelJson[f"STORY_CASTLE_NAME_{cid}"]["ZHTW"],
            }
        }
    for eid in storyDataJsonCN["queststory_event"]:
        storyDataJson["queststory_event"][eid] = {
            "name": {
                "en_us": fetchEventName(eid, "ENUS"),
                "ja_jp": fetchEventName(eid, "JP"),
                "zh_cn": fetchEventName(eid, "ZHCN"),
                "zh_tw": fetchEventName(eid, "ZHTW"),
            },
            "content": [],
        }
        for content in storyDataJsonCN["queststory_event"][eid]["content"]:
            tempContent = {}
            tempContent["id"] = content["story_id"]
            tempContent["name"] = {
                "en_us": fetchEventStoryName(content["story_id"], "ENUS"),
                "ja_jp": fetchEventStoryName(content["story_id"], "JP"),
                "zh_cn": fetchEventStoryName(content["story_id"], "ZHCN"),
                "zh_tw": fetchEventStoryName(content["story_id"], "ZHTW"),
            }
            tempContent["episode"] = {
                "en_us": fetchEpisode(content["story_id"], "ENUS"),
                "ja_jp": fetchEpisode(content["story_id"], "JP"),
                "zh_cn": fetchEpisode(content["story_id"], "ZHCN"),
                "zh_tw": fetchEpisode(content["story_id"], "ZHTW"),
            }
            storyDataJson["queststory_event"][eid]["content"].append(tempContent)
    for mid in storyDataJsonCN["queststory_main"]:
        storyDataJson["queststory_main"][mid] = {
            "name": {
                "en_us": fetchMainName(mid, "ENUS"),
                "ja_jp": fetchMainName(mid, "JP"),
                "zh_cn": fetchMainName(mid, "ZHCN"),
                "zh_tw": fetchMainName(mid, "ZHTW"),
            },
            "content": [],
        }
        for content in storyDataJsonCN["queststory_main"][mid]["content"]:
            tempContent = {}
            tempContent["id"] = content["story_id"]
            tempContent["name"] = {
                "en_us": fetchEventStoryName(content["story_id"], "ENUS"),
                "ja_jp": fetchEventStoryName(content["story_id"], "JP"),
                "zh_cn": fetchEventStoryName(content["story_id"], "ZHCN"),
                "zh_tw": fetchEventStoryName(content["story_id"], "ZHTW"),
            }
            tempContent["title"] = {
                "en_us": fetchEpisode(content["story_id"], "ENUS"),
                "ja_jp": fetchEpisode(content["story_id"], "JP"),
                "zh_cn": fetchEpisode(content["story_id"], "ZHCN"),
                "zh_tw": fetchEpisode(content["story_id"], "ZHTW"),
            }
            storyDataJson["queststory_main"][mid]["content"].append(tempContent)
    for ucid in storyDataJsonCN["unitstory_chara"]:
        storyDataJson["unitstory_chara"][ucid] = {
            "name": {
                "en_us": fetchCharaName(ucid, "ENUS"),
                "ja_jp": fetchCharaName(ucid, "JP"),
                "zh_cn": fetchCharaName(ucid, "ZHCN"),
                "zh_tw": fetchCharaName(ucid, "ZHTW"),
            },
            "content": [],
        }
        for content in storyDataJsonCN["unitstory_chara"][ucid]["content"]:
            tempContent = {}
            tempContent["id"] = content["story_id"]
            tempContent["name"] = {
                "en_us": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}'][
                    "ENUS"
                ],
                "ja_jp": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}']["JP"],
                "zh_cn": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}'][
                    "ZHCN"
                ],
                "zh_tw": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}'][
                    "ZHTW"
                ],
            }
            tempContent["episode"] = {
                "en_us": textlabelJson[
                    f'STORY_QUEST_TITLE_EP{content["story_id"][-1]}'
                ]["ENUS"],
                "ja_jp": textlabelJson[
                    f'STORY_QUEST_TITLE_EP{content["story_id"][-1]}'
                ]["JP"],
                "zh_cn": textlabelJson[
                    f'STORY_QUEST_TITLE_EP{content["story_id"][-1]}'
                ]["ZHCN"],
                "zh_tw": textlabelJson[
                    f'STORY_QUEST_TITLE_EP{content["story_id"][-1]}'
                ]["ZHTW"],
            }
            storyDataJson["unitstory_chara"][ucid]["content"].append(tempContent)
    for udid in storyDataJsonCN["unitstory_dragon"]:
        storyDataJson["unitstory_dragon"][udid] = {
            "name": {
                "en_us": fetchDragonName(udid, "ENUS"),
                "ja_jp": fetchDragonName(udid, "JP"),
                "zh_cn": fetchDragonName(udid, "ZHCN"),
                "zh_tw": fetchDragonName(udid, "ZHTW"),
            },
            "content": [],
        }
        for content in storyDataJsonCN["unitstory_dragon"][udid]["content"]:
            tempContent = {}
            tempContent["id"] = content["story_id"]
            tempContent["name"] = {
                "en_us": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}'][
                    "ENUS"
                ],
                "ja_jp": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}']["JP"],
                "zh_cn": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}'][
                    "ZHCN"
                ],
                "zh_tw": textlabelJson[f'STORY_UNIT_NAME_{content["story_id"]}'][
                    "ZHTW"
                ],
            }
            storyDataJson["unitstory_dragon"][udid]["content"].append(tempContent)
    return storyDataJson


json.dump(
    buildIndex(),
    open("index.json", "w", encoding="utf-8"),
    ensure_ascii=False,
    indent=2,
)
