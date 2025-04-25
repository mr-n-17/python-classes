*** Settings ***
Documentation    To Vadilate A login form 
Test Setup       Open the Browser with saucedemo
Test Teardown    Close Browser
Library          SeleniumLibrary 
Resource         resource.robot


*** Test Cases *** 
Vadilate Unsuccesful Login 
    Fill the Login Form    ${user_name}    ${invalid_password}
    Wait until It Checks And Displays error message    //*[@id="login_button_container"]/div/form/div[3]/h3
    Verify error message is correct    //*[@id="login_button_container"]/div/form/div[3]/h3

*** Keywords ***
Fill the Login Form
    [Arguments]    ${username}    ${p}
    Input Text            user-name    ${username}  
    Input Password        password     ${p} 
    Click Button          login-button 

Wait until It Checks And Displays error message
    [Arguments]    ${element}
    Wait Until Element Is Visible   ${element} 

Verify error message is correct 
    [Arguments]    ${element}
    ${result}    Get Text    ${element}  
    Should Be Equal As Strings    ${result}   Epic sadface: Username and password do not match any user in this service
