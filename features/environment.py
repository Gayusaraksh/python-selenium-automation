from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.application import Application
from support.logger import logger
from selenium.webdriver.support.events import EventFiringWebDriver
from support.logger import logger, MyListener

def browser_init(context,test_name):
    """
    :param context: Behave context
    """
    service = Service(executable_path='/Users/bala/Automation/python-selenium-automation/chromedriver')
    # service = Service(executable_path='/Users/bala/Automation/python-selenium-automation/geckodriver')
    context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Firefox(service=service)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # Terminal command:
    # behave feature/tests/amazon_signin.feature
    # behave feature/tests/ -t smoke

    # Allure command:
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )
    # ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(service=service),
    #     MyListener()
    # )
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())



    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'gayu_BFN6ZX'
    # bs_key = 'gCzyaA1qfpGgsTDB9Npq'
    #
    #
    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'sessionName': test_name
    # }
    #
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)



def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context,scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
