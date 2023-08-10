/*
https://stackoverflow.com/questions/7862233/twitter-bootstrap-tabs-go-to-specific-tab-on-page-reload-or-hyperlink
*/

import { localizationText } from "./i18n.js";

// Javascript to enable link to tab
var hash = location.hash.replace(/^#/, ""); // ^ means starting, meaning only match the first hash
if (hash) {
  $('.nav-tabs a[href="#' + hash + '"]').tab("show");
}
// Change hash for page-reload
$(".nav-tabs a").on("shown.bs.tab", function (e) {
  window.location.hash = e.target.hash;
});

const params = new URLSearchParams(window.location.search);
const lang = params.get("lang");
const languageSvg = ` <svg xmlns="http://www.w3.org/2000/svg" height="1.6em" viewBox="0 0 640 512"><style>svg {fill: #ffffff;}</style>
<path d="M0 128C0 92.7 28.7 64 64 64H256h48 16H576c35.3 0 64 28.7 64 64V384c0 35.3-28.7 64-64 64H320 304 256 64c-35.3 0-64-28.7-64-64V128zm320 0V384H576V128H320zM178.3 175.9c-3.2-7.2-10.4-11.9-18.3-11.9s-15.1 4.7-18.3 11.9l-64 144c-4.5 10.1 .1 21.9 10.2 26.4s21.9-.1 26.4-10.2l8.9-20.1h73.6l8.9 20.1c4.5 10.1 16.3 14.6 26.4 10.2s14.6-16.3 10.2-26.4l-64-144zM160 233.2L179 276H141l19-42.8zM448 164c11 0 20 9 20 20v4h44 16c11 0 20 9 20 20s-9 20-20 20h-2l-1.6 4.5c-8.9 24.4-22.4 46.6-39.6 65.4c.9 .6 1.8 1.1 2.7 1.6l18.9 11.3c9.5 5.7 12.5 18 6.9 27.4s-18 12.5-27.4 6.9l-18.9-11.3c-4.5-2.7-8.8-5.5-13.1-8.5c-10.6 7.5-21.9 14-34 19.4l-3.6 1.6c-10.1 4.5-21.9-.1-26.4-10.2s.1-21.9 10.2-26.4l3.6-1.6c6.4-2.9 12.6-6.1 18.5-9.8l-12.2-12.2c-7.8-7.8-7.8-20.5 0-28.3s20.5-7.8 28.3 0l14.6 14.6 .5 .5c12.4-13.1 22.5-28.3 29.8-45H448 376c-11 0-20-9-20-20s9-20 20-20h52v-4c0-11 9-20 20-20z"/></svg> `;
var language = "ja_jp";

var cs = document.getElementById("castlestory-div");
var qs_e = document.getElementById("queststory_event-div");
var qs_m = document.getElementById("queststory_main-div");
var us_c = document.getElementById("unitstory_chara-div");
var us_d = document.getElementById("unitstory_dragon-div");

if (lang) {
  language = lang;
} else {
  var userLang = navigator.language || navigator.userLanguage;
  switch (userLang) {
    case "zh-CN":
      language = "zh_cn";
      break;
    case "zh-TW":
    case "zh-HK":
      language = "zh_tw";
      break;
    case "ja":
      language = "ja_jp";
      break;
    case "en-GB":
    case "en-US":
      language = "en_us";
      break;
    default:
      language = "ja_jp";
  }
  console.log(language);
}

initializeUpdateTime();
initializeLanguageSelector();
resetLanguage(language);

function resetLanguage(language) {
  document.title = localizationText["title"][language];
  setFont(language);
  document.getElementById("castlestory-tab").innerHTML =
    localizationText["castlestory"][language];
  document.getElementById("queststory_event-tab").innerHTML =
    localizationText["queststory_event"][language];
  document.getElementById("queststory_main-tab").innerHTML =
    localizationText["queststory_main"][language];
  document.getElementById("unitstory_chara-tab").innerHTML =
    localizationText["unitstory_chara"][language];
  document.getElementById("unitstory_dragon-tab").innerHTML =
    localizationText["unitstory_dragon"][language];
  document.getElementById("dropdownMenuButton").innerHTML =
    localizationText["language"][language] + languageSvg;
  loadIndexJson();
}

function setFont(language) {
  var container = document.getElementById("main-container");
  switch (language) {
    case "en_us":
      container.style.fontFamily = '"Roboto Condensed 700", sans-serif';
      break;
    case "ja_jp":
      container.style.fontFamily = '"Noto Sans JP 700", sans-serif';
      break;
    case "zh_cn":
      container.style.fontFamily = '"Noto Sans SC 700", sans-serif';
      break;
    case "zh_tw":
      container.style.fontFamily = '"Noto Sans TC", sans-serif';
      break;
  }
}

function initializeUpdateTime() {
  let currentUrl = window.location.href;
  if (currentUrl.includes("gitee")) {
    lastCommitGitee();
  } else {
    lastCommitGithub();
  }
}

function initializeLanguageSelector() {
  document.getElementById("dropdown-en_us").href = "./index.html?lang=en_us";
  document.getElementById("dropdown-ja_jp").href = "./index.html?lang=ja_jp";
  document.getElementById("dropdown-zh_cn").href = "./index.html?lang=zh_cn";
  document.getElementById("dropdown-zh_tw").href = "./index.html?lang=zh_tw";
}

function lastCommitGitee() {
  fetch("https://gitee.com/api/v5/repos/sh0wer1ee/dlstories/commits")
    .then(function (response) {
      if (!response.ok) {
        throw Error(response.statusText);
      }
      return response;
    })
    .then((response) => response.json())
    .then((json) => {
      latestTime = json[0].commit.author.date;
      var d = new Date(latestTime);
      var datestring =
        d.getFullYear() +
        "/" +
        ("0" + (d.getMonth() + 1)).slice(-2) +
        "/" +
        ("0" + d.getDate()).slice(-2) +
        " " +
        ("0" + d.getHours()).slice(-2) +
        ":" +
        ("0" + d.getMinutes()).slice(-2);
      document.getElementById(
        "update-time"
      ).innerText = `${localizationText["recent_update"][language]} ${datestring}`;
      document.getElementById(
        "recommendation"
      ).innerHTML = `全语音版(速度可能会慢)：<a href="https://sh0wer1ee.github.io/DLStories/">https://sh0wer1ee.github.io/DLStories/</a>`;
    })
    .catch(function (error) {
      console.log(error);
      document.getElementById(
        "update-time"
      ).innerText = `${localizationText["recent_update"][language]} N/A`;
    });
}

function lastCommitGithub() {
  fetch("https://api.github.com/repos/sh0wer1ee/dlstories/branches/master")
    .then(function (response) {
      if (!response.ok) {
        throw Error(response.statusText);
      }
      return response;
    })
    .then((response) => response.json())
    .then((json) => {
      var latestTime = json.commit.commit.author.date;
      var d = new Date(latestTime);
      var datestring =
        d.getFullYear() +
        "/" +
        ("0" + (d.getMonth() + 1)).slice(-2) +
        "/" +
        ("0" + d.getDate()).slice(-2) +
        " " +
        ("0" + d.getHours()).slice(-2) +
        ":" +
        ("0" + d.getMinutes()).slice(-2);
      document.getElementById(
        "update-time"
      ).innerText = `Recent update: ${datestring}`;
    })
    .catch(function (error) {
      console.log(error);
      document.getElementById("update-time").innerText = `Recent update: N/A`;
    });
}

function loadIndexJson() {
  fetch("./index.json")
    .then(function (response) {
      if (!response.ok) {
        throw Error(response.statusText);
      }
      return response;
    })
    .then((response) => response.json())
    .then((json) => {
      loadCastleStory(json.castlestory);
      loadQuestStoryEvent(json.queststory_event);
      loadQuestStoryMain(json.queststory_main);
      loadUnitStoryChara(json.unitstory_chara);
      loadunitStoryDragon(json.unitstory_dragon);
    })
    .catch(function (error) {
      console.log("failed while loading index json.");
    });
}

function loadCastleStory(json) {
  var inner = "";
  for (var key in json) {
    inner += `<div class="castlestory-items">`;
    inner += `<a href="./stories/view.html?type=castlestory&id=${key}&lang=${language}">`;
    inner += `<img src="./icons/castlestory/${key}.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = './icons/DummyIcon.png';"/>`;
    inner += `<span>${json[key].name[language]}</span></a>`;
    inner += "</div>";
  }
  cs.innerHTML = inner;
  $("#cs-search").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".castlestory-items").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
  console.log("castle stories loaded.");
}

