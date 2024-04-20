import os
import re
import shutil
import json
import tqdm
import errno
import UnityPy

playerNameJP = "ユーディル"
playerName = {"zh_cn": "尤蒂尔", "zh_tw": "尤帝爾", "ja_jp": "ユーディル", "en_us": "Euden"}
swapTable = {"m": "10", "p": "11", "n": "12", "e": "20", "b": "21"}
# static_fid_map = {
#     'c01098': '100009_06', # 皇帝ゼシア
#     'dn2268': '120231_01', # ミカエル (but NPC ver)
#     'cn4503': '110403_01', # イズモ
#     'cn3693': '110393_01', # ファルギルト (01 or 02 whatever)
#     'cn02672': '110349_01', # ラトニー？ (a certain expression)
#     # 'cn3597': '', # ヴァース
#     'dn2014': '200014_01', # ウラノス
#     'cn3594': '',
#     'dn2263': '',
#     'cn010972': '',
#     'cn01382': '',
#     'cn2223': '',
#     'cn4501': '',
#     'cn4702': '',
#     'dn2269': '',
#     'cn0932': '',
#     'cn01303': '',
#     'cn01125': '',
#     'cn01126': '',
#     'cn3495': '',
#     'cn0147' : ''
# }
# support_path_format = [
#     'story.castlestory',
#     'story.queststory.event',
#     'story.queststory.main',
#     'story.unitstory.chara',
#     'story.unitstory.dragon'
# ]

indexJson = json.load(open("stories_noascii/index.json", "r", encoding="utf-8"))


def retrieveStoryJson(input):
    env = UnityPy.load(input)
    for obj in env.objects:
        if obj.type.name in ["MonoBehaviour"]:
            data = obj.read()
            tree = data.type_tree
            dic = dict(
                zip(
                    tree["functions"][0]["variables"]["entriesKey"],
                    tree["functions"][0]["variables"]["entriesValue"],
                )
            )
            # json.dump(dic, open('funcData.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
            return dic


funcIdJson = retrieveStoryJson("assets/story/function")
funcNameJson = retrieveStoryJson("assets/story/function_namelist_notedit")

debug_unknown = {}


def getSpeakerIdByFuncId(funcId):
    if funcId.startswith("c") or funcId.startswith("d"):
        try:
            id_str = funcIdJson[funcId.replace("n", "")]
            if id_str.endswith("b") or id_str.endswith("c"):
                id_str = id_str[:-1]
            if len(id_str) == 12 and id_str.count("_") == 2:
                id_str = "_".join([id_str.split("_")[0], id_str.split("_")[1]])
            return id_str
        except KeyError:
            return funcId
    # RE: (private string) StoryScriptRuntime.CommandStack::GetUnitVariable(string value)
    if (
        funcId.startswith("m")
        or funcId.startswith("p")
        or funcId.startswith("n")
        or funcId.startswith("b")
        or funcId.startswith("e")
    ):
        if len(funcId) < 4 or len(funcId) > 7:
            return funcId
        pattern = re.compile("[0-9]+")
        if pattern.fullmatch(funcId[1:]) is None:
            return funcId
        baseId = f"{swapTable[funcId[0]]}0{funcId[1:4]}"
        step = 2 if len(funcId) == 7 else len(funcId) - 4
        if step >= 1:
            id_str = funcId[4 : 4 + step]
            if len(funcId) != 7:
                id_str = f"{baseId}_{int(id_str):02d}"
                return id_str
            else:
                id_str = f"{baseId}_{int(id_str):02d}{funcId[6:7]}"
                return id_str
        else:
            id_str = f"{baseId}_01"
            return id_str
    return funcId


def getNameByFuncIdJP(funcId):
    if funcId not in funcNameJson:
        return getSpeakerIdByFuncId(funcId).replace("{player_name}", playerNameJP)
    else:
        return funcNameJson[funcId].replace("{player_name}", playerNameJP)


