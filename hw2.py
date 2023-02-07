"""
Amazon logo:
 driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")

Sign-in:
 driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']")

Email or mobile phone number(title):
 driver.find_element(By.XPATH,"//label[@for='ap_email']")

Email or mobile phone number(text box):
 driver.find_element( By.ID,'ap_email')

Continue button:
 driver.find_element(By.ID,'continue')

Conditions of use link:
 driver.find_element(By.XPATH, "//a[contains(@href,'/ref=ap_signin_notification_condition_of_use?')]")

Privacy Notice link:
 driver.find_element(By.XPATH, "//a[contains(@href,'/ref=ap_signin_notification_privacy_notice?')]")

Need help link:
 driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

Forgot your password? link:
 driver.find_element(By.ID,"auth-fpp-link-bottom")

Other issues with sign-in link:
 driver.find_element(By.ID,'ap-other-signin-issues-link')

Create your amazon account button:
 driver.find_element(By.ID,'createAccountSubmit')

Privacy Notice link (footer):
 driver.find_element(By.XPATH, "//a[contains(@href,'/ref=ap_desktop_footer_privacy_notice?') and  @class='a-link-normal']"

Conditions of Use link (footer):
 driver.find_element(By.XPATH, "//a[contains(@href,'/ref=ap_desktop_footer_cou?') and @class='a-link-normal']"

Help link (footer):
 driver.find_element(By.XPATH, "//a[@class='a-link-normal' and @target='_blank' and @rel='noopener' and @href='/help']"
"""