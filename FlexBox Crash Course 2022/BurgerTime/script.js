// Add all the objects we'll need to manipulate
const hamburger = document.querySelector('.hamburger');
const logo = document.querySelector('.logo');
const navs = document.querySelector('.nav');
const navUl = document.querySelector('.navbar ul');
const navContainer = document.querySelector('.navbar .container');
const headerContainer = document.querySelector('.header .container');
const boxesContainer = document.querySelectorAll('.boxes .container');

// Create functions that set for phone and tablet
function setToPhone(){
    headerContainer.style.flexDirection = "column";
    headerContainer.style.paddingTop = "20px";
    headerContainer.style.textAlign = "center";
    for ( let i = 0; i < boxesContainer.length; i++ ){
        boxesContainer[i].style.display = "block";
        boxesContainer[i].style.textAlign = "center";
    }
    navUl.style.display = "none";
    hamburger.style.display = "flex";
}

function setToDesktop(){
    headerContainer.style.flexDirection = "row";
    headerContainer.style.justifyContent = "space-between";
    headerContainer.style.alignItems = "center"; 
    for ( let i = 0; i < boxesContainer.length; i++ ){
        boxesContainer[i].style.display = "flex";
        boxesContainer[i].style.textAlign = "";
    }
    navUl.style.display = "flex";
    hamburger.style.display = "none";
}

// Create a condition that targets viewports at least 768px wide
const mediaQuery = window.matchMedia('(max-width: 768px)');
function handleChanges(e) {
  if (e.matches) {
    console.log('Screen less than 768px');
    setToPhone();
  } else {
    console.log('Screen more than 768px');
    setToDesktop();
  }
}

// Register event listeners (don't fire initially)
mediaQuery.addListener(handleChanges); 
hamburger.addEventListener('click', () => {
    if( hamburger.innerHTML.includes('bars') ){
        hamburger.innerHTML = '<i class="fas fa-times"></i>';
        hamburger.style.marginLeft = "20px";
        logo.style.display = "none";
        navs.style.display = "flex";
        navContainer.style.justifyContent = "flex-end";
    } else {
        hamburger.innerHTML = '<i class="fas fa-bars"></i>';
        logo.style.display = "block";
        navs.style.display = "none";
        navContainer.style.justifyContent = "space-between";
    }
});
handleChanges(mediaQuery); // Initial check