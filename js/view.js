const params = new URLSearchParams(window.location.search);
const story_type = params.get('type');
const story_id = params.get('id');
const story_path = params.get('path');

var article = document.getElementById('story');

if (story_path) {
    loadStory(story_path);
} else if (story_type && story_id) {
    loadByTypeId(story_type, story_id);
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
            article.innerHTML += `<div id="narrator"><a href="../index.html#${story_type}">返回首页</a></div>`;
            json.story_content.forEach(function(content) {
                if ($.inArray(content.speaker_name, ['add_book_text', 'telop', 'SYS']) == -1) {
                    /*Dialogue here*/
                    var inner = '';
                    inner += '<div id="dialogue">';
                    inner += `<div id="speaker_icon"><img src="../icons/${content.speaker_id[0]}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/></div>`;
                    inner += `<div id="speaker_name">${content.speaker_name}</div>`;
                    inner += `<div id="speak_content">${content.context.replace(/\\n/g, '<br>')}</div>`;
                    inner += '</div>';
                    article.innerHTML += inner;
                } else {
                    /*Narration here*/
                    article.innerHTML += `<div id="narrator">${content.context.replace(/\\n/g, '<br>')}</div><br>`;
                }
            });
            article.innerHTML += `<div id="narrator"><a href="../index.html#${story_type}">返回首页</a></div>`;
        }).catch(function(error) {
            rand404();
        });
}

function loadByTypeId(type, id) {
    let story_path = `../stories/${type}/${id}.json`;
    loadStory(story_path);
    /*
    fetch('./index.json')
        .then(function(response) {
            if (!response.ok) {
                throw Error(response.statusText);
            }
            return response;
        })
        .then(response => response.json())
        .then(json => {
            console.log(json[type])
            if (json.hasOwnProperty(type)) {
                switch (type) {
                    case 'castlestory':
                        if (json[type].hasOwnProperty(id)) {
                            loadStory(json[type][id].path);
                            return;
                        }
                        break;
                }
            }
            console.log('file not exists.');
        }).catch(function(error) {
            console.log('failed while loading index.json.');
        });
    */
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

function getTypeByID(id) {
    /*
    castlestory: 1**** + ** (len: 7)       <-
    queststory_event: 2**** + ** (len: 7)    |= same format so no
    queststory_main: 1**** + ** (len: 7)   <-
    unitstory_chara: 1******* + ** (len: 9)
    unitstory_dragon: 2******* + ** (len: 9)
    */
}