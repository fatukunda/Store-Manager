//LOGIN
const form = document.getElementById('form-login');
const username = document.getElementById('username');
const password = document.getElementById('password');
//Add a submit event on the login form
form.addEventListener('submit', (event) => {
    event.preventDefault();
    //Check if user is admin and redirect them to admin panel
    if(username.value === 'admin' && password.value ==='admin'){
        window.location = './admin.html';
    //Redirect a store attendant to the attendant profile
    }else if(username.value === 'user' && password.value === 'user'){
        window.location = './attendant.html';
    }else{
        window.location ='./admin.html'
        // alert('Invalid username or password');
        // username.value ='';
        // password.value ='';
    }
});
