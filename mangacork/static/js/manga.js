
if (!localStorage.getItem('show_post_text') && 
                !localStorage.getItem('show_comments')){

        localStorage.setItem('show_post_text', 'hidden');
        localStorage.setItem('show_comments', 'hidden');
}

function toggle_post()
{
        if (localStorage.getItem('show_post_text') == 'hidden')
                localStorage.setItem('show_post_text', 'visible');
        else
                localStorage.setItem('show_post_text', 'hidden');
    alert("post local storage "+localStorage.getItem('show_post_text'));
}

function toggle_comments()
{
    if (localStorage.getItem('show_comments') == 'hidden')
                localStorage.setItem('show_comments', 'visible');
        else
                localStorage.setItem('show_comments', 'hidden');
    alert("comments local storage "+localStorage.getItem('show_comments'));
}

function hide_comments()
{
    localStorage.setItem('show_comments', 'hide');
}

function hide_post()
{
    localStorage.setItem('show_post', 'hide');
}

