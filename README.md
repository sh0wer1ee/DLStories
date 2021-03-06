# DLStories

A site that lists Dragalia Lost stories (experimental & **simplified Chinese Localization only**). Raw assets are parsed and processed to novel-like contents.

## Demo

- [gitee page](https://sh0wer1ee.gitee.io/dlstories/)
- [github page](https://sh0wer1ee.github.io/DLStories/) **(audio available)**

## Tools

- [Surtr Language Translator](https://sh0wer1ee.github.io/DLStories/translator) **Only CHS and EN supported**

## TODO list

- [x] Finish the asset parser
- [x] Export story data json
- [x] Push these stories into html
- [x] Make a good-looking UI
- [x] favicon.ico
- [x] Collect missing story files
- [x] Make chapter/castlestory/event icons
- [x] More user-friendly (previous episode & next episode)
- [x] Add voices (impossible in gitee but you can test ghpage)
- [ ] Add event CG or event video
- [ ] Adjust python scripts (like DLPortraits to deal with increment update)
- [ ] Figure out the id mapping
- [ ] Generate portrait icons with proper emotion (impossible)
- [ ] Sorting by release date (need help)

## Current missing story files

| ID  | NAME |
| --- | ---- |
| x   | x    |

Currently all the story scripts are found.

## Missing event icons

| ID  | NAME |
| --- | ---- |
| x   | x    |

Currently all the icons are made.

## Some Memos

### Command type (Common)(WIP)

Please refer to `func/parsed_funtion.py`.

- Text related
  > - `OL_TITLE("title")`: title of the outline.
  > - `outline("text")`: outline of the story.
  > - `telop(param1, param2, param3, param4)`: show up to four lines of superimposed texts on screen.
  > - `add_book_text("text", param2)`: print book texts. optional param2 is filename of a book image.
  > - `print(param1, param2)`: print texts. optional param2 is filename of a voice line if full-voice.
- Set chara (key functions to get chara ID)
  > - `CHARA_SET("eye", "lip", "POS", "CID", "int")`: fade in one chara(`"CID"`) at given location(`"POS"`) and given emotion(`"eye", "lip", "int"`). `"int"` will be pass to `chara_face`, which is important in emotion research.
  > - `CHARA_SET2("eye", "lip", "CID", "int", "eye2", "lip2", "CID2", "int2")`:
  > - `CHARA_SET3("eye", "lip", "CID", "int", "eye2", "lip2", "CID2", "int2" "eye3", "lip3", "CID3", "int3")`:
  > - `CharaSet`...
  > - `CHARA_KAMITE_SE`...
  > - `CHANGE_DRAGON_RELEASE`...
  > - ...I give up

**Currently** I use the recently appeared id(s) to decide the speaker icon (but not that accurate). So at this point I can fix them manually, and please feel free to open an issue or pr.

- Effects
  > - `xxxx_EMO` emotion bubble
- Codes
  > - `func_research.py`: transform the function into python code and json (output in `func` folder) to help me research the story scripts.
  > - etc.
