# DLStories (**WIP!**)
A site that lists Dragalia Lost stories (experimental). Raw assets are parsed and processed to novel-like contents.
## TODO list
- [x] Finish the asset parser
- [x] Export story data json
- [x] Adjust the old parser code
- [x] Push these stories into html
- [x] Make a good-looking UI
- [x] favicon.ico?
- [ ] Figure out the id mapping
- [ ] More user-friendly
- [ ] Collect missing story files
- [ ] Generate portrait icons (emotion research)
- [ ] Add voices (copyrights?)
## Current missing story files
| NAME | ID1 | ID2 | ID3 | ID4 |
|----------------------------|---|---|---|---|
|   |   |   |   |   |
Currently all the story scripts are found.
## Some Memos
### Command type (Common)(WIP)
- Text related
>- `OL_TITLE("title")`: title of the outline.
>- `outline("text")`: outline of the story.
>- `telop(param1, param2, param3, param4)`: show up to four lines of superimposed texts on screen.
>- `add_book_text("text", param2)`: print book texts. optional param2 is filename of a book image.
>- `print(param1, param2)`: print texts. optional param2 is filename of a voice line if full-voice.
- Set chara (key functions to get chara ID)
>- `CHARA_SET("eye", "lip", "POS", "CID", "int")`: fade in one chara(`"CID"`) at given location(`"POS"`) and given emotion(`"eye", "lip", "int"`). `"int"` will be pass to `chara_face`, which is important in emotion research.
>- `CHARA_SET2("eye", "lip", "CID", "int", "eye2", "lip2", "CID2", "int2")`:
>- `CHARA_SET3("eye", "lip", "CID", "int", "eye2", "lip2", "CID2", "int2" "eye3", "lip3", "CID3", "int3")`:
>- `CharaSet`...
>- `CHARA_KAMITE_SE`...
>- `CHANGE_DRAGON_RELEASE`...
>- too many f^*kin' funcs... Rua Guess I should find another way

**Currently** I use the recently appeared id(s) to decide the speaker icon (but not that accurate). So at this point I can fix them manually, and please feel free to open an issue or pr.
- Effects
>- `xxxx_EMO` emotion bubble
- Codes
>- `func_research.py`: transform the function into python code and json (output in `func` folder) to help me research the story scripts.