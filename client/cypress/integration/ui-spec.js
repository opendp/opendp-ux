{
  describe('My First Test', () => {
      it('Does not do much!', () => {
          expect(true).to.equal(true)
      })
  }),
      describe('The Home Page', () => {
          it('successfully loads', () => {
              cy.visit('/')
          })
      }),

      describe('The Home Page Title', () => {
          it('successfully loads', () => {
              cy.visit('/')
              cy.get('h2')
                  .should('contain', 'Open')
          })
      })
    describe('The Home Page', () => {
        it('shows correct error message', () => {
            cy.visit('/')
            cy.get('div')
                .should('contain', 'To create a DP Release, please make a request from an registered Dataverse installation')
        })
    })
    describe('Mock DV Request', () => {
        it('correctly redirects to homepage', () => {
            cy.visit('/mock-dv')
            cy.get('#postOpenDP > .v-btn__content').click();
            cy.get('.v-form').submit();
            cy.url().should('include', '/?id=');

        })
    })

}

