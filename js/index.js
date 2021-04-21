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

var cs = document.getElementById("castlestory-div");
var qs_e = document.getElementById("queststory_event-div");
var qs_m = document.getElementById("queststory_main-div");
var us_c = document.getElementById("unitstory_chara-div");
var us_d = document.getElementById("unitstory_dragon-div");

lastCommit();
loadIndexJson();

function lastCommit() {
    fetch('https://gitee.com/api/v5/repos/sh0wer1ee/dlstories/commits')
        .then(function(response) {
            if (!response.ok) {
                throw Error(response.statusText);
            }
            return response;
        })
        .then(response => response.json())
        .then(json => {
            latestTime = json[0].commit.author.date;
            var d = new Date(latestTime);
            var datestring = (d.getFullYear() + '/' + ('0' + (d.getMonth() + 1)).slice(-2) + '/' +
                ('0' + d.getDate()).slice(-2) + ' ' + ('0' + d.getHours()).slice(-2) + ':' + ('0' + d.getMinutes()).slice(-2));
            document.getElementById("update-time").innerText = `最近更新：${datestring}`;
        }).catch(function(error) {
            console.log(error);
            document.getElementById("update-time").innerText = `最近更新：N/A`;
        });
}

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
        inner += `<div class="castlestory-items">`;
        inner += `<a href="./stories/view.html?type=castlestory&id=${key}">`;
        inner += `<img src="./icons/castlestory/${key}.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = './icons/DummyIcon.png';"/>`;
        inner += `<span>${json[key].story_name}</span></a>`;
        inner += '</div>';
    }
    cs.innerHTML = inner;
    $("#cs-search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".castlestory-items").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    console.log('castle stories loaded.');
}

function loadQuestStoryEvent(json) {
    var inner = '';
    for (var key in json) {
        inner += '<div class="story-group">';
        inner += `<div id="story-group-questevent-icon"><img src="./icons/queststory_event/${key}.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = './icons/DummyIcon.png';"/></div>`;
        inner += `<div id="story-group-name">${json[key].event_name}</div>`;
        inner += '<div id="story-group-items">';
        json[key].content.forEach(story => {
            if (story.story_id.charAt(5) != '3' && story.story_id.charAt(5) != '5') {
                inner += `<a href="./stories/view.html?type=queststory_event&id=${story.story_id}">${story.episode} ${story.story_name}</a><br>`;
            }
        });
        inner += '</div></div>';
    }
    qs_e.innerHTML = inner;
    $("#qs_e-search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".story-group").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    console.log('event stories loaded.');
}

function loadQuestStoryMain(json) {
    var inner = '';
    for (var key in json) {
        inner += '<div class="story-group">';
        inner += `<div id="story-group-questmain-icon"><img src="./icons/queststory_main/${key}.png" onerror="if (this.src != './icons/DummyIcon.png') this.src = './icons/DummyIcon.png';"/></div>`;
        inner += `<div id="story-group-name">${json[key].chapter_name}</div>`;
        inner += '<div id="story-group-items">';
        json[key].content.forEach(story => {
            if (story.story_name) {
                inner += `<a href="./stories/view.html?type=queststory_main&id=${story.story_id}">${story.title} ${story.story_name}</a><br>`;
            } else {
                inner += `<a href="./stories/view.html?type=queststory_main&id=${story.story_id}">${story.story_id}</a><br>`;
            }
        });
        inner += '</div></div>';
    }
    qs_m.innerHTML = inner;
    $("#qs_m-search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".story-group").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    console.log('main stories loaded.');
}

function loadUnitStoryChara(json) {
    var inner = '';
    for (var key in json) {
        inner += '<div class="story-group">';
        inner += `<div id="story-group-unit-icon"><img src="https://gitee.com/sh0wer1ee/dlicons/raw/master/icons/chara/l/${key.substring(0,6)}_${key.substring(6)}_r05.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/></div>`;
        inner += `<div id="story-group-name">${json[key].chara_name}</div>`;
        inner += '<div id="story-group-items">';
        json[key].content.forEach(story => {
            inner += `<a href="./stories/view.html?type=unitstory_chara&id=${story.story_id}">${story.episode} ${story.story_name}</a><br>`;
        });
        inner += '</div></div>';
    }
    us_c.innerHTML = inner;
    $("#us_c-search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".story-group").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    console.log('chara stories loaded.');
}

function loadunitStoryDragon(json) {
    var inner = '';
    for (var key in json) {
        inner += '<div class="story-group">';
        inner += `<div id="story-group-unit-icon"><img src="https://gitee.com/sh0wer1ee/dlicons/raw/master/icons/dragon/l/${key.substring(0,6)}_${key.substring(6)}.png" onerror="if (this.src != '../icons/DummyIcon.png') this.src = '../icons/DummyIcon.png';"/></div>`;
        inner += `<div id="story-group-name">${json[key].dragon_name}</div>`;
        inner += '<div id="story-group-items">';
        json[key].content.forEach(story => {
            inner += `<a href="./stories/view.html?type=unitstory_dragon&id=${story.story_id}">${story.story_name}</a><br>`;
        });
        inner += '</div></div>';
    }
    us_d.innerHTML = inner;
    $("#us_d-search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $(".story-group").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
    console.log('dragon stories loaded.');
}