const adminProductsList = document.getElementById('admin-products-list');
const addCategory = document.getElementById('add-category');
const addProduct = document.getElementById('add-product');
const viewSales = document.getElementById('view-sales');
const addSalesPerson = document.getElementById('add-sales-person');
const productDetailsView = document.getElementById('product-details-view');
const editProductDetailsView = document.getElementById('edit-product-details-view');
const attendantsList = document.getElementById('attendants-list');
const attendantDetails = document.getElementById('attendant-details');

//Show element
const show = (elem) => {
    elem.style.display = 'block';
}

//Hide element
const hide = (elem) => {
    elem.style.display = 'none';
}

const elements = [adminProductsList, attendantDetails, addCategory, addProduct,viewSales, addSalesPerson,
    productDetailsView,editProductDetailsView, attendantsList]

const modifyDiv = (divToModify) => {
    elements.forEach((element) => {
        if (element === divToModify){
            show(element)
        }else{
            hide(element)
        }
    })
}

const postConfig = (data) => {
    const config = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + window.sessionStorage.getItem('token')
        }
    }
    return config;
}
const getConfig = () => {
    const config = {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + window.sessionStorage.getItem('token')
        }
    }
    return config
}

const putConfig = (data) => {
    const config = {
        method: 'PUT',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + window.sessionStorage.getItem('token')
        }
    }
    return config;
}
const deleteConfig = () => {
    const config = {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + window.sessionStorage.getItem('token')
        }
    }
    return config
}
async function createItem(url, data) {
    const config = postConfig(data)
    let response = await fetch(url, config)
    let returnData = response.json();
    return returnData
}

async function fetchAllItems(url) {
    const config = getConfig();
    let response = await fetch(url, config);
    let data = response.json();
    return data
}

async function getSingleItem(url) {
    const config = getConfig()
    let response = await fetch(url, config);
    let data = response.json();
    return data
}
async function editItem(url, data) {
    const config = putConfig(data)
    let response = await fetch(url, config);
    let returnData = response.json();
    return returnData
}
async function deleteItem(url) {
    const config = deleteConfig()
    let response = await fetch(url, config);
    let data = response.json();
    return data
}

export { modifyDiv , createItem, getSingleItem, editItem, deleteItem, fetchAllItems }