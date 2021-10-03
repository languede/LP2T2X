const sign_in_button = document.querySelector('#sign-in-button');
const sign_up_button = document.querySelector('#sign-up-button');
const container = document.querySelector('.container');

sign_up_button.addEventListener('click', ()=>{
    container.classList.add('sign-up-mode');
});

sign_in_button.addEventListener('click', ()=>{
    container.classList.remove('sign-up-mode');
});
