from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        # open page
        self.open("https://practice.automationbro.com/contact")

        # fill in all the fields
        self.send_keys('.contact-name input', 'Test name')
        self.send_keys('.contact-email input' , 'test@email.com')
        self.send_keys('.contact-phone input', '123456789')
        self.send_keys('.contact-message textarea' , 'This is a test message')
        #send_keys for css selector
        #contact- is unique within class for each 
        

        # click the submit button
        self.click("#evf-submit-277")


        # verify submit message
        self.assert_text("Thanks for contacting us! We will be in touch with you shortly" , "div[role=alert]")
        