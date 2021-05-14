from seleniumbase import BaseCase

class HomeTest(BaseCase):
    #pass
    def test_home_page(self):
        # open home page
        self.open("https://practice.automationbro.com")

        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")


        # assert logo
        self.assert_element(".custom-logo-link") #note the . and if you search for it

        # click on the get started button and assert the url
        self.click("#get-started")
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url) #both lines of code are testing the same

        # get the text of the header and asser the value
        #h1 tag is unique no other headers with same tag
        self.assert_text("Think different. Make different.", "h1")
        
        #Scroll to bottom and asser the copyright text
        self.scroll_to_bottom() #without this line of code , test passed
        self.assert_text("Copyright © 2020 Automation Bro" , ".tg-site-footer-section-1") #class immediately after p tag
        #self.assert_text("Copyright © 2020" , ".tg-site-footer-section-1") #PASSED
        #self.assert_text("Copyright © 2020 Automation Bro" , ".tg-container tg-container--flex tg-container--flex-top") #ERROR: E;ement was not present after 6 seconds
        #self.assert_text("Copyright © 2020 Automation Bro", "p") #ERROR: was not visible after 6 seconds -- same without Automation Bro

    def test_menu_links(self):
        expected_links = ['Home', 'About', 'Shop' , 'Blog' , 'Contact' , 'My account']

        # open url
        self.open("https://practice.automationbro.com/")

        #find menu links elements
        
        #self.find_elements("//*[starts-with(@id, 'menu-item')]") #primary-menu li [id*=menu-item] -- CSS Selector for menu items
        #print(self.find_elements("//*[starts-with(@id, 'menu-item')]")) #~ pytest -k "test_menu_links" -s  works for this
        # the above line of code prints out if print function added, prints web elements, session id and element id 
        
        menu_links_el = self.find_elements("//*[starts-with(@id, 'menu-item')]")

        #loop through our menu links
        for idx, link_el in enumerate(menu_links_el): #idx and enumerate to get index numbers
            #print(idx , link_el.text) #we are using .text to get the text value from element
            self.assertEqual(expected_links[idx] , link_el.text)
            #printing twice as in website there is secondary menu also
            #index out of range as too many menu_links due to secondary menu

#pytest checks for tests folder and test_ starting file and test_ class
# ~ pytest
# ~ pytest -k "test_home_page"  #tests only that function
# ~ pytest -k "test_menu_links" -s 


