*** Settings ***
Documentation    To Vadilate A login form 
Library    SeleniumLibrary 

*** Test Cases *** 
Vadilate succesful Login 
    Open Browser with saucedemo 
    Fill the Login Form 
    WAit Until It checks

*** Keywords ***
Open Browser with saucedemo 
    Open Browser    https://www.saucedemo.com/    Chrome 

Fill the Login Form
    Input Text        user-name    standard_user  
    Input Password    password    secret_sauce
    Click Button      login-button 

Wait until It checks 
    Wait Until Element Is Visible    //*[@id="header_container"]/div[2]/span




    
