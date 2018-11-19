// attendants.js
import { modifyDiv, createItem, editItem, fetchAllItems } from './helpers.js'

const attendantsList = document.getElementById('attendants-list');
const attendantsCard = document.getElementById('attendants-card');
const attendantsForm = document.getElementById('add-attendant-form');

const url = 'https://store-manager-api-heroku.herokuapp.com/api/v1/attendants';

// Create attendants table structure........................................
const createAttendantsListStructure = (number, attendantId, firstName, lastName, email, username, role) => {

    const attendantsTableBody = document.getElementById('attendants-body');
    const attendantRow = document.createElement('tr');

    // create attendants columns
    const NumberTd = document.createElement('td');
    NumberTd.innerHTML = number;
    const IdTd = document.createElement('td');
    IdTd.innerHTML = attendantId;
    const firstNameTd = document.createElement('td');
    firstNameTd.innerHTML = firstName;
    const lastNameTd = document.createElement('td');
    lastNameTd.innerHTML = lastName
    const emailTd = document.createElement('td');
    emailTd.innerHTML = email
    const usernameTd = document.createElement('td');
    usernameTd.innerHTML = username
    const roleTd = document.createElement('td');
    roleTd.innerHTML = role

    const makeAdminTd = document.createElement('td');
    const makeAdminBtn = document.createElement('button')
    makeAdminBtn.innerHTML = 'Make Admin';
    makeAdminBtn.id = 'make-admin';
    makeAdminBtn.addEventListener('click', (event) => {
        event.preventDefault();
        makeAdmin(attendantId);
        alert(`${firstName} ${lastName} is now an administrator`)
    })

    makeAdminTd.appendChild(makeAdminBtn)

    attendantRow.appendChild(NumberTd)
    attendantRow.appendChild(IdTd)
    attendantRow.appendChild(firstNameTd)
    attendantRow.appendChild(lastNameTd)
    attendantRow.appendChild(emailTd)
    attendantRow.appendChild(usernameTd)
    attendantRow.appendChild(roleTd)

    attendantsTableBody.appendChild(attendantRow)

}

// Get all attendants from the api

const getAllAttendants = () => {
    fetchAllItems(url)
        .then((data) => {
            const attendants = data
            attendants.forEach((attendant, index) => {
                createAttendantsListStructure(index + 1, attendant.user_id, attendant.first_name, attendant.last_name,
                    attendant.email, attendant.username, attendant.user_type) 
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

