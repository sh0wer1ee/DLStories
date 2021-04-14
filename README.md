# DLStories (**WIP!**)
A site that lists Dragalia Lost stories. Raw assets are parsed and processed to novel-like contents.
## TODO list
- [ ] Finish the asset parser
- [ ] Export story data json
- [ ] Adjust the old parser code
- [ ] Push these stories into html
- [ ] Make a good-looking UI
- [ ] Generate portrait icons (emotion research)
- [ ] Add voices
## Some Memos
### Command type (Common)(WIP)
- Text related
>- `OL_TITLE("title")`: title of the outline.
>- `outline("text")`: outline of the story.
>- `telop(param1, param2, param3, param4)`: show up to four lines of superimposed texts on screen.
>- `add_book_text("text", param2)`: print book texts. optional param2 is filename of a book image.
>- `print(param1, param2)`: print texts. optional param2 is filename of a voice line if full-voice.
- Set chara (key functions to get chara ID)
>- `CHARA_SET("eye", "lip", "POS", "CID", "int")`: fade in one chara(`"CID"`) at given location(`"POS"`) and given emotion(`"eye", "lip", "int"`). `"int"` will be pass to `chara_face`, which is important in emotion research.※
>- `CHARA_SET2("eye", "lip", "CID", "int", "eye2", "lip2", "CID2", "int2")`:
>- `CHARA_SET3("eye", "lip", "CID", "int", "eye2", "lip2", "CID2", "int2" "eye3", "lip3", "CID3", "int3")`:
>- `CharaSet`...
>- `CHARA_KAMITE_SE`...
>- `CHANGE_DRAGON_RELEASE`...
>- ...
- Effects
>- `xxxx_EMO` emotion bubble