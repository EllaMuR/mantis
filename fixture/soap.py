from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        base_url = self.app.config['web']['baseUrl']
        client = Client(base_url+"api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        base_url = self.app.config['web']['baseUrl']
        client = Client(base_url+"api/soap/mantisconnect.php?wsdl")
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        project_list = []
        for project in client.service.mc_projects_get_user_accessible(username, password):
            project_list.append(Project(name=project.name, id=project.id, description=project.description))
        return project_list