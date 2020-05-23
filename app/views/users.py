# app/views/users.py
from app.models.users import User
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

  # Render the
  def new():
    user = User()
    return render_template('users/new.html', user = user)

  def create():
    username = request.form['username']
    email = request.form['email']
    user = User(username, email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('users.index'))

  def show(id):
    try:
      user = User.query.filter_by(id=id).first()
      return render_template('users/show.html')
    except TemplateNotFound:
      abort(404)

  def edit(id):
    try:
      user = User.query.filter_by(id=id).first()
      return render_template('users/edit.html')
    except TemplateNotFound:
      abort(404)

  def update(id):
    user = User.query.filter_by(id=id).first()
    email = request.form['email']
    user.email = email
    return redirect(url_for('users.index'))

  def destroy(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.index'))