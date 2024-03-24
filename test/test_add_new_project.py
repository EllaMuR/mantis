from model.project import Project
from random import randint

# def test_add_new_project(app):
#     old_projects = app.mantis_project.get_project_list()
#     project = Project(name="Test project name"+str(len(old_projects)+randint(1,1000)), description="test project description")
#     app.mantis_project.create_project(project)
#     new_projects = app.mantis_project.get_project_list()
#     old_projects.append(project)
#     assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_add_new_project_soap(app):
    old_projects = app.soap.get_project_list()
    project = Project(name="Test project name"+str(len(old_projects)+randint(1,1000)), description="test project description")
    app.mantis_project.create_project(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)