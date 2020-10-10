from . import db
from models import User
import datetime

tags = db.Table('tags',
                db.Column(
                    'tag_id',
                    db.Integer,
                    db.ForeignKey('tag.id'),
                    primary_key=True
                ),
                db.Column(
                    'post_id',
                    db.Integer,
                    db.ForeignKey('post.id'),
                    primary_key=True
                )
                )


class Tag (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String, nullable=False)

# children = relationship("Child", cascade="all,delete", backref="parent")


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=True)
    views = db.Column(db.Integer, nullable=True)
    hidden = db.Column(db.Integer, nullable=True)
    # Para que pueda acceder a las tags desde post.
    tags = db.relationship('Tag', secondary=tags)
    # El thumbnail tiene que ser generado
    # a partir de la primera imagen o video que se sube
    thumbnail = db.Column(db.String, nullable=False)
    thumbnail_max = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    total_thanks = db.Column(db.Integer, nullable=True)
    # Crea el atributo .post en Category y Comment
    categories = db.relationship(
        "Category",
        cascade="all,delete",
        backref="post"
    )
    comments = db.relationship(
        "Comment",
        cascade="all,delete",
        backref="post"
    )
    thanks = db.relationship(
        "Thank",
        cascade="all,delete",
        backref="post"
    )
    files = db.relationship(
        "FilePost",
        cascade="all,delete",
        backref="post"
    )

    # One To Many relationship, es decir un
    # post puede tener muchos archivos adjuntos.
    # No sé si es la mejor forma de hacerlo.
    # Esto se puede agregar directamente en el campo
    # de FileARchivo y no se necesita agregar la
    # relación acá yo prefiero hacer eso.
    # pdfs = db.relationship('FilePost', backref='post', lazy=True)

# Después de crear el post usar nuevo_articulo = Catalogo(32,'Linux')
# Esta es la estructura que se me ocurrió para luego poder buscar los posts por
# categoría.
# Igual a Tag
# Analizar mejor esta definición

# Lista de categorías aceptables.


class CategoryList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String,
        unique=True,
        nullable=False
    )

# Relaciono el posteo con una categoría, si la categoría no existe
# en CategoryList no vas a poder subirlo
# (este chequeo lo hago en routes/upload.py).
# Acá no tenemos id.
# La parte que más me costó y todavía no entiendo como funciona.
# primary key = única y no nula.


class Category(db.Model):
    post_id = db.Column(
            db.Integer,
            db.ForeignKey(Post.id),
            primary_key=True
    )
    # Me obliga a usar esto para definir bien la relación
    category = db.relationship('CategoryList', backref='categories')
    # Igual necesito establecer esta relación aunque no la use.
    category_name = db.Column(db.String, db.ForeignKey(CategoryList.name))

    # Para poder acceder desde la view al subject: category.post.subject
    # post = db.relationship('Post', cascade='all, delete')


class Comment(db.Model):
    # Para citar un comentario, deberías citar el id.
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(
            db.Integer,
            db.ForeignKey(Post.id)
    )
    user_id = db.Column(
            db.Integer,
            db.ForeignKey(User.id)
    )
    # Para que pueda acceder a los datos
    # del usuario haciendo comment.user.username
    user = db.relationship('User', cascade='all, delete')
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    comment = db.Column(db.String, nullable=False)
    files = db.relationship('FileComment', cascade='all, delete')
    # Para poder acceder desde la view al subject: category.post.comment
    # post = db.relationship('Post', cascade='all, delete')


class GlobalMsg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String, nullable=False)


# Una tabla para sólo permitir un agradecimiento por autor
# y tener una lista de quien agradeció al post.
# Ejemplo de uso: primero agregá +1 al thanks del post
# después: nuevo_agradecimiento = Thank(43,'futterstaffel')
class Thank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User')
    # Ahora convierto a user_id como la primary key.
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id')
    )


class FileComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(
        db.Integer,
        db.ForeignKey('comment.id'),
    )
    file = db.Column(db.String, nullable=False)
    extension = db.Column(db.String, nullable=False)


class FilePost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(
        db.Integer,
        db.ForeignKey('post.id'),
    )
    file = db.Column(db.String, nullable=False)
    extension = db.Column(db.String, nullable=False)
