import json
import tqdm

indexJson = json.load(open("index.json", "r", encoding="utf-8"))
resSample = {
    "story_id": "",
    "story_name": "",
    "story_icon": "",
    "outline": {"title": "", "content": ""},
    "story_content": [],
}
contentSample = {
    "speaker_id": [],
    "speaker_name": "",
    "context": "",
    "voice_line": "",
    "book_image": "",
}

newRes = {
    "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
    "outline": {
        "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
        "content": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
    },
    "prev": "",
    "next": "",
    "content": [],
}
newContent = {
    "icon": "",
    "name": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
    "context": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
    "voice": "",
    "book": "",
}


def processCastleStory():
    storyList = list(indexJson["castlestory"].keys())
    for c in tqdm.tqdm(indexJson["castlestory"]):
        Res = {
            "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
            "outline": {
                "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                "content": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
            },
            "prev": "",
            "next": "",
            "content": [],
        }
        if len(storyList) > 1:
            cidx = storyList.index(c)
            if cidx == 0:
                Res["next"] = storyList[cidx + 1]
            elif cidx == len(storyList) - 1:
                Res["prev"] = storyList[cidx - 1]
            else:
                Res["prev"] = storyList[cidx - 1]
                Res["next"] = storyList[cidx + 1]
        enus = json.load(
            open(f"test_stories/en_us/castlestory/{c}.json", "r", encoding="utf8")
        )
        jajp = json.load(
            open(f"test_stories/ja_jp/castlestory/{c}.json", "r", encoding="utf8")
        )
        zhcn = json.load(
            open(f"stories_noascii/castlestory/{c}.json", "r", encoding="utf8")
        )
        zhtw = json.load(
            open(f"test_stories/zh_tw/castlestory/{c}.json", "r", encoding="utf8")
        )
        assert (
            len(enus["story_content"])
            == len(jajp["story_content"])
            == len(zhcn["story_content"])
            == len(zhtw["story_content"])
        )
        Res["title"][
            "en_us"
        ] = f"Castle Story: {indexJson['castlestory'][c]['name']['en_us']}"
        Res["title"][
            "ja_jp"
        ] = f"キャッスルストーリー {indexJson['castlestory'][c]['name']['ja_jp']}"
        Res["title"]["zh_cn"] = f"城堡剧情 {indexJson['castlestory'][c]['name']['zh_cn']}"
        Res["title"]["zh_tw"] = f"城堡的故事 {indexJson['castlestory'][c]['name']['zh_tw']}"

        Res["outline"]["title"]["en_us"] = enus["outline"]["title"]
        Res["outline"]["title"]["ja_jp"] = jajp["outline"]["title"]
        Res["outline"]["title"]["zh_cn"] = zhcn["outline"]["title"]
        Res["outline"]["title"]["zh_tw"] = zhtw["outline"]["title"]
        Res["outline"]["content"]["ja_jp"] = jajp["outline"]["content"]
        Res["outline"]["content"]["en_us"] = (
            "" if enus["outline"]["content"] == "" else enus["outline"]["content"][0]
        )
        Res["outline"]["content"]["zh_cn"] = (
            "" if zhcn["outline"]["content"] == "" else zhcn["outline"]["content"][0]
        )
        Res["outline"]["content"]["zh_tw"] = (
            "" if zhtw["outline"]["content"] == "" else zhtw["outline"]["content"][0]
        )

        for idx in range(len(zhcn["story_content"])):
            tempContent = {
                "icon": "",
                "name": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                "context": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                "voice": "",
                "book": "",
            }
            if len(zhcn["story_content"][idx]["speaker_id"]) != 0:
                tempContent["icon"] = zhcn["story_content"][idx]["speaker_id"][-1]
            else:
                if jajp["story_content"][idx]["speaker_id"] != "":
                    tempContent["icon"] = jajp["story_content"][idx]["speaker_id"]
            tempContent["name"] = {
                "en_us": enus["story_content"][idx]["speaker_name"],
                "ja_jp": jajp["story_content"][idx]["speaker_name"],
                "zh_cn": zhcn["story_content"][idx]["speaker_name"],
                "zh_tw": zhtw["story_content"][idx]["speaker_name"],
            }
            tempContent["context"] = {
                "en_us": enus["story_content"][idx]["context"],
                "ja_jp": jajp["story_content"][idx]["context"],
                "zh_cn": zhcn["story_content"][idx]["context"],
                "zh_tw": zhtw["story_content"][idx]["context"],
            }
            tempContent["voice"] = zhcn["story_content"][idx]["voice_line"]
            tempContent["book"] = zhcn["story_content"][idx]["book_image"]
            Res["content"].append(tempContent)
        json.dump(
            Res,
            open(f"test_stories/castlestory/{c}.json", "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=2,
        )


def processQuestMainStory():
    for e in tqdm.tqdm(indexJson["queststory_main"]):
        for idx, es in enumerate(indexJson["queststory_main"][e]["content"]):
            Res = {
                "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                "outline": {
                    "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "content": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                },
                "prev": "",
                "next": "",
                "content": [],
            }
            if len(indexJson["queststory_main"][e]["content"]) > 1:
                if idx == 0:
                    Res["next"] = indexJson["queststory_main"][e]["content"][idx + 1][
                        "id"
                    ]
                elif idx == len(indexJson["queststory_main"][e]["content"]) - 1:
                    Res["prev"] = indexJson["queststory_main"][e]["content"][idx - 1][
                        "id"
                    ]
                else:
                    Res["prev"] = indexJson["queststory_main"][e]["content"][idx - 1][
                        "id"
                    ]
                    Res["next"] = indexJson["queststory_main"][e]["content"][idx + 1][
                        "id"
                    ]
            enus = json.load(
                open(
                    f"test_stories/en_us/queststory_main/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            jajp = json.load(
                open(
                    f"test_stories/ja_jp/queststory_main/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhcn = json.load(
                open(
                    f"stories_noascii/queststory_main/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhtw = json.load(
                open(
                    f"test_stories/zh_tw/queststory_main/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            try:
                assert (
                    len(enus["story_content"])
                    == len(jajp["story_content"])
                    == len(zhcn["story_content"])
                    == len(zhtw["story_content"])
                )
            except AssertionError:
                """
                3100102
                34 35 34 34
                """
                print(es["id"])
                print(
                    len(enus["story_content"]),
                    len(jajp["story_content"]),
                    len(zhcn["story_content"]),
                    len(zhtw["story_content"]),
                )
                exit(-1)
            Res["title"][
                "en_us"
            ] = f"{indexJson['queststory_main'][e]['name']['en_us']}  {es['title']['en_us']}  {es['name']['en_us']}"
            Res["title"][
                "ja_jp"
            ] = f"{indexJson['queststory_main'][e]['name']['ja_jp']} {es['title']['ja_jp']} {es['name']['ja_jp']}"
            Res["title"][
                "zh_cn"
            ] = f"{indexJson['queststory_main'][e]['name']['zh_cn']} {es['title']['zh_cn']} {es['name']['zh_cn']}"
            Res["title"][
                "zh_tw"
            ] = f"{indexJson['queststory_main'][e]['name']['zh_tw']} {es['title']['zh_tw']} {es['name']['zh_tw']}"

            Res["outline"]["title"]["en_us"] = enus["outline"]["title"]
            Res["outline"]["title"]["ja_jp"] = jajp["outline"]["title"]
            Res["outline"]["title"]["zh_cn"] = zhcn["outline"]["title"]
            Res["outline"]["title"]["zh_tw"] = zhtw["outline"]["title"]
            Res["outline"]["content"]["ja_jp"] = jajp["outline"]["content"]
            Res["outline"]["content"]["en_us"] = (
                ""
                if enus["outline"]["content"] == ""
                else enus["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_cn"] = (
                ""
                if zhcn["outline"]["content"] == ""
                else zhcn["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_tw"] = (
                ""
                if zhtw["outline"]["content"] == ""
                else zhtw["outline"]["content"][0]
            )

            for idx in range(len(zhcn["story_content"])):
                tempContent = {
                    "icon": "",
                    "name": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "context": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "voice": "",
                    "book": "",
                }
                if len(zhcn["story_content"][idx]["speaker_id"]) != 0:
                    tempContent["icon"] = zhcn["story_content"][idx]["speaker_id"][-1]
                else:
                    if jajp["story_content"][idx]["speaker_id"] != "":
                        tempContent["icon"] = jajp["story_content"][idx]["speaker_id"]
                tempContent["name"] = {
                    "en_us": enus["story_content"][idx]["speaker_name"],
                    "ja_jp": jajp["story_content"][idx]["speaker_name"],
                    "zh_cn": zhcn["story_content"][idx]["speaker_name"],
                    "zh_tw": zhtw["story_content"][idx]["speaker_name"],
                }
                tempContent["context"] = {
                    "en_us": enus["story_content"][idx]["context"],
                    "ja_jp": jajp["story_content"][idx]["context"],
                    "zh_cn": zhcn["story_content"][idx]["context"],
                    "zh_tw": zhtw["story_content"][idx]["context"],
                }
                tempContent["voice"] = zhcn["story_content"][idx]["voice_line"]
                tempContent["book"] = zhcn["story_content"][idx]["book_image"]
                Res["content"].append(tempContent)
            json.dump(
                Res,
                open(
                    f"test_stories/queststory_main/{es['id']}.json",
                    "w",
                    encoding="utf-8",
                ),
                ensure_ascii=False,
                indent=2,
            )


def processQuestEventStory():
    for e in tqdm.tqdm(indexJson["queststory_event"]):
        for idx, es in enumerate(indexJson["queststory_event"][e]["content"]):
            Res = {
                "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                "outline": {
                    "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "content": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                },
                "prev": "",
                "next": "",
                "content": [],
            }
            if len(indexJson["queststory_event"][e]["content"]) > 1:
                if idx == 0:
                    Res["next"] = indexJson["queststory_event"][e]["content"][idx + 1][
                        "id"
                    ]
                elif idx == len(indexJson["queststory_event"][e]["content"]) - 1:
                    Res["prev"] = indexJson["queststory_event"][e]["content"][idx - 1][
                        "id"
                    ]
                else:
                    Res["prev"] = indexJson["queststory_event"][e]["content"][idx - 1][
                        "id"
                    ]
                    Res["next"] = indexJson["queststory_event"][e]["content"][idx + 1][
                        "id"
                    ]
            enus = json.load(
                open(
                    f"test_stories/en_us/queststory_event/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            jajp = json.load(
                open(
                    f"test_stories/ja_jp/queststory_event/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhcn = json.load(
                open(
                    f"stories_noascii/queststory_event/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhtw = json.load(
                open(
                    f"test_stories/zh_tw/queststory_event/{es['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            try:
                assert (
                    len(enus["story_content"])
                    == len(jajp["story_content"])
                    == len(zhcn["story_content"])
                    == len(zhtw["story_content"])
                )
            except AssertionError:
                """
                3100102
                34 35 34 34
                """
                print(es["id"])
                print(
                    len(enus["story_content"]),
                    len(jajp["story_content"]),
                    len(zhcn["story_content"]),
                    len(zhtw["story_content"]),
                )
                exit(-1)
            Res["title"][
                "en_us"
            ] = f"{indexJson['queststory_event'][e]['name']['en_us']}  {es['episode']['en_us']}  {es['name']['en_us']}"
            Res["title"][
                "ja_jp"
            ] = f"{indexJson['queststory_event'][e]['name']['ja_jp']} {es['episode']['ja_jp']} {es['name']['ja_jp']}"
            Res["title"][
                "zh_cn"
            ] = f"{indexJson['queststory_event'][e]['name']['zh_cn']} {es['episode']['zh_cn']} {es['name']['zh_cn']}"
            Res["title"][
                "zh_tw"
            ] = f"{indexJson['queststory_event'][e]['name']['zh_tw']} {es['episode']['zh_tw']} {es['name']['zh_tw']}"

            Res["outline"]["title"]["en_us"] = enus["outline"]["title"]
            Res["outline"]["title"]["ja_jp"] = jajp["outline"]["title"]
            Res["outline"]["title"]["zh_cn"] = zhcn["outline"]["title"]
            Res["outline"]["title"]["zh_tw"] = zhtw["outline"]["title"]
            Res["outline"]["content"]["ja_jp"] = jajp["outline"]["content"]
            Res["outline"]["content"]["en_us"] = (
                ""
                if enus["outline"]["content"] == ""
                else enus["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_cn"] = (
                ""
                if zhcn["outline"]["content"] == ""
                else zhcn["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_tw"] = (
                ""
                if zhtw["outline"]["content"] == ""
                else zhtw["outline"]["content"][0]
            )

            for idx in range(len(zhcn["story_content"])):
                tempContent = {
                    "icon": "",
                    "name": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "context": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "voice": "",
                    "book": "",
                }
                if len(zhcn["story_content"][idx]["speaker_id"]) != 0:
                    tempContent["icon"] = zhcn["story_content"][idx]["speaker_id"][-1]
                else:
                    if jajp["story_content"][idx]["speaker_id"] != "":
                        tempContent["icon"] = jajp["story_content"][idx]["speaker_id"]
                tempContent["name"] = {
                    "en_us": enus["story_content"][idx]["speaker_name"],
                    "ja_jp": jajp["story_content"][idx]["speaker_name"],
                    "zh_cn": zhcn["story_content"][idx]["speaker_name"],
                    "zh_tw": zhtw["story_content"][idx]["speaker_name"],
                }
                tempContent["context"] = {
                    "en_us": enus["story_content"][idx]["context"],
                    "ja_jp": jajp["story_content"][idx]["context"],
                    "zh_cn": zhcn["story_content"][idx]["context"],
                    "zh_tw": zhtw["story_content"][idx]["context"],
                }
                tempContent["voice"] = zhcn["story_content"][idx]["voice_line"]
                tempContent["book"] = zhcn["story_content"][idx]["book_image"]
                Res["content"].append(tempContent)
            json.dump(
                Res,
                open(
                    f"test_stories/queststory_event/{es['id']}.json",
                    "w",
                    encoding="utf-8",
                ),
                ensure_ascii=False,
                indent=2,
            )


def processUnitCharaStory():
    for c in tqdm.tqdm(indexJson["unitstory_chara"]):
        for idx, cs in enumerate(indexJson["unitstory_chara"][c]["content"]):
            Res = {
                "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                "outline": {
                    "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "content": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                },
                "prev": "",
                "next": "",
                "content": [],
            }
            if len(indexJson["unitstory_chara"][c]["content"]) > 1:
                if idx == 0:
                    Res["next"] = indexJson["unitstory_chara"][c]["content"][idx + 1][
                        "id"
                    ]
                elif idx == len(indexJson["unitstory_chara"][c]["content"]) - 1:
                    Res["prev"] = indexJson["unitstory_chara"][c]["content"][idx - 1][
                        "id"
                    ]
                else:
                    Res["prev"] = indexJson["unitstory_chara"][c]["content"][idx - 1][
                        "id"
                    ]
                    Res["next"] = indexJson["unitstory_chara"][c]["content"][idx + 1][
                        "id"
                    ]
            enus = json.load(
                open(
                    f"test_stories/en_us/unitstory_chara/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            jajp = json.load(
                open(
                    f"test_stories/ja_jp/unitstory_chara/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhcn = json.load(
                open(
                    f"stories_noascii/unitstory_chara/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhtw = json.load(
                open(
                    f"test_stories/zh_tw/unitstory_chara/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            try:
                assert (
                    len(enus["story_content"])
                    == len(jajp["story_content"])
                    == len(zhcn["story_content"])
                    == len(zhtw["story_content"])
                )
            except AssertionError:
                """
                3100102
                34 35 34 34
                """
                print(cs["id"])
                print(
                    len(enus["story_content"]),
                    len(jajp["story_content"]),
                    len(zhcn["story_content"]),
                    len(zhtw["story_content"]),
                )
                exit(-1)
            Res["title"][
                "en_us"
            ] = f"{indexJson['unitstory_chara'][c]['name']['en_us']}  {cs['episode']['en_us']}  {cs['name']['en_us']}"
            Res["title"][
                "ja_jp"
            ] = f"{indexJson['unitstory_chara'][c]['name']['ja_jp']} {cs['episode']['ja_jp']} {cs['name']['ja_jp']}"
            Res["title"][
                "zh_cn"
            ] = f"{indexJson['unitstory_chara'][c]['name']['zh_cn']} {cs['episode']['zh_cn']} {cs['name']['zh_cn']}"
            Res["title"][
                "zh_tw"
            ] = f"{indexJson['unitstory_chara'][c]['name']['zh_tw']} {cs['episode']['zh_tw']} {cs['name']['zh_tw']}"

            Res["outline"]["title"]["en_us"] = enus["outline"]["title"]
            Res["outline"]["title"]["ja_jp"] = jajp["outline"]["title"]
            Res["outline"]["title"]["zh_cn"] = zhcn["outline"]["title"]
            Res["outline"]["title"]["zh_tw"] = zhtw["outline"]["title"]
            Res["outline"]["content"]["ja_jp"] = jajp["outline"]["content"]
            Res["outline"]["content"]["en_us"] = (
                ""
                if enus["outline"]["content"] == ""
                else enus["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_cn"] = (
                ""
                if zhcn["outline"]["content"] == ""
                else zhcn["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_tw"] = (
                ""
                if zhtw["outline"]["content"] == ""
                else zhtw["outline"]["content"][0]
            )

            for idx in range(len(zhcn["story_content"])):
                tempContent = {
                    "icon": "",
                    "name": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "context": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "voice": "",
                    "book": "",
                }
                if len(zhcn["story_content"][idx]["speaker_id"]) != 0:
                    tempContent["icon"] = zhcn["story_content"][idx]["speaker_id"][-1]
                else:
                    if jajp["story_content"][idx]["speaker_id"] != "":
                        tempContent["icon"] = jajp["story_content"][idx]["speaker_id"]
                tempContent["name"] = {
                    "en_us": enus["story_content"][idx]["speaker_name"],
                    "ja_jp": jajp["story_content"][idx]["speaker_name"],
                    "zh_cn": zhcn["story_content"][idx]["speaker_name"],
                    "zh_tw": zhtw["story_content"][idx]["speaker_name"],
                }
                tempContent["context"] = {
                    "en_us": enus["story_content"][idx]["context"],
                    "ja_jp": jajp["story_content"][idx]["context"],
                    "zh_cn": zhcn["story_content"][idx]["context"],
                    "zh_tw": zhtw["story_content"][idx]["context"],
                }
                tempContent["voice"] = zhcn["story_content"][idx]["voice_line"]
                tempContent["book"] = zhcn["story_content"][idx]["book_image"]
                Res["content"].append(tempContent)
            json.dump(
                Res,
                open(
                    f"test_stories/unitstory_chara/{cs['id']}.json",
                    "w",
                    encoding="utf-8",
                ),
                ensure_ascii=False,
                indent=2,
            )


def processUnitDragonStory():
    for c in tqdm.tqdm(indexJson["unitstory_dragon"]):
        for idx, cs in enumerate(indexJson["unitstory_dragon"][c]["content"]):
            Res = {
                "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                "outline": {
                    "title": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "content": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                },
                "prev": "",
                "next": "",
                "content": [],
            }
            if len(indexJson["unitstory_dragon"][c]["content"]) > 1:
                if idx == 0:
                    Res["next"] = indexJson["unitstory_dragon"][c]["content"][idx + 1][
                        "id"
                    ]
                elif idx == len(indexJson["unitstory_dragon"][c]["content"]) - 1:
                    Res["prev"] = indexJson["unitstory_dragon"][c]["content"][idx - 1][
                        "id"
                    ]
                else:
                    Res["prev"] = indexJson["unitstory_dragon"][c]["content"][idx - 1][
                        "id"
                    ]
                    Res["next"] = indexJson["unitstory_dragon"][c]["content"][idx + 1][
                        "id"
                    ]
            enus = json.load(
                open(
                    f"test_stories/en_us/unitstory_dragon/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            jajp = json.load(
                open(
                    f"test_stories/ja_jp/unitstory_dragon/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhcn = json.load(
                open(
                    f"stories_noascii/unitstory_dragon/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            zhtw = json.load(
                open(
                    f"test_stories/zh_tw/unitstory_dragon/{cs['id']}.json",
                    "r",
                    encoding="utf8",
                )
            )
            try:
                assert (
                    len(enus["story_content"])
                    == len(jajp["story_content"])
                    == len(zhcn["story_content"])
                    == len(zhtw["story_content"])
                )
            except AssertionError:
                """
                3100102
                34 35 34 34
                """
                print(cs["id"])
                print(
                    len(enus["story_content"]),
                    len(jajp["story_content"]),
                    len(zhcn["story_content"]),
                    len(zhtw["story_content"]),
                )
                exit(-1)
            Res["title"][
                "en_us"
            ] = f"{indexJson['unitstory_dragon'][c]['name']['en_us']}  {cs['name']['en_us']}"
            Res["title"][
                "ja_jp"
            ] = f"{indexJson['unitstory_dragon'][c]['name']['ja_jp']} {cs['name']['ja_jp']}"
            Res["title"][
                "zh_cn"
            ] = f"{indexJson['unitstory_dragon'][c]['name']['zh_cn']} {cs['name']['zh_cn']}"
            Res["title"][
                "zh_tw"
            ] = f"{indexJson['unitstory_dragon'][c]['name']['zh_tw']} {cs['name']['zh_tw']}"

            Res["outline"]["title"]["en_us"] = enus["outline"]["title"]
            Res["outline"]["title"]["ja_jp"] = jajp["outline"]["title"]
            Res["outline"]["title"]["zh_cn"] = zhcn["outline"]["title"]
            Res["outline"]["title"]["zh_tw"] = zhtw["outline"]["title"]
            Res["outline"]["content"]["ja_jp"] = jajp["outline"]["content"]
            Res["outline"]["content"]["en_us"] = (
                ""
                if enus["outline"]["content"] == ""
                else enus["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_cn"] = (
                ""
                if zhcn["outline"]["content"] == ""
                else zhcn["outline"]["content"][0]
            )
            Res["outline"]["content"]["zh_tw"] = (
                ""
                if zhtw["outline"]["content"] == ""
                else zhtw["outline"]["content"][0]
            )

            for idx in range(len(zhcn["story_content"])):
                tempContent = {
                    "icon": "",
                    "name": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "context": {"en_us": "", "ja_jp": "", "zh_cn": "", "zh_tw": ""},
                    "voice": "",
                    "book": "",
                }
                if len(zhcn["story_content"][idx]["speaker_id"]) != 0:
                    tempContent["icon"] = zhcn["story_content"][idx]["speaker_id"][-1]
                else:
                    if jajp["story_content"][idx]["speaker_id"] != "":
                        tempContent["icon"] = jajp["story_content"][idx]["speaker_id"]
                tempContent["name"] = {
                    "en_us": enus["story_content"][idx]["speaker_name"],
                    "ja_jp": jajp["story_content"][idx]["speaker_name"],
                    "zh_cn": zhcn["story_content"][idx]["speaker_name"],
                    "zh_tw": zhtw["story_content"][idx]["speaker_name"],
                }
                tempContent["context"] = {
                    "en_us": enus["story_content"][idx]["context"],
                    "ja_jp": jajp["story_content"][idx]["context"],
                    "zh_cn": zhcn["story_content"][idx]["context"],
                    "zh_tw": zhtw["story_content"][idx]["context"],
                }
                tempContent["voice"] = zhcn["story_content"][idx]["voice_line"]
                tempContent["book"] = zhcn["story_content"][idx]["book_image"]
                Res["content"].append(tempContent)
            json.dump(
                Res,
                open(
                    f"test_stories/unitstory_dragon/{cs['id']}.json",
                    "w",
                    encoding="utf-8",
                ),
                ensure_ascii=False,
                indent=2,
            )


processCastleStory()
processQuestEventStory()
processQuestMainStory()
processUnitCharaStory()
processUnitDragonStory()
