class SignupPage

#defines selectors as constants:
FIRSTNAME_FIELD = {id: 'NewAccount_FirstName'}
LASTNAME_FIELD = {id: 'NewAccount_LastName'}
EMAIL_ADD = {id:'NewAccount_EmailAddress'}
EMAIL_ADD_CONFIRM = {id:'NewAccount_ConfirmEmail'}
PASSWORD_ADD = {id: 'NewAccount_Password'}
CONFIRM_PASSWORD_ADD = {id:'NewAccount_ConfirmPassword'}
CHECKBOX = {class:'Checkbox-state'}
ACCT_BUTTON = {xpath:'//*[@value="Create Account"]'}


attr_reader :driver

#class methods:

def initialize(driver)
  @driver = driver    #passes driver into attr reader above
end

def enter_first_name(firstname)
  first_name = @driver.find_element(FIRSTNAME_FIELD)
  first_name.send_keys(firstname)
end

def enter_last_name(lastname)
  last_name = @driver.find_element(LASTNAME_FIELD)
  last_name.send_keys(lastname)
end

def enter_email(email)
  email_field = @driver.find_element(EMAIL_ADD)
  email_field.send_keys(email)
end

def email_confrim(email)
  confirm_email_field = @driver.find_element(EMAIL_ADD_CONFIRM)
  confirm_email_fied.send_keys(email)
end

def enter_password(password)
 password_field = @driver.find_element(PASSWORD_ADD)
 password_field.send_keys(password)
end

def confirm_password(password)
    confirm_password_field = @driver.find_element(CONFIRM_PASSWORD_ADD)
    confirm_password_field.send_keys(password)
end

def uncheck()
  uncheck_offer= @driver.find_element(CHECKBOX)
  uncheck_offer.click
end

def submit_button()
  create_acct_button= @driver.find_element(ACCT_BUTTON)
  create_acct_button.click
end

end
