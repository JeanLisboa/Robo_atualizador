from flask_wtf import FlaskForm
from flask import Flask, render_template, flash
from wtforms import StringField, SubmitField, SelectField
app = Flask(__name__)


class Pesquisa_tracking(FlaskForm):
    uf = 'TODOS', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF'
    status = 'Todos','Nao Entregues','Na Expedidos','Devolucoes'
    regiao = 'TODOS', 'NORTE', 'NORDESTE', 'LESTE', 'FARMA BRASIL', 'SP/SUL ALIMENTAR DIRETO', 'SP/SUL ALIMENTAR INDIRETO','CENTRO OESTE'
    agend = 'Sem Filtro', 'Nao Agendado', 'Agendado Pedido', 'Agendado Danfe', 'Agendado Trp', 'Todos Agendados'
    empresa = 'Extrema', 'Alhandra'
    macro_canal = 'TODOS', 'ATACADO', 'CASH CARY', ' DEMAIS CANAIS', 'DISTRIBUIDOR PARCEIRO','FARMA', 'VAREJO'

    uf = SelectField("status", coerce=str, choices=[uf])
    status = SelectField("status", coerce=str, choices=[status])
    regiao = SelectField("status", coerce=str, choices=[regiao])
    agend = SelectField("status", coerce=str, choices=[agend])
    empresa = SelectField("empresa", coerce=str, choices=[empresa])
    macro_canal = SelectField("status", coerce=str, choices=[macro_canal])

    processa = SubmitField("processa")

import base_tracking
relatorio_usuarios = base_tracking.result

@app.route('/base_tracking', methods=['GET','POST'])
def pesquisa():
    # name = None
    form = Pesquisa_tracking()
    # if form.validate_on_submit():
    if form:
        uf = form.uf.data
        status = form.status.data
        regiao = form.regiao.data
        agend = form.agend.data
        empresa = form.empresa.data
        macro_canal = form.macro_canal.data
    form.uf.data = ''
    form.status.data = ''
    form.regiao.data = ''
    form.agend.data = ''
    form.empresa.data = ''
    form.macro_canal.data = ''

    processa_pesquisa = relatorio_usuarios
    return render_template("tracking_pesquisa.html",
                           uf=uf,
                           status=status,
                           regiao=regiao,
                           agend=agend,
                           empresa=empresa,
                           macro_canal=macro_canal,
                           processa_pesquisa=processa_pesquisa
                           )
