*** Settings *** 
Library    Collections 
Library    BuiltIn
Library    String

*** Test Cases ***
Create A New Dict 
    ${dict1}=    Create Dictionary    name=John    age=21 

    Set To Dictionary    ${dict1}    place=TPT 

    Log    DICT IS: ${dict1} 


    Remove From Dictionary    ${dict1}    name 
    
    Log    DICT IS: ${dict1} 
