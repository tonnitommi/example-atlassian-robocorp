from dataclasses import dataclass
from atlassian import Jira
from robot.api import logger
from RPA.Robocorp.Vault import Vault


@dataclass
class JiraIssue:
    id: str
    key: float
    url: str = None

    def __init__(self, id: str, key: float, url: str):
        self.id = id
        self.key = key
        self.url = f"{url}browse/{self.key}"


class AtlassianLibrary:
    def __init__(self):
        self._jira_url = None
        self.project = None

    def auth_jira_password(self, url, user, token):
        try:
            self.jira = Jira(url=url, username=user, password=token, cloud=True)
        except Exception as e:
            logger.console(e)

    def auth_jira_with_robocorp_vault(self, vault_name: str):
        secrets = Vault().get_secret(vault_name)
        self._jira_url = secrets["jira_url"]
        self.auth_jira_password(
            self._jira_url, secrets["jira_user"], secrets["jira_token"]
        )

    def create_ticket(self, summary: str, issuetype: str, project):
        project = project or self.project
        fields = {
            "summary": summary,
            "project": {"key": project},
            "issuetype": {"name": issuetype},
        }
        try:
            result = self.jira.issue_create(fields)
            issue = JiraIssue(result["id"], result["key"], url=self._jira_url)
            return issue
        except Exception as e:
            logger.console(e)

    def get_issue_by_key(self, issue_key: str):
        return self.jira.issue(issue_key)

    def get_issue_type_names(self):
        types = self.jira.get_issue_types()
        result = [{"name": t["name"], "description": t["description"]} for t in types]
        return result

    def get_issues(self, query: str, project: str = None):
        project = project or self.project
        result = self.jira.jql(f"project = {project} AND {query}")
        return result["issues"]

    def set_jira_project(self, project: str):
        self.project = project
