*** Settings ***
Library    OperatingSystem 

*** Test Cases ***
Check File Exists
    [Documentation]    Verify file presence 
    File Should Exist    myfile.txt 

Create And Log A List 
    @{my_list}=    Create List    Apple    Banana    Mango   #Local variable(my_list) to Create And Log A List
    Log    ${my_list} 

Loop Through List 
    @{my_list}=    Create List    Apple    Banana    Mango
    FOR    ${fruit}    IN    @{my_list}
        Log    I Like ${fruit}
    END 

Check If Mango Is In The List
    @{my_list}=    Create List    Apple    Banana    Mango 
    ${is_it}=    Evaluate    'Mango' in ${my_list}
    Run Keyword If    ${is_it}    Log    Mango is in the List


Find A Specific Fruit 
    @{my_list}=    Create List    Apple    Banana    Orange 
    FOR    ${fruit}    IN    @{my_list}
        Run Keyword If    '${fruit}' == 'Banana'    Log    Found Banana!
    END

Count Items In List 
    @{my_list}=    Create List    Apple    Banana    Orange 
    ${countit}=    Get Length    ${my_list}
    Log    There are ${countit} fruits in the list 



