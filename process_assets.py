import os
import re
import shutil
import json
import tqdm
import errno
import UnityPy

# story.awakeningstory/rarity*_1*****_**
# story.castlestory/100****
# story.ingame000* 
# story.queststory.event/2******
# story.queststory.main/100****
# story.tutorial/t******
# story.unitstory.chara/1********
# story.unitstory.dragon/2********

ROOT = os.path.dirname(os.path.realpath(__file__))
#--CONFIG--#
playerNameCHS = '尤蒂尔'
playerName = {
    'zh_cn':'尤蒂尔'
}
lang = 'zh_cn'
masterJSONPath = 'json/'
storyDir = './stories'
INPUT = os.path.join(ROOT, 'assets')
OUTPUT = os.path.join(ROOT, 'stories')
TEST = os.path.join(ROOT, 'json_research')
support_path_format = [
    'story.castlestory',
    'story.queststory.event',
    'story.queststory.main',
    'story.unitstory.chara',
    'story.unitstory.dragon'
]
#--CONFIG--#
os.makedirs(INPUT, exist_ok=True)
os.makedirs(OUTPUT, exist_ok=True)

textlabel = {}
storyDataJson = {
    'castlestory':{},# id: {story_name, path}
    'queststory_event':{},# event_id: {event_name, content: [{story_id, episode, story_name, path}]}
    'queststory_main':{},# chapter_id: {chapter_name, content: [{story_id, title, story_name, path}]}
    'unitstory_chara':{},# chara_id: {chara_name, content: [{story_id, episode, story_name, path}]}
    'unitstory_dragon':{}# dragon_id: {dragon_name, content: [{story_id, story_name, path}]}
}
specialEventDic = {
    '21001': '真耶梦加得的试炼',
    '21002': '真墨丘利的试炼',
    '21003': '真布伦希尔德的试炼',
    '21004': '真朱庇特的试炼',
    '21005': '真佐迪亚克的试炼',
    '21601': '宝龙之挑战',
    '21900': '阿基德叛乱战',
    '21901': '卢弗·托修卡特尔叛乱战',
    '21902': '凯严叛乱战',
    '21903': '谢希耶尔叛乱战',
    '21904': '彩羽&乙羽叛乱战',
    '21905': '塔耳塔洛斯叛乱战',
    '22805': '天魔封灭战 暗之章'
}
forbiddenEventList = [
    '20811', '20812', '20813', '20814',
    '21701', '21702'
]
textlabelJson = json.load(open(masterJSONPath + 'TextLabel.json', encoding='utf8'))
charadataJson = json.load(open(masterJSONPath + 'CharaData.json', encoding='utf8'))
dragondataJson = json.load(open(masterJSONPath + 'DragonData.json', encoding='utf8'))
funcDataJson = {}

def retrieveStoryJson(input):
    env = UnityPy.load(input)
    for obj in env.objects:
        if obj.type in ['MonoBehaviour']:
            data = obj.read()
            tree = data.type_tree
            dic = dict(zip(tree['functions'][0]['variables']['entriesKey'], tree['functions'][0]['variables']['entriesValue']))
            #json.dump(dic, open('funcData.json', 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
            return dic

