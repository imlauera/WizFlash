from . import routes
import bbcode
from flask import (
    render_template,
    redirect,
    url_for,
    current_app
)
from forms import ContactForm, CommentForm
from models import (
    db,
    Post,
    User,
    CategoryList,
    Category,
    Comment,
)
import os
import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from werkzeug.utils import secure_filename
from flask_login import (
    current_user,
)


@routes.route('/')
@routes.route('/index')
def index():
    # Orden descending
    posts = Post.query.order_by(Post.created_date.desc()).limit(25)
    destacados = Post.query.order_by(Post.views.desc()).limit(10)
    users_best_reputation = User.query.order_by(User.karma.desc()).limit(10)
    lista_categorias = CategoryList.query.all()
    return render_template(
        'home.html',
        sidebar='catalog',
        posts=posts,
        destacados=destacados,
        users=users_best_reputation,
        lista_categorias=lista_categorias
    )


@routes.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')


@routes.route('/category/<name>', methods=['GET', 'POST'])
def category(name=None):
    posts_category = Category.query.filter_by(category_name=name).limit(20)
    print(posts_category)
    return render_template(
        'category.html',
        posts_category=posts_category,
        category_name=name
    )


@routes.route('/view/<id>', methods=['GET', 'POST'])
def view(id=None):
    form = CommentForm()
    post = Post.query.get_or_404(id)
    comments = Comment.query.filter_by(
        post_id=id
    ).order_by(
        Comment.created_date.desc()
    )

    post.views += 1
    db.session.commit()

    category = Category.query.filter_by(post_id=id).first()
    if category is None:
        return """<h1>Cuando creaste el post
        pusiste una categoría que ahora no existe.</h1>"""

    if form.validate_on_submit() and current_user.is_anonymous is not True:
        print(form.file.data)
        filename = secure_filename(
            form.file.data.filename
        ) if (
            form.file.data is not None
        ) else ''

        # filename = filename if (filename is not None) else ''

        print("el valor de filename es: {}".format(filename))
        new_comment = Comment(
            post_id=id,
            comment=bbcode.render_html(form.comment.data),
            created_date=datetime.datetime.utcnow(),
            user_id=current_user.id,
            filename=filename,
            file_ext=filename.split('.').pop(),
        )
        db.session.add(new_comment)
        db.session.commit()

        file = form.file.data

        if file is not None:
            file.save(os.path.join(
                current_app.config['UPLOAD_FOLDER'], 'images', filename
            ))

        ''' No more multiple files uploader
        if form.files.data is not None:
            filename = secure_filename(f.filename)
            print(f.filename)
            f.save(os.path.join(
                current_app.config['UPLOAD_FOLDER'], 'images', filename
            ))
            new_comment_files = FileComment(
                comment_id=new_comment.id,
                file=filename,
                extension=filename.split('.').pop()
            )
            db.session.add(new_comment_files)

        db.session.commit()
        '''

        return redirect(
            url_for(
                'routes.view',
                id=id
            )
        )
    elif form.validate_on_submit() and current_user.is_anonymous is True:
        return redirect(
            url_for(
                'routes.login',
            )
        )

    return render_template(
            'view.html',
            post=post,
            category=category.category.name,
            form=form,
            comments=comments
    )


@routes.route('/rules', methods=['GET'])
def rules():
    return render_template('rules.html')


@routes.route('/helpme', methods=['GET'])
def services():
    return render_template('helpme.html', sidebar='services')


@routes.route('/globalmsgs', methods=['GET'])
def globalmsgs():
    return render_template('global.html')


@routes.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    print(form.errors)

    print(form.errors)
    print('Estoy acá1')
    if form.validate_on_submit():
        print('Estoy acá2')
        return redirect(url_for('routes.register_success'))
    # Si falla vuelve a la misma página con los
    # errores que se produjeron al intentar enviar el formulario
    return render_template('contact.html', sidebar='contact', form=form)


@routes.route('/faq', methods=['GET'])
def faq():
    return render_template('faq.html')


@routes.route('/output/<msg>')
def output(msg='Hola'):
    return render_template(
        'output.html',
        msg=msg
    )


@routes.route('/video/id/<videoId>')
def video(videoId=None):
    transcript = YouTubeTranscriptApi.get_transcript(videoId)

    '''
        print(transcript.video_id,
            transcript.language,
            transcript.language_code,
            whether it has been manually created or generated by YouTube
            transcript.is_generated,
            whether this transcript can be translated or not
            transcript.is_translatable,
            a list of languages the transcript can be translated to
            transcript.translation_languages
        )
        Get info from a video curl using Google API
        "https://www.googleapis.com/youtube/v3/videos?key=AIzaSyDsb4vxGfNEUHLVrHhNFXUCRhEnQDqqy3s
        &part={id,snippet,statistics,status,topicDetails}&id=JL295OjIBtE"
        Part is the most import variable of the query
    '''

    output = ''
    for line in transcript:
        output += 'alguien dijo <span style="color: red;">' + line['text']
        + '</span> en el minuto ' + str(line['start']) + '<br/>'

    return 'YouTube: <p>{}</p>'.format(output)
