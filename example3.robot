*** Settings ***
Library    BuiltIn
Library    Collections 
Library    String

*** Test Cases ***
Add And Remove Items In List 
    @{mylist}=    Create List    Apple    Banana    Mango    Orange 
    Log    Original List: ${mylist}

    #add items
    Append To List    ${mylist}    grapes 
    Append To List    ${mylist}    Melons 
    Log    After Appending: ${mylist}

    #remoe items 
    Remove From List    ${mylist}    1 
    Log    After remooving index 1: ${mylist} 

Check fruit Availabilty 
    ${fruit}=    Set Variable    orange
    @{Mylist}=    Create List    Apple     Banana    mango

    Run Keyword If    '${fruit}' in ${Mylist}    Log    ${fruit} is available 
    Run Keyword Unless    '${fruit}' in ${Mylist}    Log    ${fruit} is Not available


Filter List Items Startiung with A 
    @{fruits}=    Create List    Apple    Mango    Amla    Apricot 
    @{f}=    Create List

    FOR    ${i}    IN    @{fruits}
        Run Keyword If    '${i}'[0]=='A'    Append To List    ${f}    ${i}
    END 


Count The Length Of The List

    @{fruits}=    Create List    Apple    Banana    Orange    Mango 
    ${Count}=    Set Variable    0 
    FOR    ${item}    IN    @{fruits}
        ${Count}=    Evaluate  ${Count} + 1
    END
    Log    Count of the list is: ${Count} 

Check Type 
    ${a}=    Set Variable    'txt'
    ${b}=    Set Variable    123
    @{list1}=    Create List    apple    orange 
    ${dict}=    Create Dictionary    name=John    age=23 

    ${type_a}=    Evaluate    type(${a}).__name__ 
    ${type_b}=    Evaluate    type(${b}).__name__ 
    ${type_list}=    Evaluate    type(${list1}).__name__ 
    ${type_dict}=    Evaluate    type(${dict}).__name__ 

    Log    Number type is: ${type_b}
    Log    str type is: ${type_a}
    Log    list type is: ${type_list}
    Log    dict type is: ${type_dict}