def parseStory(filePath):
    env = UnityPy.load(filePath)
    for obj in env.objects:
        if obj.type in ['MonoBehaviour']:
            data = obj.read()
            tree = data.type_tree
            filename, storyname = generateName(filePath)
            if filename == 'INVALID' and storyname == 'INVALID':
                continue
            outPath = OUTPUT + filename
            #outPath = TEST + generateName(filePath)
            os.makedirs(os.path.dirname(outPath), exist_ok=True)
            #json.dump(tree, open(outPath, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
            json.dump(parseMono(tree, storyname), open(outPath, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
                
def parseMono(tree, storyname):
    # JSON:    {story_id, story_name, story_icon, outline: {title, content}, story_content: [{speaker_id:[], speaker_name, context, voice_line, book_image}]}
    res = {
        'story_id':'',
        'story_name':f'{storyname}',
        'story_icon':'',
        'outline':{
            'title':'',
            'content':''
        },
        'story_content':[]
    }
    for func in tree['functions']: # multiple functions  e.g.2082806
        speaker_id = []
        for command in func['commandList']:
            commandType = command['command']
            commandData = command['args']
            if commandType in ['telop', 'add_book_text', 'print']:# printable text function
                content = {
                    'speaker_id':[],
                    'speaker_name': '',
                    'context':'',
                    'voice_line':'',
                    'book_image':''
                }
                if commandType == 'telop':
                    content['speaker_name'] = commandType
                    for line in commandData:
                        content['context'] = f'{content["context"]}\\n{line}'
                    content['context'] = content['context'].replace('{player_name}', playerName[lang])
                    res['story_content'].append(content)
                elif commandType == 'add_book_text':
                    content['speaker_name'] = commandType
                    content['context'] = commandData[0].replace('{player_name}', playerName[lang])
                    if len(commandData) == 2:
                        content['book_image'] = commandData[1]
                    res['story_content'].append(content)
                elif commandType == 'print':
                    content['speaker_name'] = commandData[0].replace('{player_name}', playerName[lang])
                    content['context'] = commandData[1].replace('{player_name}', playerName[lang])
                    if len(commandData) == 3:
                        content['voice_line'] = commandData[2]
                    content['speaker_id'] = speaker_id
                    res['story_content'].append(content)
            elif commandType == 'OL_TITLE':
                res['outline']['title'] = commandData
            elif commandType == 'outline':
                res['outline']['content'] = commandData
            else:
                # some functions may contain speaker id(s), but too many functions exist
                temp_speaker_id = []
                for arg in commandData:
                    if arg.startswith('c') or arg.startswith('d'):
                        try:
                            id_str = funcDataJson[arg]
                            if id_str.endswith('b') or id_str.endswith('c'):
                                id_str = id_str[:-1]
                            if len(id_str) == 12 and id_str.count('_') == 2:
                                id_str = '_'.join([id_str.split('_')[0], id_str.split('_')[1]])
                            temp_speaker_id.append(id_str)
                        except KeyError:
                            pass
                if len(temp_speaker_id) > 0:
                    speaker_id = temp_speaker_id
    return res

def generateName(filepath):
    res = ''
    res_name = ''
    fileName = os.path.basename(filepath)
    if 'story.castlestory' in filepath:
        try:
            castleStoryName = textlabel[('STORY_CASTLE_NAME_%s') % fileName]
        except KeyError:
            castleStoryName = fileName
        res = f'/castlestory/{fileName}.json'
        # JSON format    id: {story_name, path}
        try:
            storyDataJson['castlestory'][fileName]
        except KeyError:
            storyDataJson['castlestory'][fileName] = {}
        storyDataJson['castlestory'][fileName]['story_name'] = castleStoryName
        storyDataJson['castlestory'][fileName]['path'] = f'{storyDir}{res}'
        res_name = f'城堡剧情 {castleStoryName}'
    elif 'story.queststory.event' in filepath:
        eventID = fileName[:5]
        eventName = ''
        storyName = ''
        episode = ''
        questStoryEventData = {}
        if eventID in forbiddenEventList:
            return 'INVALID', 'INVALID'
        try:
            eventName = textlabel[('EVENT_NAME_%s') % eventID]
        except KeyError:
            try:
                eventName = textlabel[('QUEST_GROUP_NAME_%s') % eventID]
            except KeyError:
                if eventID in specialEventDic:
                    eventName = specialEventDic[eventID]
                else:
                    return 'INVALID', 'INVALID'
        try:
            storyName = textlabel[('STORY_QUEST_NAME_%s') % fileName]
        except KeyError:
            storyName = fileName
        try:
            episode = textlabel[('STORY_QUEST_TITLE_%s') % fileName]
        except KeyError:
            #episode = fileName[5:]
            episode = ''
        res = f'/queststory_event/{fileName}.json'
        #JSON format    event_id: {event_name, content: [{story_id, episode, story_name, path}]}
        try:
            storyDataJson['queststory_event'][eventID]
        except KeyError:
            storyDataJson['queststory_event'][eventID] = {}
            storyDataJson['queststory_event'][eventID]['event_name'] = eventName
            storyDataJson['queststory_event'][eventID]['content'] = []
        questStoryEventData['story_id'] = fileName
        questStoryEventData['episode'] = episode
        questStoryEventData['story_name'] = storyName
        questStoryEventData['path'] = f'{storyDir}{res}'
        res_name = f'{eventName}{episode} {storyName}'
        storyDataJson['queststory_event'][eventID]['content'].append(questStoryEventData)
    elif 'story.queststory.main' in filepath:
        chapterID = fileName[:5]
        title = ''
        storyName = ''
        chapterName = ''
        questStoryMainData = {}
        try:
            chapterName = textlabel[('QUEST_GROUP_NAME_%s') % chapterID]
        except KeyError:
            chapterName = chapterID
        try:
            title = textlabel[('STORY_QUEST_TITLE_%s') % fileName]
        except KeyError:
            title = fileName
        try:
            storyName = textlabel[('STORY_QUEST_NAME_%s') % fileName]
        except KeyError:
            storyName = fileName 
        res = f'/queststory_main/{fileName}.json'
        # chapter_id: {chapter_name, content: [{story_id, title, story_name, path}]}
        try:
            storyDataJson['queststory_main'][chapterID]
        except KeyError:
            storyDataJson['queststory_main'][chapterID] = {}
            storyDataJson['queststory_main'][chapterID]['chapter_name'] = chapterName
            storyDataJson['queststory_main'][chapterID]['content'] = []
        questStoryMainData['story_id'] = fileName
        questStoryMainData['title'] = title
        questStoryMainData['story_name'] = storyName
        questStoryMainData['path'] = f'{storyDir}{res}'
        res_name = f'{chapterName} {title} {storyName}'
        storyDataJson['queststory_main'][chapterID]['content'].append(questStoryMainData)
    elif 'story.unitstory.chara' in filepath:
        charaName = ''
        storyName = ''
        charaID = fileName[:8]
        charaBaseID = fileName[:6]
        charaVariationId = fileName[6:8]
        episode = fileName[-1]
        unitStoryCharaData = {}
        for cd in charadataJson:
            if charadataJson[cd]['_BaseId'] == int(charaBaseID) and charadataJson[cd]['_VariationId'] == int(charaVariationId) and str(charadataJson[cd]['_Id'])[0] != '9':
                # some id begin with 9 match the condition but is not correct.
                try:
                    if charadataJson[cd]['_VariationId'] == 1:
                        charaName = textlabel[charadataJson[cd]['_Name']]
                        break
                    else: # Zena(Another Zethia) is special here, she uses Zethia's baseID but VariationId is not 1
                          # And she is technically an alter of Zethia but not with second name.
                        charaName = textlabel[charadataJson[cd]['_SecondName']]
                        break
                except KeyError:
                    charaName = textlabel[charadataJson[cd]['_Name']]
                    break     
        try:
            storyName = textlabel[f'STORY_UNIT_NAME_{fileName}']
        except KeyError:
            storyName = fileName
        res = f'/unitstory_chara/{fileName}.json'
        # chara_id: {chara_name, content: [{story_id, episode, story_name, path}]}
        try:
            storyDataJson['unitstory_chara'][charaID]
        except KeyError:
            storyDataJson['unitstory_chara'][charaID] = {}
            storyDataJson['unitstory_chara'][charaID]['chara_name'] = charaName
            storyDataJson['unitstory_chara'][charaID]['content'] = []
        unitStoryCharaData['story_id'] = fileName
        episode_name = textlabel[f'STORY_QUEST_TITLE_EP{episode}']
        unitStoryCharaData['episode'] = episode_name
        unitStoryCharaData['story_name'] = storyName
        unitStoryCharaData['path'] = f'{storyDir}{res}'
        res_name = f'{charaName} {episode_name} {storyName}'
        storyDataJson['unitstory_chara'][charaID]['content'].append(unitStoryCharaData)
    elif 'story.unitstory.dragon' in filepath:
        dragonName = ''
        storyName = ''
        dragonID = fileName[:8]
        dragonBaseID = fileName[:6] # the unique one
        unitStoryDragonData = {}
        # dragonVariationId = fileName[6:8] # sadly the dragon alt wont get a different VariationId except some dragon npc
        for dd in dragondataJson:
            if dragondataJson[dd]['_BaseId'] == int(dragonBaseID):
                try:
                    dragonName = textlabel[dragondataJson[dd]['_SecondName']]
                    break
                except KeyError:
                    dragonName = textlabel[dragondataJson[dd]['_Name']]
                    break
        try:
            storyName = textlabel[('STORY_UNIT_NAME_%s') % fileName]
        except KeyError:
            storyName = fileName
        res = f'/unitstory_dragon/{fileName}.json'
        # dragon_id: {dragon_name, content: [{story_id, story_name, path}]}
        try:
            storyDataJson['unitstory_dragon'][dragonID]
        except KeyError:
            storyDataJson['unitstory_dragon'][dragonID] = {}
            storyDataJson['unitstory_dragon'][dragonID]['dragon_name'] = dragonName
            storyDataJson['unitstory_dragon'][dragonID]['content'] = []
        unitStoryDragonData['story_id'] = fileName
        unitStoryDragonData['story_name'] = storyName
        unitStoryDragonData['path'] = f'{storyDir}{res}'
        res_name = f'{dragonName} {storyName}'
        storyDataJson['unitstory_dragon'][dragonID]['content'].append(unitStoryDragonData)
    return res, res_name

def main():
    global funcDataJson
    for tid in textlabelJson:
        textlabel[textlabelJson[tid]['_Id']] = textlabelJson[tid]['_Text']
    funcDataJson = retrieveStoryJson('assets/story/function')
    for root, dirs, files in os.walk(INPUT, topdown=False):
        if files and os.path.basename(root) in support_path_format:
            pbar = tqdm.tqdm(files)
            for f in pbar:
                pbar.set_description('processing %s...' % f)
                src = os.path.realpath(os.path.join(root, f))
                parseStory(src)
    json.dump(storyDataJson, open('index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()