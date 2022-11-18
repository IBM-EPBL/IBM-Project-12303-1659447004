let bgColor =  "#1abc9c";
let fontColor = "#fff";
let logo = document.getElementsByTagName('svg')[0];
let signin = document.getElementById('signin');
let signup = document.getElementById('signup');
let logo_heading = document.getElementById('logo_heading');
let left_container = document.querySelector('.left');
let right_container = document.querySelector('.right');
let main_left_content = document.querySelector('.left_invisible');
let main_right_content = document.querySelector('.signup');
let right_content = document.querySelector('.right_invisible');
let left_content = document.querySelector('.signin');
//sign in container go to invisible
signin.addEventListener('click',()=>{
    left_container.style.backgroundColor = fontColor;
    right_container.style.backgroundColor = bgColor;
    logo.style.fill = bgColor;
    logo_heading.style.color = bgColor;
    main_right_content.style.display = "none";
    main_left_content.style.display = "none";
    right_content.style.display = "block";
    left_content.style.display = "inline-flex";
})
//sign up container go to invisible
signup.addEventListener('click',()=>{
    left_container.style.backgroundColor = "";
    left_container.style.width = "";
    right_container.style.backgroundColor = "";
    logo.style.fill = "";
    logo_heading.style.color = "";
    main_right_content.style.display = "";
    main_left_content.style.display = "";
    right_content.style.display = "";
    left_content.style.display = "";
})