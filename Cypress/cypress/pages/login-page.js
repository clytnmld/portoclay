export class LoginPage {
    doVisitUrl(){
        cy.visit('/')
    }
    doLogin(username, password){
        this.doInputUsername(username)
        this.doInputPassword(password)
    }
    doInputUsername(username){
        cy.get('[name="username"]').type(username)
    }
    doInputPassword(password){
        cy.get('[name="password"]').type(password)
    }
    doClickLoginButton(){
        cy.get('button').contains('Login').click()
    }
    validateShowErrorLogin(){
        cy.get('.orangehrm-login-error').contains('Invalid credentials').should('be.visible')
    }
    validateSuccessLogin(){
        cy.url().should("include", "/dashboard")
        cy.get('.oxd-topbar-header-title').contains('Dashboard').should('be.visible')
    }
}