from flask import url_for
from app import app
from app.views.users import views
from jinja2 import TemplateNotFound


# Index page
@app.route('/', methods=['GET'])
def index():
    return views.index()

# Create new user page
@app.route('/new', methods=['GET'])
def new():
  url = url_for("create", id=id)
  return views.new(url)

# Create a new user
@app.route('/create', methods=['POST'])
def create():
  return views.create()

# Show user data
@app.route('/<int:id>', methods=['GET'])
def show(id):
  try:
    url_update = url_for("edit", id=id)
    return views.show(id, url_update)
  except TemplateNotFound:
    return abort(404)


@app.route('/<int:id>/edit', methods=['GET'])
def edit(id):
    url_update = url_for("update", id=id)
    url_delete = url_for("destroy", id=id)
    return views.edit(id, url_update = url_update, url_delete = url_delete)


@app.route('/<int:id>', methods=['POST'])
def update(id):
  views.update(id)
  return "User update successful!"


@app.route('/<int:id>/delete', methods=['POST'])
def destroy(id):
  views.destroy(id)
  return "User deleted !"
