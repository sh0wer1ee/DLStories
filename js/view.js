const params = new URLSearchParams(window.location.search);
const story_type = params.get('type');
const story_id = params.get('id');
//const story_path = params.get('path');

var article = document.getElementById('story');
var storyList = [];
var mainstory_dir = '../audio/mainstory'
var knightsstory_dir = '../audio/knightsstory'
var eventstory_dir = '../audio/eventstory'
var ingamestory_dir = '../audio/ingamestory'
var svg_volume_up = `
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-volume-up" viewBox="0 0 16 16">
  <path d="M11.536 14.01A8.473 8.473 0 0 0 14.026 8a8.473 8.473 0 0 0-2.49-6.01l-.708.707A7.476 7.476 0 0 1 13.025 8c0 2.071-.84 3.946-2.197 5.303l.708.707z"/>
  <path d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.483 5.483 0 0 1 11.025 8a5.483 5.483 0 0 1-1.61 3.89l.706.706z"/>
  <path d="M10.025 8a4.486 4.486 0 0 1-1.318 3.182L8 10.475A3.489 3.489 0 0 0 9.025 8c0-.966-.392-1.841-1.025-2.475l.707-.707A4.486 4.486 0 0 1 10.025 8zM7 4a.5.5 0 0 0-.812-.39L3.825 5.5H1.5A.5.5 0 0 0 1 6v4a.5.5 0 0 0 .5.5h2.325l2.363 1.89A.5.5 0 0 0 7 12V4zM4.312 6.39 6 5.04v5.92L4.312 9.61A.5.5 0 0 0 4 9.5H2v-3h2a.5.5 0 0 0 .312-.11z"/>
</svg>
`;

/*if (story_path) { //debug use
    loadStory(story_path);
} else*/
if (story_type && story_id) {
    if ($.inArray(story_type, ['castlestory', 'unitstory_chara', 'unitstory_dragon']) == -1) {
        loadStoryList(story_type, story_id);
    } else {
        loadByTypeId(story_type, story_id);
    }
} else {
    rand404();
}

function loadStory(story_path) {
    fetch(story_path)
        .then(function(response) {
            if (!response.ok) {
                throw Error(response.statusText);
            }
            return response;
        })
        .then(response => response.json())
        .then(json => {
            document.title = `${json.story_name}`;
            var navi = naviHtml(story_type, story_id);
            article.innerHTML += navi;
            json.story_content.forEach(function(content) {
                if ($.inArray(content.speaker_name, ['add_book_text', 'telop', 'SYS']) == -1) {
                    /*Dialogue here*/
                    var inner = '';
                    inner += '<div id="dialogue">';
                    inner += '<div id="speaker_icon">';
                    if (content.voice_line) {
                        inner += `<a onclick="playVoiceLine('${content.voice_line}');">`
                        inner += `<img src="../icons/${content.speaker_id[0]}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/>`;
                        inner += `${svg_volume_up}</a>`;
                    } else {
                        inner += `<img src="../icons/${content.speaker_id[0]}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/>`;
                    }
                    inner += '</div>';
                    inner += `<div id="speaker_name">${content.speaker_name}</div>`;
                    inner += `<div id="speak_content">${content.context.replace(/\\n/g, '<br>')}</div>`;
                    inner += '</div>';
                    article.innerHTML += inner;
                } else {
                    /*Narration here*/
                    article.innerHTML += `<div id="narrator">${content.context.replace(/\\n/g, '<br>')}</div><br>`;
                }
            });
            article.innerHTML += navi;
        }).catch(function(error) {
            rand404();
        });
}

function loadByTypeId(type, id) {
    let story_path = `../stories/${type}/${id}.json`;
    loadStory(story_path);
}

function loadStoryList(story_type, story_id) {
    fetch('../index.json')
        .then(function(response) {
            if (!response.ok) {
                throw Error(response.statusText);
            }
            return response;
        })
        .then(response => response.json())
        .then(json => {
            storyList = [];
            let base_id = story_id.substring(0, 5);
            json[story_type][base_id].content.forEach(function(item) {
                storyList.push(item["story_id"]);
            });
            loadByTypeId(story_type, story_id);
        }).catch(function(error) {
            console.log('failed while loading index.json.');
        });
}

