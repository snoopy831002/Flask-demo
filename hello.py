from flask import render_template
from app.views.users import views
from app import app

# Define route and method
@app.route('/', methods=['GET'])
def index():
    return views.index()


@app.route('/new', methods=['GET'])
def new():
  return views.new()


@app.route('/create', methods=['POST'])
def create():
  return views.create()
  #username = request.form['username']
  #email = request.form['email']
  #user = User(username, email)
  #db.session.add(user)
  #db.session.commit()
  #return redirect(url_for('users.index'))


@app.route('/<int:id>', methods=['GET'])
def show(id):
  try:
    user = User.query.filter_by(id=id).first()
    return render_template('users/show.html', user = user)
  except TemplateNotFound:
    abort(404)
@app.route('/<int:id>/edit', methods=['GET'])
def edit(id):
  try:
    user = User.query.filter_by(id=id).first()
    return render_template('users/edit.html', user = user)
  except TemplateNotFound:
    abort(404)
@app.route('/<int:id>', methods=['POST'])
def update(id):
  user = User.query.filter_by(id=id).first()
  email = request.form['email']
  user.email = email
  return redirect(url_for('users.index'))
@app.route('/<int:id>/delete', methods=['POST'])
def destroy(id):
  user = User.query.filter_by(id=id).first()
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for('users.index'))
