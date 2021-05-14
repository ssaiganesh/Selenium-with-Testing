from seleniumbase import BaseCase

class UploadTest(BaseCase):
    def test_visible_upload(self):
        #open page
        self.open("https://the-internet.herokuapp.com/upload")

        # get file path
        file_path = './data/Sample.jpg'

        # upload file
        self.choose_file("#file-upload" , file_path) #file-upload here is id

        # click the upload button
        self.click("#file-submit") #file-submit here is similar to file-upload above and is id


        # assert file uploaded text
        self.assert_text("File Uploaded!" , "h3")

    def test_hidden_upload(self):
        # open page
        self.open("https://practice.automationbro.com/cart/")

        # get file path
        file_path = './data/Sample.jpg'

        # add js code
        
        #remove_hidden_class = "document.getElementById('upfile_1').classList.remove('file_input_hidden')"
        #self.add_js_code(remove_hidden_class)        
        
        # upload file
        
        """
        self.choose_file("#input_1" , file_path) 
        # This was found but was not able to upload because this is not input type = "file"
        # The error is therefore cannot find uploaded message
        """
     
        self.choose_file('#upfile_1', file_path)
        # This works and passed full test even without adding js code


        # click upload button
        self.click("#upload_1") 

        # assert the file uploaded text
        self.assert_text("uploaded successfully" , "#wfu_messageblock_header_1_label_1")