def parseMonoJP(tree, storyname):
    res = {
        "story_id": "",
        "story_name": "",
        "story_icon": "",
        "outline": {"title": "", "content": ""},
        "story_content": [],
    }

    for func in tree["functions"]:  # multiple functions  e.g.2082806
        rowFilteredFunc = {}

        # 'row' as keys
        for command in func["commandList"]:
            if command["row"] not in rowFilteredFunc:
                rowFilteredFunc[command["row"]] = []
            rowFilteredFunc[command["row"]].append(
                {
                    "command": command["command"],
                    "args": command["args"],
                    "end": command["end"],
                }
            )

        for row in rowFilteredFunc:
            currentContent = {
                "speaker_id": "",
                "speaker_name": "",
                "context": "",
                "voice_line": "",
                "book_image": "",
            }
            commandList = set([x["command"] for x in rowFilteredFunc[row]])

            # outline part
            # if rowFilteredFunc[row][0]['command'] in ['OL_LEFT', 'OL_CENTER']:  # TODO: really?
            if "outline" in commandList:
                tempOutline = ""
                for command in rowFilteredFunc[row]:
                    if command["command"] == "OL_TITLE":
                        res["outline"]["title"] = command["args"]
                    if command["command"] == "ruby":
                        tempOutline += f'<ruby><rb>{command["args"][0]}</rb><rt>{command["args"][1]}</rt></ruby>'
                        # tempOutline += f'<ruby><rb>{command["args"][0]}</rb><rp>(</rp><rt>{command["args"][1]}</rt><rp>)</rp></ruby>'
                    if command["command"] == "outline":
                        if len(command["args"]) == 0:
                            continue
                        tempOutline += command["args"][0]
                res["outline"]["content"] = tempOutline

            # printable part
            # if rowFilteredFunc[row][0]['command'] == 'print':
            if "print" in commandList:
                tempPrintable = ""
                firstArgs = ""
                # for one sentence
                for idx, command in enumerate(rowFilteredFunc[row]):
                    if idx == 0:
                        """
                        Basic:
                          First command must contain speaker id.
                          Last command may contain voice id if available.
                        Some first args examples:
                          #1 {'command': 'print', 'args': ['cn0307', 'おっと、'], 'end': 0}
                          #2 {'command': 'print', 'args': ['？？？#cn1857' or 'SYS', 'ニャニャ!?'], 'end': 0}
                          #3 {'command': 'print', 'args': ['？？？#cn1857'], 'end': 0}
                          #4 {'command': 'print', 'args': ['？？？#cn1859', 'ああっ！アイルーが！', 'VO_CHR_EVENTSTORY_22001_01_0003'], 'end': 1}
                          #5 {'command': 'print', 'args': ['？？？#cn1857', 'ニャ～～～～!!'], 'end': 1}
                          #6 {'command': 'print', 'args': [], 'end': 1}
                          #7 {'command': 'print', 'args': ['cn0101'], 'end': 0}
                        Please note:
                          #1 has charaname_id & end == 0
                            => Every print command behind #1 should contain 2 args(charaname_id, kana) except last one could get 3 if vocal is available.
                          #2 starts with ？？？ or SYS
                          #3 unlike #1#2, args[1] == null, because this sentence starts with kanji (need ruby command)
                          #4#5 end == 1, do not forget potential vocal arg
                          #6 end == 1, because sentence ends with kanji. And do not forget potential vocal arg.
                          #7 will happen when no kana between two rubys (example: ...一体 #7 何者...)
                          #Extra  print args could contain speaker id, sometimes not.
                        """
                        firstArgs = command["args"]
                        if "#" in firstArgs[0]:
                            currentContent["speaker_id"] = getSpeakerIdByFuncId(
                                firstArgs[0].split("#")[-1]
                            )
                            currentContent["speaker_name"] = firstArgs[0].split("#")[0]
                        elif firstArgs[0] in [
                            "SYS",
                            "ＳＹＳ",
                        ]:  # story/castlestory/1000402.a
                            currentContent["speaker_name"] = "SYS"
                        else:
                            # cannot generate id
                            if firstArgs[0] == getSpeakerIdByFuncId(firstArgs[0]):
                                if storyname not in debug_unknown:
                                    debug_unknown[storyname] = {"id": [], "name": []}
                                if firstArgs[0] not in debug_unknown[storyname]["id"]:
                                    debug_unknown[storyname]["id"].append(firstArgs[0])

                            # cannot genarate name
                            if firstArgs[0] == getNameByFuncIdJP(firstArgs[0]):
                                if storyname not in debug_unknown:
                                    debug_unknown[storyname] = {"id": [], "name": []}
                                if firstArgs[0] not in debug_unknown[storyname]["name"]:
                                    debug_unknown[storyname]["name"].append(
                                        firstArgs[0]
                                    )
                            currentContent["speaker_id"] = getSpeakerIdByFuncId(
                                firstArgs[0]
                            )
                            currentContent["speaker_name"] = getNameByFuncIdJP(
                                firstArgs[0]
                            )
                        tempPrintable += firstArgs[1] if len(firstArgs) > 1 else ""
                        currentContent["voice_line"] = (
                            firstArgs[2] if len(firstArgs) == 3 else ""
                        )
                        continue
                    if command["command"] == "print":  # following command
                        if command["args"] == []:  # like #6
                            continue

                        speakerIdOmitted = (
                            False if command["args"][0] == firstArgs[0] else True
                        )

                        if command["end"] == 1:
                            isVocal = command["args"][-1].startswith(
                                "VO"
                            )  # TODO: Really?
                            if isVocal:
                                currentContent["voice_line"] = command["args"][-1]
                                if speakerIdOmitted:
                                    if len(command["args"]) == 2:
                                        tempPrintable += command["args"][0]
                                else:
                                    if len(command["args"]) == 3:
                                        tempPrintable += command["args"][1]
                            else:
                                if speakerIdOmitted:
                                    tempPrintable += command["args"][-1]
                                else:
                                    if len(command["args"]) == 1:
                                        pass
                                    elif len(command["args"]) > 1:
                                        tempPrintable += command["args"][-1]
                        else:
                            if speakerIdOmitted:
                                tempPrintable += command["args"][0]
                            elif len(command["args"]) == 2:
                                tempPrintable += command["args"][1]
                    if command["command"] == "ruby":
                        tempPrintable += f'<ruby><rb>{command["args"][0]}</rb><rt>{command["args"][1]}</rt></ruby>'
                        # tempPrintable += f'<ruby><rb>{command["args"][0]}</rb><rp>(</rp><rt>{command["args"][1]}</rt><rp>)</rp></ruby>'
                currentContent["context"] = tempPrintable.replace(
                    "{player_name}", playerNameJP
                )
                res["story_content"].append(currentContent)
            # if rowFilteredFunc[row][0]['command'] == 'telop':
            if "telop" in commandList:
                """
                  #1 "args": [
                        "城内王座決定戦",
                        " ",
                        "じょうないおうざけっていせん"]
                  #2 "args": [
                        "参上！スイーツパイレーツ！",
                        " ",
                        "さんじょう　　　　　　　　　　　　　　　　　　　　　　",
                        " "]
                  #3 "args": [
                        "ギンギラバレンタイン",
                        " ",
                        " ",
                        " "]
                #1 contains kanji, 3-args
                #2 contains kanji, 4-args
                #3 contains kana only, 4-args(maybe 3-args exists)
                """
                # assert(len(rowFilteredFunc[row]) == 1)
                main = rowFilteredFunc[row][0]["args"][0].replace(
                    "{player_name}", playerNameJP
                )
                ruby = rowFilteredFunc[row][0]["args"][2]
                currentContent["speaker_name"] = "telop"
                currentContent["context"] = (
                    main
                    if ruby == " "
                    else f"<ruby><rb>{main}</rb><rt>{ruby}</rt></ruby>"
                )
                res["story_content"].append(currentContent)
            if "add_book_text" in commandList:
                """
                If this sentence starts with kanji, <ruby> will be the first command.
                (As a comparison, <print> command will always be the first command.)

                add_book_text may have 1-2 arg(s)
                  1-arg: text
                  2-args: text, book_image
                """
                tempPrintable = ""
                currentContent["speaker_name"] = "add_book_text"
                for command in rowFilteredFunc[row]:
                    if command["command"] == "add_book_text":
                        if len(command["args"]) == 0:
                            continue
                        if len(command["args"]) == 2:
                            currentContent["book_image"] = command["args"][1]
                        tempPrintable += command["args"][0]
                    if command["command"] == "ruby":
                        tempPrintable += f'<ruby><rb>{command["args"][0]}</rb><rt>{command["args"][1]}</rt></ruby>'
                currentContent["context"] = tempPrintable.replace(
                    "{player_name}", playerNameJP
                )
                res["story_content"].append(currentContent)
    return res


