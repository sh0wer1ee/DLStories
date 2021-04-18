/*
https://stackoverflow.com/questions/7862233/twitter-bootstrap-tabs-go-to-specific-tab-on-page-reload-or-hyperlink
*/

// Javascript to enable link to tab
var hash = location.hash.replace(/^#/, ''); // ^ means starting, meaning only match the first hash
if (hash) {
    $('.nav-tabs a[href="#' + hash + '"]').tab('show');
}
// Change hash for page-reload
$('.nav-tabs a').on('shown.bs.tab', function(e) {
    window.location.hash = e.target.hash;
})

var cs = document.getElementById("castlestory");
var qs_e = document.getElementById("queststory_event");
var qs_m = document.getElementById("queststory_main");
var us_c = document.getElementById("unitstory_chara");
var us_d = document.getElementById("unitstory_dragon");

loadIndexJson();

function loadIndexJson() {
    fetch('./index.json')
        .then(function(response) {
            if (!response.ok) {
                throw Error(response.statusText);
            }
            return response;
        })
        .then(response => response.json())
        .then(json => {
            loadCastleStory(json.castlestory);
            loadQuestStoryEvent(json.queststory_event);
            loadQuestStoryMain(json.queststory_main);
            loadUnitStoryChara(json.unitstory_chara);
            loadunitStoryDragon(json.unitstory_dragon);
        }).catch(function(error) {
            console.log('failed while loading index.json.');
        });
}

function loadCastleStory(json) {
    var inner = '';
    for (var key in json) {
        inner += `<a href="./stories/view.html?type=castlestory&id=${key}">${json[key].story_name}</a><br>`;
    }
    cs.innerHTML = inner;
    console.log('castle stories loaded.');
}

function loadQuestStoryEvent(json) {
    var inner = '';
    for (var key in json) {
        inner += `<span>${json[key].event_name}</span><br>`
        json[key].content.forEach(story => {
            inner += `<a href="./stories/view.html?type=queststory_event&id=${story.story_id}">${story.episode} ${story.story_name}</a><br>`;
        });
    }
    qs_e.innerHTML = inner;
    console.log('event stories loaded.');
}

function loadQuestStoryMain(json) {
    var inner = '';
    for (var key in json) {
        inner += `<span>${json[key].chapter_name}</span><br>`
        json[key].content.forEach(story => {
            if (story.story_name) {
                inner += `<a href="./stories/view.html?type=queststory_main&id=${story.story_id}">${story.title} ${story.story_name}</a><br>`;
            } else {
                inner += `<a href="./stories/view.html?type=queststory_main&id=${story.story_id}">${story.story_id}</a><br>`;
            }

        });
    }
    qs_m.innerHTML = inner;
    console.log('main stories loaded.');
}

function loadUnitStoryChara(json) {
    var inner = '';
    for (var key in json) {
        inner += `<span>${json[key].chara_name}</span><br>`
        json[key].content.forEach(story => {
            inner += `<a href="./stories/view.html?type=unitstory_chara&id=${story.story_id}">${story.episode} ${story.story_name}</a><br>`;
        });
    }
    us_c.innerHTML = inner;
    console.log('chara stories loaded.');
}

function loadunitStoryDragon(json) {
    var inner = '';
    for (var key in json) {
        inner += `<span>${json[key].dragon_name}</span><br>`
        json[key].content.forEach(story => {
            inner += `<a href="./stories/view.html?type=unitstory_dragon&id=${story.story_id}">${story.story_name}</a><br>`;
        });
    }
    us_d.innerHTML = inner;
    console.log('dragon stories loaded.');
}