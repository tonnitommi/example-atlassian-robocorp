from atlassian import Jira
from robot.api import logger

class AtlassianLibrary:

    def __init__(self):
        return

    def auth_jira_password(self, url, user, token):
        try:
            self.jira = Jira(
                url=url,
                username=user,
                password=token,
                cloud=True)
        except Exception as e:
            logger.console(e)

    def create_ticket(self, summary, issuetype):
        fields = {
            'summary': summary,
            'project': {
                'id': '10000'
            },
            'issuetype': {
                'id': str(issuetype)
            }
        }
        try:
            self.jira.issue_create(fields)
        except Exception as e:
            logger.console(e)