function loadQuestStoryEvent(json) {
  var inner = "";
  for (var key in json) {
    inner += '<div class="story-group">';
    inner += `<div id="story-group-questevent-icon"><img src="./icons/queststory_event/${language}/${key}.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = './icons/DummyIcon.png';"/></div>`;
    inner += `<div id="story-group-name">${json[key].name[language]}</div>`;
    inner += '<div id="story-group-items">';
    json[key].content.forEach((story) => {
      inner += `<a href="./stories/view.html?type=queststory_event&id=${story.id}&lang=${language}">${story.episode[language]} ${story.name[language]}</a><br>`;
    });
    inner += "</div></div>";
  }
  qs_e.innerHTML = inner;
  $("#qs_e-search").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".story-group").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
  console.log("event stories loaded.");
}

function loadQuestStoryMain(json) {
  var inner = "";
  for (var key in json) {
    inner += '<div class="story-group">';
    inner += `<div id="story-group-questmain-icon"><img src="./icons/queststory_main/${key}.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = './icons/DummyIcon.png';"/></div>`;
    inner += `<div id="story-group-name">${json[key].name[language]}</div>`;
    inner += '<div id="story-group-items">';
    json[key].content.forEach((story) => {
      if (story.name[language]) {
        inner += `<a href="./stories/view.html?type=queststory_main&id=${story.id}&lang=${language}">${story.title[language]} ${story.name[language]}</a><br>`;
      } else {
        inner += `<a href="./stories/view.html?type=queststory_main&id=${story.id}&lang=${language}">${story.id}</a><br>`;
      }
    });
    inner += "</div></div>";
  }
  qs_m.innerHTML = inner;
  $("#qs_m-search").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".story-group").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
  console.log("main stories loaded.");
}

