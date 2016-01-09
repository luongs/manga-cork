/* Functions to set and modfiy local storage */

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

/* Function to show and hide modal */


function show_login_form()
{
    var login_form = document.getElementById('login_form');
    dialogPolyfill.registerDialog(login_form);
    login_form.showModal();
}

function clicked_in_login_form(mouseEvent) {

    var login_form = document.getElementById('login_form');
    var rect = login_form.getBoundingClientRect();
    return rect.top <= mouseEvent.clientY && mouseEvent.clientY <= rect.top +
        rect.height && rect.left <= mouseEvent.clientX && mouseEvent.clientX
        <= rect.left + rect.width;
}

function hide_login_form()
{
    var login_form = document.getElementById('login_form');
    if (login_form.open)
            login_form.close();
}

function show_signup_form()
{
    var login_form = document.getElementById('login_form');
    var signup_form = document.getElementById('signup_form');
    if (login_form.open)
            login_form.close();
    dialogPolyfill.registerDialog(signup_form);
    signup_form.showModal();
}

function hide_signup_form()
{
    var signup_form = document.getElementById('signup_form');
    if (signup_form.open)
        signup_form.close();
}

function clicked_in_signup_form(mouseEvent) {

    var signup_form = document.getElementById('signup_form');
    var rect = signup_form.getBoundingClientRect();
    return rect.top <= mouseEvent.clientY && mouseEvent.clientY <= rect.top +
        rect.height && rect.left <= mouseEvent.clientX && mouseEvent.clientX
        <= rect.left + rect.width;
}

function check_click_location_login(e) {
    if (clicked_in_login_form(e))
        return;
    hide_login_form();
}

function check_click_location_signup(e) {
    if (clicked_in_signup_form(e))
        return;
    hide_signup_form();
}

/* END OF FUNCTIONS */

if (!localStorage.getItem('show_post_text') &&
                !localStorage.getItem('show_comments')){

        localStorage.setItem('show_post_text', 'visible');
        localStorage.setItem('show_comments', 'visible');
}

document.addEventListener("DOMContentLoaded", checkHidden, false);
