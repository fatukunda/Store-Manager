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
const addProductForm = document.getElementById('add-product-form');

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
    viewDetailsBtn.addEventListener('click', (event) => {
        event.preventDefault();
        createProductDetailsView(name,category, quantity, price);
        modifyDiv(productDetailsView);
    })
    
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
const saveProduct = () => {
    // Get the user input from the form and save the product details into the database
    name = document.getElementById('prod-name').value;
    category = document.getElementById('prod-category');
    category = category.options[category.selectedIndex].text;
    quantity = parseInt(document.getElementById('prod-quantity').value);
    unit_price = parseFloat(document.getElementById('prod-price').value);

    addNewProduct(name, category, unit_price, quantity)
}

const addNewProduct = (name, category, unit_price, quantity) => {
    // Post the product details to the products endpoint
    const url = 'https://store-manager-api-heroku.herokuapp.com/api/v1/products'
    const data = {
        name: name,
        category: category,
        quantity: quantity,
        unit_price: unit_price
    }
    const config = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + window.sessionStorage.getItem('token')
        }
    }
    fetch(url, config)
        .then((res) => res.json())
        .then((data) => JSON.stringify(data))
        .catch((err) => console.log(err))
}

const clearTextFields = () => {
    document.getElementById('prod-name').value = ''
    document.getElementById('prod-quantity').value = ''
    document.getElementById('prod-price').value = '';
}

const createProductDetailsView = (productName, category, quantity, unitPrice) => {
    // Get the product details div
    const mainView = document.getElementById('product-details-view')
    const title = document.createElement('h4');
    title.innerHTML = productName
    mainView.appendChild(title)
    const detailsColumn = document.createElement('div');
    detailsColumn.classList.add('details-right-column')

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
    });
    buttonsDiv.appendChild(editBtn)

    const deleteBtn = document.createElement('button');
    deleteBtn.id = 'delete'
    deleteBtn.innerHTML = 'Delete product'
    deleteBtn.addEventListener('click', (event) => {
        event.preventDefault();
        response = confirm('Are you sure you want to delete this Item?');
        if (response){
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
const saveEditBtn = document.getElementById('save-edited-product');
const backProductDetailBtn = document.getElementById('back-product-detail');
const attendantsList = document.getElementById('attendants-list');
const attendantsCard = document.getElementById('attendants-card')


const elements = [adminProductsList, addCategory, addProduct,viewSales, addSalesPerson,
     productDetailsView,editProductDetailsView, attendantsList]
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