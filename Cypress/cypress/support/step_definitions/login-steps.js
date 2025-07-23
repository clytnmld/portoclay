import { Given, When, Then, And } from "@badeball/cypress-cucumber-preprocessor";
import { LoginPage } from "../../pages/login-page";

const loginPage = new LoginPage()

let credential
before(()=>{
    cy.fixture("list_user").then((data)=>{
        credential = data
    })
    cy.window().then((win) => {
        // Try removing any persistent UI popups
        const warning = win.document.querySelector('[role="alert"]');
        if (warning) warning.remove();
      });
      
})

Given("I open the orangeHRM website",()=>{
    loginPage.doVisitUrl()
})

When("I do login using {string} account",(user)=>{
    let username = credential.users[user].username
    let password = credential.users[user].password
    loginPage.doLogin(username, password)
})

When("I do input username {string}",(user)=>{
    loginPage.doInputUsername(user)
})

When("I do input password {string}",(password)=>{
    loginPage.doInputPassword(password)
})

Then("I saw error message for failed login invalid credentials",()=>{
    loginPage.validateShowErrorLogin()
})

Then("I success login and already in dashboard page",()=>{
    loginPage.validateSuccessLogin()
})

Then("I click button login", ()=>{
    loginPage.doClickLoginButton()
})