from .. import routes
from flask import render_template, redirect, url_for, current_app
from forms import UploadForm, DeleteForm, ThankPostForm, ThankUserForm, CreateCategoryForm
from models import *
import datetime
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_login import current_user, login_user, logout_user, login_required

from youtube_transcript_api import YouTubeTranscriptApi

@routes.route('/thanks/post/<id>', methods=['GET', 'POST'])
@login_required
def thanks_post(id=None):
    form = ThankPostForm()
    print(form.errors)

    if form.is_submitted():
      print("submitted")

    print(form.errors)

    if form.validate_on_submit():
        post = Post.query.get(id)
        thanked = Thank.query.filter_by(user_id=current_user.id, post_id=post.id).first()
        if thanked!=None:
            return '<h1>Ya agradeciste este post!</h1><br/><a href="/">Volver</a>'
        post.total_thanks += 1
        new_thank = Thank(
                user_id = current_user.id,
                post_id = post.id,
        )
        db.session.add(new_thank)
        db.session.commit()

        return redirect(url_for('routes.view', id=post.id))
    return render_template('thanks.html', form=form)

@routes.route('/thanks/user/<id>', methods=['GET', 'POST'])
@login_required
def thanks_user(id=None):
    form = ThankUserForm()
    print(form.errors)

    if form.is_submitted():
      print("submitted")
    #if form.validate():
      #print("valid")
    print(form.errors)
    if form.validate_on_submit():
        user = User.query.get(id)
        user.karma += 1

        db.session.commit()
        return redirect(url_for('routes.show_user', username=user.username))

    return render_template('thanks.html', form=form)

@routes.route('/delete/post/<id>', methods=['GET', 'POST'])
@login_required
def delete(id=None):
    form = DeleteForm()
    print(form.errors)

    if form.is_submitted():
      print("submitted")

    #if form.validate():
      #print("valid")

    print(form.errors)
    print('Estoy acá1')

    if form.validate_on_submit():
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()

        return redirect(url_for('routes.index'))
        # Ahora debería guardar el catalogo del negocio en la db

    elemento = Post.query.get(id)
    return render_template('user/delete.html', form=form)

@routes.route('/categories',methods=['GET','POST'])
def categories():
    lista_categorias = CategoryList.query.all()
    print(lista_categorias)
    return render_template('categories.html', lista_categorias=lista_categorias)

@routes.route('/createcategory',methods=['GET','POST'])
@login_required
def createcategory():
    form = CreateCategoryForm()
    print(form.errors)

    if form.validate_on_submit():
        new_category = CategoryList(
            name = form.category.data,
        )
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('routes.index'))
    return render_template('user/createcategory.html', form=form)


@routes.route('/upload',methods=['GET','POST'])
@login_required
def upload():
    form = UploadForm()
    lista_categorias = CategoryList.query.all()

    # Hacerlo de una forma más pythonica o como quiera que se diga.
    Categorias = []
    for c in lista_categorias:
        Categorias.append((c.name,c.name.title()))
    form.category.choices = Categorias

    print(form.errors)

    if form.is_submitted():
      print("submitted")

    #c = Category.query.filter_by(name='gaming').first()
    #print(c.id)

    print(form.errors)
    print('Estoy acá1')

    if form.validate_on_submit():
        f = form.thumbnail.data
        filename = secure_filename(f.filename)
        # Detectar si es un video o una imágen depediendo el ext guardar en diferentes carpetas.
        ext = os.path.splitext(filename)[1]
        f.save(os.path.join(
            current_app.config['UPLOAD_FOLDER'], 'images', filename
        ))

        # ¿Existe la categoría a la que intentás agregar un post?
        c = CategoryList.query.filter_by(name=form.category.data).first()
        if c == None:
            return '<h1>No existe esa categoría</h1><br/><a href="/upload">Volver a intentar</a>'

        # Ahora debería guardar el catalogo del negocio en la db
        new_post = Post(
            subject = form.subject.data,
            desc = form.desc.data,
            autor = current_user.username,
            # Crear el thumbnail pequeño
            thumbnail = filename,
            thumbnail_max = filename,
            #tags = form.tags.data,
            # cambiar a category
            created_date = datetime.datetime.utcnow(),
            views = 0,
            total_thanks = 0,
            hidden = False,
        )
        # Ahora tengo que subir la cantidad de posteos del usuario.
        user = User.query.get(current_user.id)
        user.posts += 1

        db.session.add(new_post)
        db.session.commit()

        # Agrego una categoría al post, si no existe no deberías poder 
        # agregar un post a una categoría inexistente
        new_post_category = Category(
            category = c,
            post_id = new_post.id
        )
        db.session.add(new_post_category)
        db.session.commit()

        print(form.tags.data)
        tags = form.tags.data.split(' ')
        print(tags)

        for tag in tags:
            new_post_tag = Tag(
                tag_name = tag,
            )
            new_post.tags.append(new_post_tag)
            db.session.commit()


        return redirect(url_for('routes.view',id=new_post.id))

    return render_template('upload.html', nbar='upload', form=form, lista_categorias=lista_categorias)

