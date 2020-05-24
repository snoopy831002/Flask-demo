# app/views/users.py
from app.models.users import User,create
import flask
from flask import Blueprint, request, jsonify, render_template, abort, redirect, url_for
from jinja2 import TemplateNotFound
#from .. import db

class views:
  def page_not_found():
    return abort(404)

  # Render the index page
  def index():
    return render_template('users/index.html', name = "sss")

  # Render the creation page
  def new():
    user = User() # Dont know do i need the user
    return render_template('users/new.html', user = user)

  # Backend api for creation
  def create():
    username = request.form['username']
    email = request.form['email']
    user = User(id=1,username=username, email=email)
    create(user)
    return "Done"
    #return redirect(url_for('users.index'))

  def show(id,url):
    user = User.query.filter_by(id=id).first()
    return render_template('users/show.html',user=user,url=url)

  # This is a backend function
  def edit(id):
    user = User.query.filter_by(id=id).first()
    return render_template('users/edit.html',user=user)

  #This is a backend function
  def update(id):
    user = User.query.filter_by(id=id).first()
    email = request.form['email']
    user.email = email
    return redirect(url_for('users.index'))

  # This is a backend function
  def destroy(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.index'))