def parseMono(tree, storyname, lang):
    # JSON:    {story_id, story_name, story_icon, outline: {title, content}, story_content: [{speaker_id:[], speaker_name, context, voice_line, book_image}]}
    res = {
        "story_id": "",
        "story_name": "",
        "story_icon": "",
        "outline": {"title": "", "content": ""},
        "story_content": [],
    }
    for func in tree["functions"]:  # multiple functions  e.g.2082806
        speaker_id = []
        for command in func["commandList"]:
            commandType = command["command"]
            commandData = command["args"]
            if commandType in [
                "telop",
                "add_book_text",
                "print",
            ]:  # printable text function
                content = {
                    "speaker_id": [],
                    "speaker_name": "",
                    "context": "",
                    "voice_line": "",
                    "book_image": "",
                }
                if commandType == "telop":
                    content["speaker_name"] = commandType
                    for line in commandData:
                        content["context"] = f'{content["context"]}\\n{line}'
                    content["context"] = content["context"].replace(
                        "{player_name}", playerName[lang]
                    )
                    res["story_content"].append(content)
                elif commandType == "add_book_text":
                    content["speaker_name"] = commandType
                    content["context"] = commandData[0].replace(
                        "{player_name}", playerName[lang]
                    )
                    if len(commandData) == 2:
                        content["book_image"] = commandData[1]
                    res["story_content"].append(content)
                elif commandType == "print":
                    content["speaker_name"] = commandData[0].replace(
                        "{player_name}", playerName[lang]
                    )
                    content["context"] = commandData[1].replace(
                        "{player_name}", playerName[lang]
                    )
                    if len(commandData) == 3:
                        content["voice_line"] = commandData[2]
                    content["speaker_id"] = speaker_id
                    res["story_content"].append(content)
            elif commandType == "OL_TITLE":
                res["outline"]["title"] = commandData
            elif commandType == "outline":
                res["outline"]["content"] = commandData
            else:
                # some functions may contain speaker id(s), but too many functions exist
                # 2.11.0 cause id mapping changed
                temp_speaker_id = []
                for arg in commandData:
                    if arg.startswith("c") or arg.startswith("d"):
                        try:
                            id_str = funcIdJson[arg]
                            if id_str.endswith("b") or id_str.endswith("c"):
                                id_str = id_str[:-1]
                            if len(id_str) == 12 and id_str.count("_") == 2:
                                id_str = "_".join(
                                    [id_str.split("_")[0], id_str.split("_")[1]]
                                )
                            temp_speaker_id.append(id_str)
                        except KeyError:
                            pass
                    # RE: (private string) StoryScriptRuntime.CommandStack::GetUnitVariable(string value)
                    if (
                        arg.startswith("m")
                        or arg.startswith("p")
                        or arg.startswith("n")
                        or arg.startswith("b")
                        or arg.startswith("e")
                    ):
                        if len(arg) < 4 or len(arg) > 7:
                            continue
                        pattern = re.compile("[0-9]+")
                        if pattern.fullmatch(arg[1:]) is None:
                            continue
                        baseId = f"{swapTable[arg[0]]}0{arg[1:4]}"
                        step = 2 if len(arg) == 7 else len(arg) - 4
                        if step >= 1:
                            id_str = arg[4 : 4 + step]
                            if len(arg) != 7:
                                id_str = f"{baseId}_{int(id_str):02d}"
                                temp_speaker_id.append(id_str)
                            else:
                                id_str = f"{baseId}_{int(id_str):02d}{arg[6:7]}"
                                temp_speaker_id.append(id_str)
                        else:
                            id_str = f"{baseId}_01"
                            temp_speaker_id.append(id_str)
                if len(temp_speaker_id) > 0:
                    speaker_id = temp_speaker_id
    return res


