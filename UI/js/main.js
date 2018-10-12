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
const sellBtns = document.getElementsByClassName('sell');
const categorizeBtn = document.getElementsByClassName('categorize')[0];
let categorizeRow = document.getElementsByClassName('toggle-categorize')[0];
let quantityRow = document.getElementsByClassName('toggle-sell')[0];
console.log(sellBtns, categorizeBtn);

for(i =0; i<sellBtns.length; i++){
    sellBtns[i].addEventListener('click', (event) => {
        clickedBtn = event.target;
        hide(clickedBtn.closest(categorizeRow));
        toggle(clickedBtn.closest(quantityRow));
    });
}
// sellBtns.forEach((btn) => {
//     btn.addEventListener('click', () => {
//         hide(categorizeRow);
//         toggle(quantityRow);
//     })
// })
// sellBtn.addEventListener('click', () => {
//     hide(categorizeRow);
//     toggle(quantityRow);
// });

categorizeBtn.addEventListener('click', () => {
    hide(quantityRow);
    toggle(categorizeRow);
})


