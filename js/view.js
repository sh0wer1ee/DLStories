import { localizationText } from "./i18n.js";

const params = new URLSearchParams(window.location.search);
const story_type = params.get("type");
const story_id = params.get("id");
const lang = params.get("lang");
//const story_path = params.get('path');

var language = "ja_jp";
var article = document.getElementById("story");
const svg_volume_up = `
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-volume-up" viewBox="0 0 16 16">
  <path d="M11.536 14.01A8.473 8.473 0 0 0 14.026 8a8.473 8.473 0 0 0-2.49-6.01l-.708.707A7.476 7.476 0 0 1 13.025 8c0 2.071-.84 3.946-2.197 5.303l.708.707z"/>
  <path d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.483 5.483 0 0 1 11.025 8a5.483 5.483 0 0 1-1.61 3.89l.706.706z"/>
  <path d="M10.025 8a4.486 4.486 0 0 1-1.318 3.182L8 10.475A3.489 3.489 0 0 0 9.025 8c0-.966-.392-1.841-1.025-2.475l.707-.707A4.486 4.486 0 0 1 10.025 8zM7 4a.5.5 0 0 0-.812-.39L3.825 5.5H1.5A.5.5 0 0 0 1 6v4a.5.5 0 0 0 .5.5h2.325l2.363 1.89A.5.5 0 0 0 7 12V4zM4.312 6.39 6 5.04v5.92L4.312 9.61A.5.5 0 0 0 4 9.5H2v-3h2a.5.5 0 0 0 .312-.11z"/>
</svg>
`;

if (lang) {
  language = lang;
}
setFont(language);

/*if (story_path) { //debug use
    loadStory(story_path);
} else*/
if (story_type && story_id) {
  loadStory(`../stories/${story_type}/${story_id}.json`, language);
} else {
  rand404();
}

function setFont(language) {
  switch (language) {
    case "en_us":
      article.style.fontFamily = '"DLFont EN", sans-serif';
      break;
    case "ja_jp":
      article.style.fontFamily = '"DLFont JP", sans-serif';
      break;
    case "zh_cn":
      article.style.fontFamily = '"Noto Sans SC", sans-serif';
      break;
    case "zh_tw":
      article.style.fontFamily = '"DLFont TC", sans-serif';
      break;
    default:
      console.log('lang can only be "en_us", "ja_jp", "zh_cn", "zh_tw"!');
  }
}

function loadStory(story_path, language) {
  fetch(story_path)
    .then(function (response) {
      if (!response.ok) {
        throw Error(response.statusText);
      }
      return response;
    })
    .then((response) => response.json())
    .then((json) => {
      document.title = `${json.title[language]}`;
      var navi = '<div id="navigator">';
      if (json.prev) {
        navi += `<div id="prev"><a href="../stories/view.html?type=${story_type}&id=${json.prev}&lang=${language}">${localizationText["prev_story"][language]}</a></div>`;
      }
      navi += `<div id="index"><a href="../index.html#${story_type}">${localizationText["back_to_index"][language]}</a></div>`;
      if (json.next) {
        navi += `<div id="next"><a href="../stories/view.html?type=${story_type}&id=${json.next}&lang=${language}">${localizationText["next_story"][language]}</a></div>`;
      }
      navi += "</div>";
      article.innerHTML += navi;
      json.content.forEach(function (content) {
        if (content.context[language])
          if (
            $.inArray(content.name[language], [
              "add_book_text",
              "telop",
              "SYS",
            ]) == -1
          ) {
            /*Dialogue here*/
            var inner = "";
            inner += '<div id="dialogue">';
            inner += '<div id="speaker_icon">';
            if (content.voice) {
              inner += `<a onclick="playVoiceLine('${content.voice}');">`;
              inner += `<img src="../icons/${content.icon}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/>`;
              inner += `${svg_volume_up}</a>`;
            } else {
              inner += `<img src="../icons/${content.icon}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/>`;
            }
            inner += "</div>";
            inner += `<div id="speaker_name">${content.name[language]}</div>`;
            inner += `<div id="speak_content">${content.context[
              language
            ].replace(/\\n/g, "<br>")}</div>`;
            inner += "</div>";
            article.innerHTML += inner;
          } else {
            /*Narration here*/
            article.innerHTML += `<div id="narrator">${content.context[
              language
            ].replace(/\\n/g, "<br>")}</div><br>`;
          }
      });
      article.innerHTML += navi;
    })
    .catch(function (error) {
      console.log(error);
      rand404();
    });
}

function rand404() {
  document.title = "404";
  var rand = parseInt(Math.random() * 10, 10);
  var inner = "";
  inner += `<div id="narrator">${localizationText["story_load_failed"][language]}~</div><br>`;
  inner += `<div id="narrator"><a href="https://store.line.me/stickershop/product/13819985">`;
  inner += `<img src="../icons/404/line${rand}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/></a></div><br>`;
  inner += `<div id="narrator"><a href="../index.html">${localizationText["back_to_index"][language]}</a></div>`;
  article.innerHTML += inner;
  console.log("failed while loading story script.");
}

// function getTypeByID(id) {
//   /*
//     castlestory: 1**** + ** (len: 7)       <-
//     queststory_event: 2**** + ** (len: 7)    |= same format so no
//     queststory_main: 1**** + ** (len: 7)   <-
//     unitstory_chara: 1******* + ** (len: 9)
//     unitstory_dragon: 2******* + ** (len: 9)
//     */
// }
