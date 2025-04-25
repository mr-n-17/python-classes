*** Settings ***
Documentation    To Vadilate A login form 
Test Setup       Open the Browser with saucedemo
Test Teardown    Close Browser
Library          SeleniumLibrary 
Resource         resource.robot


*** Test Cases *** 
Vadilate succesful Login  
    Fill the Login Form    ${user_name}    ${valid_password}
    Wait Until It checks    //*[@id="header_container"]/div[2]/span 
    Verify Card Titles In the Shop Page 


*** Keywords ***
Fill the Login Form
    [Arguments]    ${username}    ${p}
    Input Text            user-name        ${username}  
    Input Password        password         ${p}
    Click Button          login-button 

Wait until It checks 
    [Arguments]    ${e}
    Wait Until Element Is Visible    ${e}
    Log    Successful 

Verify Card Titles In the Shop Page 
    @{ele}=    Create List    Sauce Labs Backpack    Sauce Labs Bike Light    Sauce Labs Bolt T-Shirt    Sauce Labs Fleece Jacket    Sauce Labs Onesie    Test.allTheThings() T-Shirt (Red)
    ${e}=    Get WebElements    css:.inventory_item_name 
    FOR    ${i}    IN    @{e}
        ${text}=    Get Text    ${i}
        Should Contain    ${ele}    ${text}
        Log    Validated Card Title: ${text}
    END 
