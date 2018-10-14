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
//Hide admin products list when the page loads
window.addEventListener('load', () => {
    show(adminProductsList);
    hide(addProduct);
    hide(viewSales);
    hide(addCategory);

});
//Toggle admin products when the products card is clicked on
productsCard.addEventListener('click', () => {
    show(adminProductsList);
    hide(addCategory);
    hide(addProduct);
    hide(viewSales);
});
salesCard.addEventListener('click', () => {
    show(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
})
addProductLink.addEventListener('click', () => {
    hide(adminProductsList);
    hide(addCategory);
    show(addProduct);
    hide(viewSales);
});
addCategoryLink.addEventListener('click', () => {
    show(addCategory);
    hide(adminProductsList);
    hide(addProduct);
    hide(viewSales);
})
viewProducts.addEventListener('click', () => {
    hide(addProduct);
    show(adminProductsList);
    hide(addCategory);
    hide(viewSales);
});
viewSalesLink.addEventListener('click', () => {
    show(viewSales);
    hide(adminProductsList);
    hide(addCategory);
    hide(addProduct);
})
