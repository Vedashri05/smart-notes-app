from flask import Blueprint,request,Response,redirect,render_template,flash,session,url_for
from app.models import Note,User
from app import db
from flask import current_app

notes_bp=Blueprint('notes',__name__)

# Function to predict note category
def predict_category(title,content):
    if title is None:
        title=""
    if content is None:
        content=""
    
    text=title+" "+content

    text_vector=current_app.vectorizer.transform([text])
    pred_num=current_app.model.predict(text_vector)
    pred_label=current_app.label_encoder.inverse_transform(pred_num)

    return pred_label[0]


@notes_bp.route('/')
def view_notes():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    username=session['user']
    user=User.query.filter_by(username=username).first()

    if not user: #if session exist but user not
        session.clear()
        return redirect(url_for('auth.login'))
    
    selected_category=request.args.get("category","All")

    if selected_category=="All":
        notes=Note.query.filter_by(user_id=user.id).all()
    else:
        notes=Note.query.filter_by(user_id=user.id,
                        category=selected_category).all()
        
    return render_template("notes.html",notes=notes,selected_category=selected_category)


@notes_bp.route('/add',methods=["GET","POST"])
def add_note():
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    if request.method=="POST":
        title=request.form.get('title')
        content=request.form.get('content')
        user=User.query.filter_by(username=session['user']).first()

        if title and content and user:
            #using ML predicts category
            category=predict_category(title,content)

            new_note=Note(
                title=title,
                content=content,
                category=category
            )
            user.notes.append(new_note)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('notes.view_notes'))

    return render_template("note_form.html")


@notes_bp.route('/edit/<int:note_id>',methods=["GET","POST"])
def edit_note(note_id):
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    user=User.query.filter_by(username=session['user']).first()
    note=Note.query.get(note_id)

    if not note or not user:
        return redirect(url_for('notes.view_notes'))
    
    if note.user_id!=user.id:
        return redirect(url_for('notes.view_notes'))

    if request.method=="POST":
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category') #user change

        #update details
        note.title=title
        note.content=content
        note.category=category
        db.session.commit()
        flash("Note edited successfully", "success")
        return redirect(url_for('notes.view_notes'))

    return render_template("note_form.html",note=note)

    
@notes_bp.route('/delete/<int:note_id>',methods=["POST"])
def delete_note(note_id):
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    user=User.query.filter_by(username=session['user']).first()
    note=Note.query.get(note_id)

    if not note or not user:
        return redirect(url_for('notes.view_notes'))
    
    if note.user_id!=user.id:
        return redirect(url_for('notes.view_notes'))

    #delete note
    db.session.delete(note)
    db.session.commit()
    flash("Note deleted successfully", "success")
    return redirect(url_for('notes.view_notes'))


@notes_bp.route('/display/<int:note_id>')
def display_note(note_id):
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    user=User.query.filter_by(username=session['user']).first()
    note=Note.query.get(note_id)
    notes=Note.query.filter_by(user_id=user.id).all()
    
    if not note or not user:
        return redirect(url_for('notes.view_notes'))
    
    if note.user_id!=user.id:
        return redirect(url_for('notes.view_notes'))
    
    return render_template("note_display.html",note=note,notes=notes)


