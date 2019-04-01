from behave import given, when, then


@given(u'the following first two "{number1}" and "{number2}"')
def step_impl(context, number1, number2):
    context.number1 = number1
    context.number2 = number2
    pass


@when('when I add them')
def step_impl(context):
    context.sum = int(context.number1) + int(context.number2)
    print(context.sum)

@when(u'when I Subtract them')
def step_impl(context):
    context.sum = int(context.number1) - int(context.number2)
    print(context.sum)

@then('the result should be "{output}" on the screen')
def runtest(context, output):
    assert int(context.sum) == int(output)
    print(output)


