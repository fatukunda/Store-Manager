// attendants.js
import { modifyDiv, createItem, editItem, fetchAllItems } from './helpers.js'

const attendantsList = document.getElementById('attendants-list');
const attendantsCard = document.getElementById('attendants-card');
const attendantsForm = document.getElementById('add-attendant-form');
const attendantsNumber = document.getElementById('attendants-number');
const attendantDetails = document.getElementById('attendant-details');
const addSalesPersonLink = document.getElementById('add-sales-person-link');
const addSalesPerson = document.getElementById('add-sales-person');


const url = 'https://store-manager-api-heroku.herokuapp.com/api/v1/attendants';

const attendantsLayout = (firstName, email, role) => {
    const card = document.createElement('div');
    card.classList.add('card')
    card.style.width = '230px'
    card.style.float = 'left'
    card.style.margin = '5px'

    const cardHeader = document.createElement('div')
    cardHeader.classList.add('card-header')

    const cardMain = document.createElement('div')
    cardMain.classList.add('card-main')
    cardMain.style.color = '#00787a'

    const mainDescription = document.createElement('div')
    mainDescription.classList.add('main-description')

    const detailsButton = document.createElement('button');
    detailsButton.style.marginBottom = '10px';
    detailsButton.addEventListener('click', (event) => {
        event.preventDefault();

        modifyDiv(attendantDetails)
    })
    detailsButton.innerHTML = 'View Details';

    mainDescription.appendChild(detailsButton)
    const image = document.createElement('img');
    image.setAttribute('src', 'https://via.placeholder.com/200');
    cardHeader.appendChild(image)

    const name = document.createElement('h2');
    name.innerHTML = firstName
    const emailP = document.createElement('p');
    emailP.innerHTML = email;
    const userType = document.createElement('p');
    userType.innerHTML = role;

    cardMain.appendChild(name)
    cardMain.appendChild(emailP)
    cardMain.appendChild(userType)

    card.appendChild(cardHeader)
    card.appendChild(cardMain)
    card.appendChild(mainDescription)
    attendantsList.appendChild(card)

}
// Get all attendants from the api

const getAllAttendants = () => {
    fetchAllItems(url)
        .then((data) => {
            const attendants = data
            attendants.forEach((attendant) => {
                attendantsLayout(attendant.first_name, attendant.email, attendant.user_type)
            })
        })
        .catch(error => console.log(error))

}


// Make an attendant an Admin

const makeAdmin = (attendantId) => {
    url += `/${attendantId}`
    const data = {
        role: 'admin'
    }
    editItem(url, data)
        .then(data => data)
        .catch(error => console.log(error))
}
// Get form user data
const getFormUserData = () => {
    const firstName = document.getElementById('userFirstName').value;
    const lastName = document.getElementById('userLastName').value;
    const username = document.getElementById('userUsername').value;
    const email = document.getElementById('userEmail').value;
    const password = document.getElementById('userPassword').value;
    const data = {
        first_name: firstName,
        last_name: lastName,
        email: email, 
        username: username,
        password: password
    }
    createItem(url, data)
        .then(returnedData => console.log(returnedData))
        .catch(error => console.log(error))
}
const clearFormData = () => {
    document.getElementById('userFirstName').value = '';
    document.getElementById('userLastName').value = '';
    document.getElementById('userUsername').value = '';
    document.getElementById('userEmail').value = '';
    document.getElementById('userPassword').value = '';
}
// Display a list of attendants when the attendants card is clicked
attendantsCard.addEventListener('click', (event) => {
    event.preventDefault();
    getAllAttendants();
    modifyDiv(attendantsList)
});

// Create a new attendant
attendantsForm.addEventListener('submit', (event) => {
    event.preventDefault();
    getFormUserData();
    clearFormData();
})

const getNumberOfAttendants = () => {
    fetchAllItems(url)
        .then((data) => {
            attendantsNumber.innerHTML = data.length;
        })
        .catch(error => console.log(error))
}

addSalesPersonLink.addEventListener('click', () => {
    modifyDiv(addSalesPerson)
});


export { getNumberOfAttendants }

