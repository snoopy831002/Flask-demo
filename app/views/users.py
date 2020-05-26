# app/views/users.py
from app.models.users import User,_create, _update, _destroy
from flask import request, render_template, abort

class views:
  def page_not_found():
    return abort(404)

  # Render the index page
  def index():
    return render_template('users/index.html')

  # Render the creation page
  def new(url):
    user = User()
    return render_template('users/new.html', user = user, url=url)

  # Backend api for creation
  def create():
    username = request.form['username']
    email = request.form['email']
    _create(username, email)
    return "User creation successful!"

  def show(id, url_update):
    user = User.query.filter_by(id=id).first()
    return render_template('users/show.html',user=user,url_update = url_update)

  # This is a backend function
  def edit(id, url_update, url_delete):
    user = User.query.filter_by(id=id).first()
    return render_template('users/edit.html',user=user, url_update = url_update, url_delete = url_delete)

  #This is a backend function
  def update(id):
    email = request.form['email']
    _update(id,email)
    return

  # This is a backend function
  def destroy(id):
    _destroy(id)
    return