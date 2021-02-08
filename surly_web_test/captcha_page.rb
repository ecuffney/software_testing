class ConfirmCapt

#define css selector:
CONFIRM_HUMAN = {id: 'templateBody'}

attr_reader :driver

#methods:
def initialize(driver)
  @driver =  driver
end

def confirm_captcha()
  human_check = @driver.find_element(CONFIRM_HUMAN)
  human_check_text= human_check.text
end

end
