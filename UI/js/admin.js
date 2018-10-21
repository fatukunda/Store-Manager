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