function rand404() {
    document.title = '404';
    var rand = parseInt(Math.random() * 10, 10);
    var inner = '';
    inner += `<div id="narrator">未能成功装载剧情文件~</div><br>`;
    inner += `<div id="narrator"><a href="https://store.line.me/stickershop/product/13819985">`;
    inner += `<img src="../icons/404/line${rand}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/></a></div><br>`
    inner += `<div id="narrator"><a href="../index.html">返回首页</a></div>`;
    article.innerHTML += inner;
    console.log('failed while loading story script.');
}

function naviHtml(story_type, story_id) {
    var inner = '';
    if (story_type === 'queststory_event' || story_type === 'queststory_main') {
        var id_int = parseInt(story_id, 10);
        var len = storyList.length;
        var loc = storyList.indexOf(story_id)
        console.log(len);
        console.log(loc);
        inner += '<div id="navigator">';
        if (loc == -1 || len == 1) {
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
        } else if (loc == 0) {
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
            inner += `<div id="next"><a href="../stories/view.html?type=${story_type}&id=${id_int+1}">下一话</a></div>`;
        } else if (loc == (len - 1)) {
            inner += `<div id="prev"><a href="../stories/view.html?type=${story_type}&id=${id_int-1}">上一话</a></div>`;
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
        } else {
            inner += `<div id="prev"><a href="../stories/view.html?type=${story_type}&id=${id_int-1}">上一话</a></div>`;
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
            inner += `<div id="next"><a href="../stories/view.html?type=${story_type}&id=${id_int+1}">下一话</a></div>`;
        }
        inner += '</div>';
    } else if (story_type === 'unitstory_chara') { // each chara has 5 episodes
        var id_int = parseInt(story_id, 10);
        inner += '<div id="navigator">';
        if (story_id.endsWith("1")) {
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
            inner += `<div id="next"><a href="../stories/view.html?type=${story_type}&id=${id_int+1}">下一话</a></div>`;
        } else if (story_id.endsWith("5")) {
            inner += `<div id="prev"><a href="../stories/view.html?type=${story_type}&id=${id_int-1}">上一话</a></div>`;
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
        } else {
            inner += `<div id="prev"><a href="../stories/view.html?type=${story_type}&id=${id_int-1}">上一话</a></div>`;
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
            inner += `<div id="next"><a href="../stories/view.html?type=${story_type}&id=${id_int+1}">下一话</a></div>`;
        }
        inner += '</div>';
    } else if (story_type === 'unitstory_dragon') { // each dragon has 2 episodes
        var base = story_id.slice(0, -1);
        inner += '<div id="navigator">';
        if (story_id.endsWith("1")) {
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
            inner += `<div id="next"><a href="../stories/view.html?type=${story_type}&id=${base}2">下一话</a></div>`;
        } else {
            inner += `<div id="prev"><a href="../stories/view.html?type=${story_type}&id=${base}1">上一话</a></div>`;
            inner += `<div id="index"><a href="../index.html#${story_type}">返回首页</a></div>`;
        }
        inner += '</div>';
    } else { //castlestory or others
        inner = `<div id="navigator"><div id="index"><a href="../index.html#${story_type}">返回首页</a></div></div>`;
    }
    return inner;
}

function playVoiceLine(voice_line) {
    var path = '';
    var sp = voice_line.split('_');
    console.log(sp[2])
    if (sp[2] === 'MAINSTORY') {
        path = `${mainstory_dir}/${sp[3]}${sp[4]}/${voice_line}.mp3`;
    } else if (sp[2] === 'KNIGHTSSTORY') {
        path = `${knightsstory_dir}/${sp[3]}${sp[4]}${sp[5]}/${voice_line}.mp3`;
    } else if (sp[2] === 'EVENTSTORY') {
        path = `${eventstory_dir}/${sp[3]}${sp[4]}/${voice_line}.mp3`;
    } else if (sp[2] === 'INGAMESTORY') {
        path = `${ingamestory_dir}/${sp[3]}${sp[4]}/${voice_line}.mp3`;
    } else {
        console.log('wrong audio type!');
        return;
    }
    var vl = new Audio(path);
    vl.play();
}

function getTypeByID(id) {
    /*
    castlestory: 1**** + ** (len: 7)       <-
    queststory_event: 2**** + ** (len: 7)    |= same format so no
    queststory_main: 1**** + ** (len: 7)   <-
    unitstory_chara: 1******* + ** (len: 9)
    unitstory_dragon: 2******* + ** (len: 9)
    */
}