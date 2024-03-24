from model.project import Project
import random
from random import randrange


# def test_delete_some_project(app):
#     if len(app.mantis_project.get_project_list()) == 0:
#         app.mantis_project.create_project(Project(name="some_project", description="some_descr"))
#     old_projects = app.mantis_project.get_project_list()
#     index = randrange(len(app.mantis_project.get_project_list()))
#     app.mantis_project.delete_project_by_index(index)
#     new_projects = app.mantis_project.get_project_list()
#     assert len(old_projects) - 1 == len(new_projects)
#     old_projects.remove(old_projects[index])
#     assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def test_delete_some_project(app):
    if len(app.soap.get_project_list()) == 0:
        app.mantis_project.create_project(Project(name="some_project", description="some_descr"))
    old_projects = app.soap.get_project_list()
    index = randrange(len(app.soap.get_project_list()))
    app.mantis_project.delete_project_by_index(index)
    new_projects = app.soap.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(old_projects[index])
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
