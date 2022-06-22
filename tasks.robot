*** Settings ***
Library     RPA.Robocorp.Vault
Library     AtlassianLibrary
Task Setup    Authorize Atlassian


*** Tasks ***
Minimal task
    Log To Console    Create Jira issue
    ${summary}    Set Variable    Main order flow on the website is broken on macOS Chrome
    Create Ticket    ${summary}    10001

*** Keywords ***
Authorize Atlassian
    Log To Console    Create Jira client
    ${secrets}=    Get Secret    Atlassian
    Auth Jira Password    ${secrets}[jira_url]    ${secrets}[jira_user]    ${secrets}[jira_token]

