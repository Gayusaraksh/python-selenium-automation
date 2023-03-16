from behave import given, when, then


@then('Verify {expected_amount} links are present on the Best Sellers page')
def verify_link(context,expected_amount):
    context.app.header.verify_top_links(expected_amount)


@then('Click on each top links and check correct page opened')
def click_each_top_links(context):
    context.app.header.verify_correct_page_opens()



