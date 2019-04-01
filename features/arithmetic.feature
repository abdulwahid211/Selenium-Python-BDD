# Created by Abdul Wahid
Feature: Basic Arithmetic

  @addition
  Scenario Outline: Add two numbers
    Given the following first two "<number1>" and "<number2>"
    When when I add them
    Then the result should be "<output>" on the screen

    Examples:
      | number1 | number2 | output |
      | 20      | 30      | 50     |
      | 2       | 5       | 7      |
      | 0       | 40      | 40     |


  @subtraction
  Scenario Outline: Subtract two numbers
    Given the following first two "<number1>" and "<number2>"
    When when I Subtract them
    Then the result should be "<output>" on the screen

    Examples:
      | number1 | number2 | output |
      | 30      | 20      | 10     |
      | 5       | 5       | 0      |
      | 4       | 40      | -36    |
