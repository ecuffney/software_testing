require "selenium-webdriver"
require "rspec"
require_relative "SignMeUp.rb"
require_relative "captcha_page.rb"

timestamp = Time.now.to_i
email = "user{#{timestamp}@tester.com"  #creates unqiue email address each test
first_name = "Rusty"
last_name = "Snuggles"
expected_text = "Confirm Humanity"

describe "attempt email sign up..." do
    describe "attempt name info..." do
        it "checks if human confirm captcha appears" do

            @driver = Selenium::WebDriver.for :firefox
            @driver.get "https://us16.list-manage.com/subscribe?u=b3cc95f84ec1e821157a8d62d&id=abe6c495ce" #driver.get ensures page is fully loaded
            signup = SignMeUp.new(@driver)
            signup.enter_email(email)
            signup.enter_first_name(first_name)
            signup.enter_last_name(last_name)
            signup.check_button() #clicks checkbox for email signup
            signup.subscribe_button() #clicks subscribe
            human = ConfirmCapt.new(@driver)
            confirm_human_text = human.confirm_captcha()
            expect(confirm_human_text).to include(expected_text) #confirms captcha prompt
            @driver.quit

        end
    end
end
