from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Select item from the search list')
def select_item(context):
    context.app.search_results_page.select_product()


@then('Verify that every product on Amazon search results page has product name')
def results_all_product_name(context):
    context.app.search_results_page.results_all_product_name()


@then('Verify that every product on Amazon search results page has product image')
def results_all_product_image(context):
    context.app.search_results_page.results_all_product_image()


@then('Verify {alias} department is selected')
def verify_sel_dept_opened(context,alias):
    context.app.search_results_page.verify_select_dept(alias)