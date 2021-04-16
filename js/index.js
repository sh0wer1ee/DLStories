var article = document.getElementById("story");

fetch(`./stories/unitstory_chara/110385011.json`)
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
                inner += '<div id="speaker_icon"><img src="https://gitee.com/sh0wer1ee/dlicons/raw/master/icons/dragon/s/210128_01.png"/></div>'; //MISSING
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
        console.log('rua');
    });