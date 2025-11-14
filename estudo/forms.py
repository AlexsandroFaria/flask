from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required, Email

from estudo import db
from estudo.models import Contato


class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[data_required()])
    email = StringField('E-mail', validators=[data_required(), Email()])
    assunto = StringField('Assunto', validators=[data_required()])
    mensagem = StringField('Mensagem', validators=[data_required()])
    btnsubmit = SubmitField('Enviar', validators=[data_required()])

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()