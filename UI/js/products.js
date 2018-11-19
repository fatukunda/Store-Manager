import { modifyDiv, createItem, getSingleItem, editItem, deleteItem, fetchAllItems} from './helpers.js'

let url = 'https://store-manager-api-heroku.herokuapp.com/api/v1/products'

const productsCard = document.getElementById('products-card');
const salesCard = document.getElementById('sales-card');
const adminProductsList = document.getElementById('admin-products-list');
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
const editProductDetailsView = document.getElementById('edit-product-details-view');
const backProductDetailBtn = document.getElementById('back-product-detail');

const addProductForm = document.getElementById('add-product-form');

const createProduct = (number, product_id, name, category, price, quantity) => {
    const tableBody = document.getElementById('prod-details')
    const tr = document.createElement('tr')

    const idTd = document.createElement('td')
    const prodIdTd = document.createElement('td')
    const nameTd = document.createElement('td')
    const categoryTd = document.createElement('td')
    const quantityTd = document.createElement('td')
    const priceTd = document.createElement('td')
    const detailsTd = document.createElement('td')
    
    const viewDetailsBtn = document.createElement('button')
    viewDetailsBtn.classList.add('view-product-details-btn')
    viewDetailsBtn.innerHTML = 'View Product Details'
    viewDetailsBtn.addEventListener('click', (event) => {
        event.preventDefault();
        createProductDetailsView(name, product_id, category, quantity, price);
        modifyDiv(productDetailsView);
    })
    
    idTd.innerHTML = number
    prodIdTd.innerHTML = product_id
    nameTd.innerHTML = name
    categoryTd.innerHTML = category
    quantityTd.innerHTML = quantity
    priceTd.innerHTML = price

    detailsTd.appendChild(viewDetailsBtn)

    tr.appendChild(idTd)
    tr.appendChild(prodIdTd)
    tr.appendChild(nameTd)
    tr.appendChild(quantityTd)
    tr.appendChild(priceTd)
    tr.appendChild(categoryTd)
    tr.appendChild(detailsTd)
    

    tableBody.appendChild(tr)
}
const editForm = document.getElementById('edit-product-form');
editForm.addEventListener('submit', (event) => {
    event.preventDefault();
    getFormData()
})

const getFormData = () => {
    const idField = document.getElementById('id-field')
    const id = parseInt(idField.value);
    const quantityField = document.getElementById('quantity-field')
    const quantity = parseInt(quantityField.value);
    const priceField =document.getElementById('price-field')
    const price = parseFloat(priceField.value);
    updateSingleProduct(id, quantity, price);
    modifyDiv(adminProductsList)

}
const fillProductForm = (productId, name, category, quantity, price) => {
    const idField = document.getElementById('id-field');
    idField.value = productId
    const nameField = document.getElementById('name-field');
    nameField.value = name
    let categoryField = document.getElementById('select-category');
    categoryField = categoryField.options[categoryField.selectedIndex];
    categoryField.text = category
    const quantityField = document.getElementById('quantity-field')
    quantityField.value = quantity
    const priceField =document.getElementById('price-field')
    priceField.value = price
}
const deleteSingleProduct = (productId) => {
    url += `/${productId}`
    deleteItem(url)
        .then(data => data)
        .catch(error => console.log(error))
}

const updateSingleProduct = (productId, quantity, unitPrice) => {
    url += `/${productId}`
    const data = {
        quantity: quantity,
        unit_price: unitPrice
    }
    editItem(url, data)
        .then(data => data)
        .catch(error => console.log(error))
}

const getAllProducts = () => {
    fetchAllItems(url)
        .then((data) => {
            const products = data
            products.forEach((product, index) => {
                createProduct(index+1, product.product_id, product.name, product.category, product.unit_price, product.quantity)
            })
        })
        .catch(error => console.log(error))
}
const saveProduct = () => {
    // Get the user input from the form and save the product details into the database
    const name = document.getElementById('prod-name').value;
    const category = document.getElementById('prod-category');
    category = category.options[category.selectedIndex].text;
    const quantity = parseInt(document.getElementById('prod-quantity').value);
    const unit_price = parseFloat(document.getElementById('prod-price').value);

    addNewProduct(name, category, unit_price, quantity)
}

const addNewProduct = (name, category, unit_price, quantity) => {
    // Post the product details to the products endpoint
    const data = {
        name: name,
        category: category,
        quantity: quantity,
        unit_price: unit_price
    }
    createItem(url, data)
        .then(data => data)
        .catch(error => console.log(error))
}

const clearTextFields = () => {
    document.getElementById('prod-name').value = ''
    document.getElementById('prod-quantity').value = ''
    document.getElementById('prod-price').value = '';
}

const createProductDetailsView = (productName, product_id, category, quantity, unitPrice) => {
    // Get the product details div
    const mainView = document.getElementById('product-details-view')
    const title = document.createElement('h4');
    title.innerHTML = productName
    mainView.appendChild(title)
    const detailsColumn = document.createElement('div');
    detailsColumn.classList.add('details-right-column')

    const prodIdElement = document.createElement('h3');
    prodIdElement.innerHTML = 'Product ID: ' + product_id;
    detailsColumn.appendChild(prodIdElement)

    const categoryElement = document.createElement('h3');
    categoryElement.innerHTML = 'Category: ' + category;
    detailsColumn.appendChild(categoryElement)

    const quantityElement = document.createElement('h3')
    quantityElement.innerHTML = 'Quantity in stock: ' + quantity;
    detailsColumn.appendChild(quantityElement)

    const priceElement = document.createElement('h3')
    priceElement.innerHTML = 'Unit price: ' + unitPrice;
    detailsColumn.appendChild(priceElement)

    const buttonsDiv = document.createElement('div');

    const backBtn = document.createElement('button');
    backBtn.id = 'back'
    backBtn.innerHTML = '<< Back'
    backBtn.addEventListener('click', (event) => {
        event.preventDefault()
        modifyDiv(adminProductsList);
    });
    buttonsDiv.appendChild(backBtn)

    const editBtn = document.createElement('button');
    editBtn.id = 'edit'
    editBtn.innerHTML = 'Edit product';
    editBtn.addEventListener('click', (event) => {
        event.preventDefault()
        modifyDiv(editProductDetailsView)
        fillProductForm(product_id, productName, category, quantity, unitPrice)
    });
    buttonsDiv.appendChild(editBtn)

    const deleteBtn = document.createElement('button');
    deleteBtn.id = 'delete'
    deleteBtn.innerHTML = 'Delete product'
    deleteBtn.addEventListener('click', (event) => {
        event.preventDefault();
        const response = confirm('Are you sure you want to delete this Item?');
        if (response){
            deleteSingleProduct(product_id);
            getAllProducts()
            modifyDiv(adminProductsList);
        }
    });
    buttonsDiv.appendChild(deleteBtn)

    detailsColumn.appendChild(buttonsDiv)
    mainView.appendChild(detailsColumn)

}

addProductForm.addEventListener('submit', (event) => {
    // When the form is submitted, Save the product to the database
    event.preventDefault()
    saveProduct();
    alert('Product saved')
    clearTextFields()

});

//Show admin products list when the page loads
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
backProductDetailBtn.addEventListener('click', (event) => {
    event.preventDefault();
    modifyDiv(productDetailsView)
});
