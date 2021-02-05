class CheckUser

#define css selector:
GREETING_SUCCESS = {class: "UserComponent-greeting"}

attr_reader :driver

#methods:
def initialize(driver)
@driver =  driver
end

def user_greeting()
  greeting = @driver.find_element(GREETING_SUCCESS)
  user_greeting = greeting.text
end

end