def parseStoryJP(filePath, outpath):
    env = UnityPy.load(filePath)
    for obj in env.objects:
        if obj.type.name in ["MonoBehaviour"]:
            data = obj.read()
            tree = data.read_typetree()
            json.dump(
                tree,
                open("test_tree.json", "w", encoding="utf-8"),
                ensure_ascii=False,
                indent=2,
            )
            json.dump(
                parseMonoJP(tree, filePath),
                open(outpath, "w", encoding="utf-8"),
                ensure_ascii=False,
                indent=2,
            )


def parseStory(filePath, outpath, lang):
    env = UnityPy.load(filePath)
    for obj in env.objects:
        if obj.type.name in ["MonoBehaviour"]:
            data = obj.read()
            tree = data.read_typetree()
            json.dump(
                tree,
                open("test_tree.json", "w", encoding="utf-8"),
                ensure_ascii=False,
                indent=2,
            )
            exit()
            json.dump(
                parseMono(tree, filePath, lang),
                open(outpath, "w", encoding="utf-8"),
                ensure_ascii=False,
                indent=2,
            )


parseStoryJP("test_assets/ja_jp/story.queststory.event/2200103.a", "test_parsed.json")

# for castleId in tqdm.tqdm(indexJson["castlestory"]):
#     parseStoryJP(
#         f"test_assets/ja_jp/story.castlestory/{castleId}.a",
#         f"test_stories/ja_jp/castlestory/{castleId}.json",
#     )
# for eventId in tqdm.tqdm(indexJson["queststory_event"]):
#     for content in indexJson["queststory_event"][eventId]["content"]:
#         parseStoryJP(
#             f'test_assets/ja_jp/story.queststory.event/{content["story_id"]}.a',
#             f'test_stories/ja_jp/queststory_event/{content["story_id"]}.json',
#         )
# for mainId in tqdm.tqdm(indexJson["queststory_main"]):
#     for content in indexJson["queststory_main"][mainId]["content"]:
#         parseStoryJP(
#             f'test_assets/ja_jp/story.queststory.main/{content["story_id"]}.a',
#             f'test_stories/ja_jp/queststory_main/{content["story_id"]}.json',
#         )
# for charaId in tqdm.tqdm(indexJson["unitstory_chara"]):
#     for content in indexJson["unitstory_chara"][charaId]["content"]:
#         parseStoryJP(
#             f'test_assets/ja_jp/story.unitstory.chara/{content["story_id"]}.a',
#             f'test_stories/ja_jp/unitstory_chara/{content["story_id"]}.json',
#         )
# for dragonId in tqdm.tqdm(indexJson["unitstory_dragon"]):
#     for content in indexJson["unitstory_dragon"][dragonId]["content"]:
#         parseStoryJP(
#             f'test_assets/ja_jp/story.unitstory.dragon/{content["story_id"]}.a',
#             f'test_stories/ja_jp/unitstory_dragon/{content["story_id"]}.json',
#         )
exit()

