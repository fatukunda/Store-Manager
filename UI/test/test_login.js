const assert = require('assert');

let formLogin = document.getElementById('form-login')

beforeEach(() => {
    formLogin = formLogin.cloneNode(true)
})

describe('test user login', () => {
    it('should return an error when the username is invalid', () => {
        const username = document.getElementById('username');
        const password = document.getElementById('password')

        username.value = 'simonLee'
        password.value = 'simon1234'

        const result = validateForm(formLogin)
        expect(result.isValid).to.be.true;
        expect(result.errors.length).to.equal(0);
        
    })
})