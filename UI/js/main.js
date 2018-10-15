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
const addToCartButton = document.getElementById('add-to-cart-btn');
const cartBody = document.getElementById('cart-body');

//Fill the sell product form when the sell button is clicked

for(i = 0; i<sellBtns.length; i++){
    sellBtns[i].addEventListener('click', (event) => {
        let clickedBtn = event.target;
        let priceElement = clickedBtn.parentElement.previousElementSibling;
        let productNameElement = priceElement.previousElementSibling.previousElementSibling;
        let unitPrice = document.getElementById('unit-price');
        let productName = document.getElementById('product');
        unitPrice.value = parseFloat(priceElement.innerText);
        productName.value = productNameElement.innerText; 
    })
}
addToCartButton.addEventListener('click', (event) => {
    event.preventDefault();
    const productTable = document.getElementById('product-table')
    const item = document.getElementById('product').value;
    const unitPrice = document.getElementById('unit-price').value;
    const tableRow = document.createElement('tr');
    const tableDataItem = document.createElement('td');
    const tableDataPrice = document.createElement('td');
    const tableDataQuantity = document.createElement('td');
    const productQuantity = document.getElementById('product-quantity');

    //Item table data
    tableDataItem.innerText = item
    tableRow.appendChild(tableDataItem);
    //Quantity table data
    tableDataQuantity.innerText = parseInt(productQuantity.value);
    tableRow.appendChild(tableDataQuantity);
    //Unit price table data
    tableDataPrice.innerText = parseFloat(unitPrice) * tableDataQuantity.innerText;
    tableDataPrice.className += 'priceTd';
    tableRow.appendChild(tableDataPrice);
    // Append the product row to the table

    productTable.appendChild(tableRow);
    calculateTotal()
});

const calculateTotal = () => {
    const numberOfItems = document.getElementsByClassName('priceTd');
    const totalTableData = document.getElementById('total');
    let total = 0;
    for(let i =0; i <numberOfItems.length; i++){
        total += parseFloat(numberOfItems[i].innerText);
    }
    totalTableData.innerText = 'UGX. '+ total;
}

// for(i =0; i<sellBtns.length; i++){
//     sellBtns[i].addEventListener('click', (event) => {
//         clickedBtn = event.target;
//         hide(categorizeRow);
//         show(quantityRow);
//     });
// }



