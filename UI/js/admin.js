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
const showDetailsBtn = document.getElementById('show-details-btn');
const deleteBtn = document.getElementById('delete');
const backBtn = document.getElementById('back');
const editBtn = document.getElementById('edit');
const editProductDetailsView = document.getElementById('edit-product-details-view');
const saveEditBtn = document.getElementById('save-edited-product');
const backProductDetailBtn = document.getElementById('back-product-detail');
const attendantsList = document.getElementById('attendants-list');
const attendantsCard = document.getElementById('attendants-card')
//Hide admin products list when the page loads
window.addEventListener('load', () => {
    show(adminProductsList);
    hide(addProduct);
    hide(viewSales);
    hide(addCategory);
    hide(addSalesPerson);
    hide(productDetailsView);
    hide(editProductDetailsView);
    hide(editProductDetailsView);
    hide(attendantsList);

});
//Toggle admin products when the products card is clicked on
productsCard.addEventListener('click', () => {
    show(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(viewSales);
    hide(addSalesPerson);
    hide(editProductDetailsView);
    hide(attendantsList);
});
salesCard.addEventListener('click', () => {
    show(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(addSalesPerson);
    hide(editProductDetailsView);
    hide(attendantsList);
})
addProductLink.addEventListener('click', () => {
    hide(adminProductsList);
    hide(addCategory);
    show(addProduct);
    hide(viewSales);
    hide(addSalesPerson);
    hide(productDetailsView);
    hide(editProductDetailsView);
    hide(attendantsList);
});
addCategoryLink.addEventListener('click', () => {
    show(addCategory);
    hide(adminProductsList);
    hide(addProduct);
    hide(viewSales);
    hide(addSalesPerson);
    hide(productDetailsView);
    hide(editProductDetailsView);
    hide(attendantsList);
})
viewProducts.addEventListener('click', () => {
    hide(addProduct);
    show(adminProductsList);
    hide(addCategory);
    hide(viewSales);
    hide(addSalesPerson);
    hide(productDetailsView);
    hide(editProductDetailsView);
    hide(attendantsList);
});
viewSalesLink.addEventListener('click', () => {
    show(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(addSalesPerson);
    hide(productDetailsView);
    hide(editProductDetailsView);
    hide(attendantsList);
});
addSalesPersonLink.addEventListener('click', () => {
    show(addSalesPerson);
    hide(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(productDetailsView);
    hide(editProductDetailsView);
    hide(attendantsList);
});
showDetailsBtn.addEventListener('click', () => {
    show(productDetailsView);
    hide(adminProductsList);
    hide(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(editProductDetailsView);
    hide(attendantsList);
});
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
    show(editProductDetailsView)
    hide(adminProductsList);
    hide(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(productDetailsView);
    hide(attendantsList);
});
saveEditBtn.addEventListener('click', (event) => {
    event.preventDefault();
    show(productDetailsView);
    hide(editProductDetailsView)
    hide(adminProductsList);
    hide(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(attendantsList);
});
backProductDetailBtn.addEventListener('click', (event) => {
    event.preventDefault();
    show(productDetailsView);
    hide(editProductDetailsView)
    hide(adminProductsList);
    hide(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(attendantsList);
});
attendantsCard.addEventListener('click', () => {
    show(attendantsList);
    hide(productDetailsView);
    hide(editProductDetailsView)
    hide(adminProductsList);
    hide(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(addSalesPerson);
})