import { fetchAllItems, modifyDiv } from './helpers.js'

const attendantsUrl ='https://store-manager-api-heroku.herokuapp.com/api/v1/attendants';
const salesUrl = 'https://store-manager-api-heroku.herokuapp.com/api/v1/sales';
const viewSales = document.getElementById('view-sales');
const viewSalesLink = document.getElementById('view-sales-link')
const sortSalesForm = document.getElementById('sort-sales-form');
const salesCard = document.getElementById('sales-card');
const salesBody = document.getElementById('sales-body');

const attendants = [];

const selectName = document.createElement('select');

const createSalesTable = (number, date, salesPerson, product, quantity, totalPrice) => {
    // create the sales table row structure for each sale in the database.
    const tr = document.createElement('tr');

    const idTd = document.createElement('td');
    idTd.innerHTML = number
    const dateTd = document.createElement('td')
    dateTd.innerHTML = date
    const nameTd = document.createElement('td');
    nameTd.innerHTML = salesPerson
    const productTd = document.createElement('td')
    productTd.innerHTML = product
    const quantityTd = document.createElement('td')
    quantityTd.innerHTML = quantity
    const totalPriceTd = document.createElement('td')
    totalPriceTd.innerHTML = totalPrice

    tr.appendChild(idTd)
    tr.appendChild(dateTd)
    tr.appendChild(nameTd)
    tr.appendChild(productTd)
    tr.appendChild(quantityTd)
    tr.appendChild(totalPriceTd)

    salesBody.appendChild(tr)

}

const getSales = () => {
    fetchAllItems(salesUrl)
        .then((data) => {
            const sales = data
            sales.map((sale, index) => {
                createSalesTable(index +1, sale.sale_date, sale.sales_person,
                     sale.product_sold, sale.quantity_sold, sale.total_price)
            })
        })
}

const fetchAttendantsFirstName = (firstName) => {
     const option = document.createElement('option')
     option.text = firstName
     return option

}
const getAttendants = () => {
    // Fetch the attendants first names and populate them within a drop down field
    //This will help the administrator to sort the sales by a specific attendant
    fetchAllItems(attendantsUrl)
        .then((data) => {
            data.map((attendant) => {
                attendants.push(attendant)
                const optionNode = fetchAttendantsFirstName(attendant.first_name)
                selectName.appendChild(optionNode)
            })
            const saveButton = document.createElement('button')
            saveButton.innerHTML = 'Save'
            sortSalesForm.appendChild(selectName)
            sortSalesForm.appendChild(saveButton)
            
        })
        .catch(error => console.log(error))
}

viewSalesLink.addEventListener('click', (event) => {
    getAttendants();
    getSales()
    modifyDiv(viewSales)
    
})
salesCard.addEventListener('click', () => {
    getAttendants();
    getSales()
    modifyDiv(viewSales)

})