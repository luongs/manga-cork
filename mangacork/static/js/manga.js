
if (!localStorage.getItem('show_post_text') && 
                !localStorage.getItem('show_comments')){

        localStorage.setItem('show_post_text', 'hidden');
        localStorage.setItem('show_comments', 'hidden');
}

document.addEventListener("DOMContentLoaded", checkHidden, false);

function checkHidden(e) 
{
        if (localStorage.getItem('show_post_text') == 'hidden'){
                hide_post_section();
        }

        if (localStorage.getItem('show_comments') == 'hidden')
        {
                hide_comments();
        }
}
function toggle_post()
{
        if (localStorage.getItem('show_post_text') == 'hidden'){
                localStorage.setItem('show_post_text', 'visible');
                show_post_section();
        }
        else
        {
                localStorage.setItem('show_post_text', 'hidden');
                hide_post_section();
        }
}

function toggle_comments()
{
        if (localStorage.getItem('show_comments') == 'hidden')
        {
                localStorage.setItem('show_comments', 'visible');
                show_comments();
        }
        else
        {
                localStorage.setItem('show_comments', 'hidden');
                hide_comments(); 
        }
}

function hide_post_section()
{
        document.getElementById('post_section').style.display = 'none';
}

function hide_comments()
{
        document.getElementById('comment_section').style.display = 'none';
}

function show_post_section()
{
        document.getElementById('post_section').style.display = 'block';
}

function show_comments()
{
        document.getElementById('comment_section').style.display = 'block';
}
