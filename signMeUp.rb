
class SignMeUp

#define css selector:
EMAIL_FIELD = {id: 'MERGE0'}
FIRST_NAME_FIELD = {id: 'MERGE1'}
SECOND_NAME_FIELD = {id: 'MERGE2'}
CLICK_CHECK_BUTTON = {class: 'checkbox'}
CLICK_SUBSCRIBE = {class: 'formEmailButton'}

attr_reader :driver

#class method:
def initialize(driver)
  @driver = driver    #passes driver into attr reader above
end

def enter_email(email)
  email_field= @driver.find_element(EMAIL_FIELD)
  email_field.send_keys(email)
end

def enter_first_name(first_name)
  first_name_field = @driver.find_element(FIRST_NAME_FIELD)
  first_name_field.send_keys(first_name)
end

def enter_last_name(last_name)
  last_name_field = @driver.find_element(SECOND_NAME_FIELD)
  last_name_field.send_keys(last_name)
end

def check_button()
  click_check_button = @driver.find_element(CLICK_CHECK_BUTTON)
  click_check_button.click
end

def subscribe_button()
  click_subscribe = @driver.find_element(CLICK_SUBSCRIBE)
  click_subscribe.click
end

end
