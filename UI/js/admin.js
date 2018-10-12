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
const adminProductsList = document.getElementsByClassName('admin-products-list')[0];
//Hide admin products list when the page loads
window.addEventListener('load', () => {
    hide(adminProductsList);
});
//Toggle admin products when the products card is clicked on
productsCard.addEventListener('click', () => {
    toggle(adminProductsList);
});
