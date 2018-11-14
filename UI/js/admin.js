//Show element
const show = (elem) => {
    elem.style.display = 'block';
}

//Hide element
const hide = (elem) => {
    elem.style.display = 'none';
}
//Toggle element visibility
// const toggle = (elem) => {
//     if(window.getComputedStyle(elem).display === 'block'){
//         hide(elem);
//         return;
//     }
//     show(elem);
// }

const createProduct = (number, name, category, price, quantity) => {
    tableBody = document.getElementById('prod-details')
    tr = document.createElement('tr')

    idTd = document.createElement('td')
    nameTd = document.createElement('td')
    categoryTd = document.createElement('td')
    quantityTd = document.createElement('td')
    priceTd = document.createElement('td')
    detailsTd = document.createElement('td')
    
    viewDetailsBtn = document.createElement('button')
    viewDetailsBtn.classList.add('view-product-details-btn')
    viewDetailsBtn.innerHTML = 'View Product Details'
    
    idTd.innerHTML = number
    nameTd.innerHTML = name
    categoryTd.innerHTML = category
    quantityTd.innerHTML = quantity
    priceTd.innerHTML = price

    detailsTd.appendChild(viewDetailsBtn)

    tr.appendChild(idTd)
    tr.appendChild(nameTd)
    tr.appendChild(quantityTd)
    tr.appendChild(priceTd)
    tr.appendChild(categoryTd)
    tr.appendChild(detailsTd)
    

    tableBody.appendChild(tr)
}

const getAllProducts = () => {
    const url = 'https://store-manager-api-heroku.herokuapp.com/api/v1/products'
    const config = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + window.sessionStorage.getItem('token')
        }
    }
    fetch(url, config)
        .then((res) => res.json())
        .then((data) => {
            products = data
            products.forEach((product, index) => {
                createProduct(index+1, product.name, product.category, product.unit_price, product.quantity)
            })
        })
        .catch((err) => console.log(err))
}


const productsCard = document.getElementById('products-card');
const salesCard = document.getElementById('sales-card');
const adminProductsList = document.getElementsByClassName('admin-products-list')[0];
const addCategory = document.getElementById('add-category');
const addProduct = document.getElementById('add-product');
const addProductLink = document.getElementById('add-product-link');
const addCategoryLink = document.getElementById('add-category-link');
const viewProducts = document.getElementById('view-products');
const viewSales = document.getElementById('view-sales');
const viewSalesLink = document.getElementById('view-sales-link')
const addSalesPersonLink = document.getElementById('add-sales-person-link');
const addSalesPerson = document.getElementById('add-sales-person');
const productDetailsView = document.getElementById('product-details-view');
const deleteBtn = document.getElementById('delete');
const backBtn = document.getElementById('back');
const editBtn = document.getElementById('edit');
const editProductDetailsView = document.getElementById('edit-product-details-view');
const saveEditBtn = document.getElementById('save-edited-product');
const backProductDetailBtn = document.getElementById('back-product-detail');
const attendantsList = document.getElementById('attendants-list');
const attendantsCard = document.getElementById('attendants-card')
const viewProductDetails = document.getElementsByClassName('view-product-details-btn');

const elements = [adminProductsList, addCategory, addProduct,viewSales, addSalesPerson,
     productDetailsView,editProductDetailsView, attendantsList, viewProductDetails ]
// Helper methods
const modifyDiv = (divToModify) => {
    elements.forEach((element) => {
        if (element === divToModify){
            show(element)
        }else{
            hide(element)
        }
    })
}

//Hide admin products list when the page loads
window.addEventListener('load', () => {
    getAllProducts()
    modifyDiv(adminProductsList)

});

productsCard.addEventListener('click', () => {
    modifyDiv(adminProductsList)
});
salesCard.addEventListener('click', () => {
    modifyDiv(viewSales)

})
addProductLink.addEventListener('click', () => {
    modifyDiv(addProduct)

});
addCategoryLink.addEventListener('click', () => {
    modifyDiv(addCategory);
})
viewProducts.addEventListener('click', () => {
    modifyDiv(adminProductsList)

});
viewSalesLink.addEventListener('click', () => {
    modifyDiv(viewSales)
});
addSalesPersonLink.addEventListener('click', () => {
    modifyDiv(addSalesPerson)
});
for(let i=0; i<viewProductDetails.length; i++){
    viewProductDetails[i].addEventListener('click', (event) => {
        modifyDiv(productDetailsView)
   
    })
}

backBtn.addEventListener('click', () => {
    show(adminProductsList);
    hide(productDetailsView);
});
deleteBtn.addEventListener('click', () => {
    response = confirm('Are you sure you want to delete this Item?');
    if (response){
        hide(productDetailsView);
        show(adminProductsList);
    }
});
editBtn.addEventListener('click', () => {
    modifyDiv(editProductDetailsView)
});
saveEditBtn.addEventListener('click', (event) => {
    event.preventDefault();
    modifyDiv(productDetailsView)
});
backProductDetailBtn.addEventListener('click', (event) => {
    event.preventDefault();
    modifyDiv(productDetailsView)
});
attendantsCard.addEventListener('click', () => {
    modifyDiv(attendantsList)
})