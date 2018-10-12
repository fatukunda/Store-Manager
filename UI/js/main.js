//Show element
const show = (elem) => {
    elem.style.display = 'block';
}

//Hide element
const hide = (elem) => {
    elem.style.display = 'none';
}
//Toggle element visibility
const toggle = (elem) => {
    if(window.getComputedStyle(elem).display === 'block'){
        hide(elem);
        return;
    }
    show(elem);
}
const sellBtn = document.getElementsByClassName('sell')[0];
const categorizeBtn = document.getElementsByClassName('categorize')[0];
let categorizeRow = document.getElementsByClassName('toggle-categorize')[0];
let quantityRow = document.getElementsByClassName('toggle-sell')[0];
console.log(sellBtn, categorizeBtn);

sellBtn.addEventListener('click', () => {
    hide(categorizeRow);
    toggle(quantityRow);
});

categorizeBtn.addEventListener('click', () => {
    hide(quantityRow);
    toggle(categorizeRow);
})


