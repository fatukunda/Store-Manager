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
        .then((data) => {
            setCookie(data.access_token)
            user_type = data.user_type
            if(user_type === 'admin'){
                window.location = './admin.html'
            }
            else if(user_type === 'user'){
                window.location ='./attendant.html'
            }
        })
        .catch((err) => console.log(err))
}

const setCookie = (token) => {
    window.sessionStorage.setItem('token', token)
}


form.addEventListener('submit', (event) => {
    event.preventDefault();
    login()
});
