from behave import given, when, then

@given(u'the user is taken to the form page')
def step_impl(context):
    #loadPage()
    raise NotImplementedError(u'STEP: Given the user is taken to the form page')


@when(u'the user presses the submit button without inserting anything')
def step_impl(context):
    #submitForm()
    raise NotImplementedError(u'STEP: When the user presses the submit button without inserting anything')


@then(u'the alert message should be shown')
def step_impl(context):
    #assertAlertMessage()
    raise NotImplementedError(u'STEP: Then the alert message should be shown')


@given(u'the user is taken to the form page and fills in the details')
def step_impl(context):
    # loadPage()
    # fillAllDetails()
    raise NotImplementedError(u'STEP: Given fills in the necessary details')


@when(u'the user presses the submit button')
def step_impl(context):
    # submitForm()
    raise NotImplementedError(u'STEP: When the user presses the submit button')


@then(u'the user should see the pictures of 3 cats')
def step_impl(context):
    # assertCatsPics
    raise NotImplementedError(u'STEP: Then the user should see the pictures of 3 cats')


