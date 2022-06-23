*** Settings ***
Library         RPA.Robocorp.Vault
Library         AtlassianLibrary

Task Setup      Authorize Atlassian


*** Tasks ***
Create Issue
    Log To Console    Create Jira issue
    ${summary}    Set Variable    Main order flow on the website is broken on macOS Chrome
    ${issue}    Create Ticket    ${summary}    Bug    project=BEIS
    Log To Console    Issue: ${issue}

Get Issue
    Log To Console    Get Jira issue
    ${issue}    Get Issue By Key    BEIS-10
    Log To Console    Issue: ${issue}\n\n
    Set Jira Project    BEIS
    ${issues}    Get Issues    status NOT IN (Closed, Resolved) ORDER BY issuekey

    FOR    ${issue}    IN    @{issues}
        Log To Console    ${issue}[key]    #${issue}[description]\n\n
    END

List Issue Types
    Log To Console    List Issue Types
    ${issue_types}    Get Issue Type Names
    FOR    ${type}    IN    @{issue_types}
        Log To Console    ${type}
    END


*** Keywords ***
Authorize Atlassian
    Log To Console    Create Jira client
    #${secrets}=    Get Secret    Atlassian
    #Auth Jira Password    ${secrets}[jira_url]    ${secrets}[jira_user]    ${secrets}[jira_token]
    Auth Jira With Robocorp Vault    Atlassian
