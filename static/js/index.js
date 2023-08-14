
const dropmenu = document.querySelector('.drop-menu');
const dropcontent = document.querySelector('.dropdown-content');

let isMouseOverMenu = false;
let isMouseOverContent = false;

dropmenu.addEventListener('mouseenter', () => {
    isMouseOverMenu = true;
    dropcontent.style.display = 'flex';
});

dropmenu.addEventListener('mouseleave', () => {
    isMouseOverMenu = false;
    setTimeout(hideContentIfNotOver, 100);
});

dropcontent.addEventListener('mouseenter', () => {
    isMouseOverContent = true;
});

dropcontent.addEventListener('mouseleave', () => {
    isMouseOverContent = false;
    setTimeout(hideContentIfNotOver, 100);
});

function hideContentIfNotOver() {
    if (!isMouseOverMenu && !isMouseOverContent) {
        dropcontent.style.display = 'none';
    }
}

dropcontent.style.width = getComputedStyle(dropmenu).width;
const dropmenu_height = getComputedStyle(dropmenu).height;
const newHeight = parseFloat(dropmenu_height) * 0.8;

const allcontent = dropcontent.querySelectorAll('a');

allcontent.forEach(element => {
    element.style.height = `${newHeight}px`;
});
