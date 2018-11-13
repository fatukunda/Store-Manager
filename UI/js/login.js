const form = document.getElementById('form-login');
const login = () => {
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const url = 'https://store-manager-api-heroku.herokuapp.com/api/v1/auth/login';
    const data = {
        username: username.value,
        password: password.value
    }
    let fetchData = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }
    fetch(url, fetchData)
        .then((res) => res.json())
        .then((data) => console.log(JSON.stringify(data.access_token)))
        .catch((err) => console.log(err))
}

form.addEventListener('submit', (event) => {
    event.preventDefault();
    login()
});

   

// //LOGIN
// const form = document.getElementById('form-login');
// const username = document.getElementById('username');
// const password = document.getElementById('password');
// //Add a submit event on the login form
// form.addEventListener('submit', (event) => {
//     event.preventDefault();
//     //Check if user is admin and redirect them to admin panel
//     if(username.value === 'admin' && password.value ==='admin'){
//         window.location = './admin.html';
//     //Redirect a store attendant to the attendant profile
//     }else if(username.value === 'user' && password.value === 'user'){
//         window.location = './attendant.html';
//     }else{
//         window.location = './admin.html';
//         // alert('Invalid username or password');
//         // username.value ='';
//         // password.value ='';
//     }
// });
