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
const categorizeRow = document.getElementsByClassName('toggle-categorize')[0];
const quantityRow = document.getElementsByClassName('toggle-sell')[0];
const sellProductDiv =document.getElementById('sell-product');

//Fill the sell product form when the sell button is clicked

for(i = 0; i<sellBtns.length; i++){
    sellBtns[i].addEventListener('click', (event) => {
        let clickedBtn = event.target;
        let priceElement = clickedBtn.parentElement.previousElementSibling;
        let productNameElement = priceElement.previousElementSibling.previousElementSibling;
        let unitPrice = document.getElementById('unit-price');
        let productName = document.getElementById('product')
        unitPrice.value = parseFloat(priceElement.innerText);
        productName.value = productNameElement.innerText; 
    })
}

for(i =0; i<sellBtns.length; i++){
    sellBtns[i].addEventListener('click', (event) => {
        clickedBtn = event.target;
        hide(categorizeRow);
        show(quantityRow);
    });
}



