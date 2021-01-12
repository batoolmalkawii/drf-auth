PR: https://github.com/batoolmalkawii/drf-auth/pull/1

In this project, we uses Django REST Framework to create an API, then “containerize” it with Docker. 
Added JWT Authentication to our API.

To run gunicorn:
`gunicorn libraryapi_project.wsgi`