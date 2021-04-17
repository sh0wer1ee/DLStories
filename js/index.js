const params = new URLSearchParams(window.location.search);
const story_type = params.get('type');
const story_id = params.get('id');
const story_path = params.get('path');

document.title = `${story_type} ${story_id}`;
var article = document.getElementById('story');

if (!story_path) {
    loadByTypeId(story_type, story_id);
} else {
    loadStory(story_path);
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
            json.story_content.forEach(function(content) {
                if ($.inArray(content.speaker_name, ['add_book_text', 'telop', 'SYS']) == -1) {
                    /*Dialogue here*/
                    var inner = '';
                    inner += '<div id="dialogue">';
                    inner += '<div id="speaker_icon"><img src="https://gitee.com/sh0wer1ee/dlicons/raw/master/icons/DummyIcon.png"/></div>'; //MISSING
                    inner += `<div id="speaker_name">${content.speaker_name}</div>`;
                    inner += `<div id="speak_content">${content.context.replace(/\\n/g, '<br>')}</div>`;
                    inner += '</div>';
                    article.innerHTML += inner;
                } else {
                    /*Narration here*/
                    article.innerHTML += `<div id="narrator">${content.context.replace(/\\n/g, '<br>')}</div><br>`;
                }
            });
        }).catch(function(error) {
            console.log('failed while loading story script.');
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

function getTypeByID(id) {
    /*
    castlestory: 1**** + ** (len: 7)       <-
    queststory_event: 2**** + ** (len: 7)    |= same format so no
    queststory_main: 1**** + ** (len: 7)   <-
    unitstory_chara: 1******* + ** (len: 9)
    unitstory_dragon: 2******* + ** (len: 9)
    */
}