const menuIcon = document.getElementById('menu-icon');
const navMenu = document.querySelector('.nav-menu');

menuIcon.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    menuIcon.classList.toggle('bx-menu');
    menuIcon.classList.toggle('bx-x');
});