# for f in tqdm.tqdm(os.listdir('test_assets/story.queststory.main')):
#     parseStory(f'test_assets/story.queststory.main/{f}', f)

# os.makedirs('test_stories/story.castlestory', exist_ok=True)
# os.makedirs('test_stories/story.queststory.event', exist_ok=True)
# os.makedirs('test_stories/story.queststory.main', exist_ok=True)
# os.makedirs('test_stories/story.unitstory.chara', exist_ok=True)
# os.makedirs('test_stories/story.unitstory.dragon', exist_ok=True)


def parseAll(lang):
    for castleId in tqdm.tqdm(indexJson["castlestory"]):
        parseStory(
            f"test_assets/{lang}/castlestory/{castleId}.a",
            f"test_stories/{lang}/castlestory/{castleId}.json",
            lang,
        )
    for eventId in tqdm.tqdm(indexJson["queststory_event"]):
        for content in indexJson["queststory_event"][eventId]["content"]:
            parseStory(
                f'test_assets/{lang}/story.queststory.event/{content["story_id"]}.a',
                f'test_stories/{lang}/queststory_event/{content["story_id"]}.json',
                lang,
            )
    for mainId in tqdm.tqdm(indexJson["queststory_main"]):
        for content in indexJson["queststory_main"][mainId]["content"]:
            parseStory(
                f'test_assets/{lang}/story.queststory.main/{content["story_id"]}.a',
                f'test_stories/{lang}/queststory_main/{content["story_id"]}.json',
                lang,
            )
    for charaId in tqdm.tqdm(indexJson["unitstory_chara"]):
        for content in indexJson["unitstory_chara"][charaId]["content"]:
            parseStory(
                f'test_assets/{lang}/story.unitstory.chara/{content["story_id"]}.a',
                f'test_stories/{lang}/unitstory_chara/{content["story_id"]}.json',
                lang,
            )
    for dragonId in tqdm.tqdm(indexJson["unitstory_dragon"]):
        for content in indexJson["unitstory_dragon"][dragonId]["content"]:
            parseStory(
                f'test_assets/{lang}/story.unitstory.dragon/{content["story_id"]}.a',
                f'test_stories/{lang}/unitstory_dragon/{content["story_id"]}.json',
                lang,
            )


parseStory(
    f"test_assets/zh_tw/story.queststory.event/3100102.a",
    f"test_stories/zh_tw/queststory_event/3100102.json",
    "zh_tw",
)

# parseAll("zh_tw")

# json.dump(debug_unknown, open('debug_unknown.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
