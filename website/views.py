import json

from flask import Blueprint, render_template, request, flash, jsonify
#Manage user sessions, related to hernece UserMixin
from flask_login import login_required, current_user

from . import db
from .models import Note

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    #return "<h1>Home</h1>" #Basic exampple
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('User & password are not correct!', category='error')
        else:
            new_note = Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('User & password are not correct!', category='success')
    return render_template("home.html",user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
