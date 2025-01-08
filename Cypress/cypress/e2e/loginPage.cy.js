describe('Login page tests', () => {
  beforeEach(() => {
    cy.visit('https://opensource-demo.orangehrmlive.com/');
  })
  it.only('validLogin', function() {
    /* ==== Generated with Cypress Studio ==== */
    cy.fixture('userData').then((userData) => {
      cy.getByName('username').type(userData.username);
      cy.getByName('password').type(userData.password);
    })
    cy.get("button[type='submit']").click();
    /* ==== End Cypress Studio ==== */
  });
  it('invalidLogin', function() {
    /* ==== Generated with Cypress Studio ==== */
    cy.getByName('username').type('Admin');
    cy.getByName('password').type('admin1231');
    cy.get("button[type='submit']").click();
    cy.contains('Invalid credentials').should('be.visible');
    /* ==== End Cypress Studio ==== */
  });

  it('emptyLogin', function() {
    /* ==== Generated with Cypress Studio ==== */
    cy.get("button[type='submit']").click();
    cy.get(".oxd-form-row").eq(0).contains('Required').should('be.visible');
    cy.get(".oxd-form-row").eq(1).contains('Required').should('be.visible');
    /* ==== End Cypress Studio ==== */
  });

  it('should navigate to LinkedIn and back', () => {
    cy.get("a[href='https://www.linkedin.com/company/orangehrm/mycompany/']").invoke('removeAttr', 'target').click();
    cy.origin('https://www.linkedin.com', () => {
      cy.url().should('include', '/company/orangehrm');
      cy.go('back');
    });
    cy.url().should('eq', 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');
  });

  it('should navigate to Facebook and back', () => {
    cy.get("a[href='https://www.facebook.com/OrangeHRM/']").should('be.visible')
  });

  it('should navigate to twitter and back', () => {
    cy.get("a[href='https://twitter.com/orangehrm?lang=en']").invoke('removeAttr', 'target').click();
    cy.origin('https://x.com', () => {
      cy.url().should('include', '/orangehrm');
      cy.go('back');
    });
    cy.url().should('eq', 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');
  });

  it('should navigate to youtube and back', () => {
    cy.get("a[href='https://www.youtube.com/c/OrangeHRMInc']").should('be.visible')
  });
})