function loadUnitStoryChara(json) {
  var inner = "";
  for (var key in json) {
    inner += '<div class="story-group">';
    inner += `<div id="story-group-unit-icon"><img src="./icons/unitstory_chara/${key.substring(
      0,
      6
    )}_${key.substring(
      6
    )}_r05.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/></div>`;
    inner += `<div id="story-group-name">${json[key].name[language]}</div>`;
    inner += '<div id="story-group-items">';
    json[key].content.forEach((story) => {
      inner += `<a href="./stories/view.html?type=unitstory_chara&id=${story.id}&lang=${language}">${story.episode[language]} ${story.name[language]}</a><br>`;
    });
    inner += "</div></div>";
  }
  us_c.innerHTML = inner;
  $("#us_c-search").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".story-group").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
  console.log("chara stories loaded.");
}

function loadunitStoryDragon(json) {
  var inner = "";
  for (var key in json) {
    inner += '<div class="story-group">';
    inner += `<div id="story-group-unit-icon"><img src="./icons/unitstory_dragon/${key.substring(
      0,
      6
    )}_${key.substring(
      6
    )}.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/></div>`;
    inner += `<div id="story-group-name">${json[key].name[language]}</div>`;
    inner += '<div id="story-group-items">';
    json[key].content.forEach((story) => {
      inner += `<a href="./stories/view.html?type=unitstory_dragon&id=${story.id}&lang=${language}">${story.name[language]}</a><br>`;
    });
    inner += "</div></div>";
  }
  us_d.innerHTML = inner;
  $("#us_d-search").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(".story-group").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
  console.log("dragon stories loaded.");
}
