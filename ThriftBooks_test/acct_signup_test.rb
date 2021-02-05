require "selenium-webdriver"
require "rspec"
require_relative "thrift_sign_up.rb"
require_relative "users_page.rb"

timestamp = Time.now.to_i
firstname = "Rusty"
lastname = "Snuggles"
email = "user#{timestamp}@test.com" #adds unique timestamp string for new user email each test instance
password = "password1312"
expected_greeting = "Hi Rusty!"


describe "user sign up" do
    describe "sign up as new user" do
        it "confirms a user can sign up" do


            @driver = Selenium::WebDriver.for :firefox
            @driver.get "https://www.thriftbooks.com/account/login/?wapas=https%3a%2f%2fwww.thriftbooks.com%2faccount%2flogin%2f&newaccount=true"
            signup = SignupPage.new(@driver)
            signup.enter_first_name(firstname)
            signup.enter_last_name(lastname)
            signup.enter_email(email)
            signup.enter_password(password)
            signup.confirm_password(password)
            signup.uncheck()
            signup.submit_button()
            checkuser = CheckUser.new(@driver)
            greeting_text = checkuser.user_greeting()
            expect(greeting_text).to eq(expected_greeting)

            driver.quit

        end
    end
end
