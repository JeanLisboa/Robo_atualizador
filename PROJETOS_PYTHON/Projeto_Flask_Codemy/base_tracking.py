# import queries.connector
# from queries.connector import errorcode
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
class Teste(FlaskForm):
    processa = SubmitField("submit")
    empresa = SelectField(coerce=str, choices=['Todos','Extrema', 'Alhandra'])
    uf = SelectField(coerce=str, choices=['TODOS', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF'])
    status = SelectField(coerce=str, choices=['Todos', 'Nao Entregues', 'Na Expedidos', 'Devolucoes'])
    regiao = SelectField(coerce=str, choices=['TODOS', 'NORTE', 'NORDESTE', 'LESTE', 'FARMA BRASIL', 'SP/SUL ALIMENTAR DIRETO', 'SP/SUL ALIMENTAR INDIRETO', 'CENTRO OESTE'])
    agend = SelectField(coerce=str, choices=['Todos', 'Nao Agendado', 'Agendado Pedido', 'Agendado Danfe', 'Agendado Trp', 'Todos Agendados'])
    macro_canal = SelectField(coerce=str, choices=['TODOS', 'ATACADO', 'CASH CARY', ' DEMAIS CANAIS', 'DISTRIBUIDOR PARCEIRO', 'FARMA', 'VAREJO'])
    danfe = StringField()
    pedido = StringField()
    cod_cli = StringField()
    destinatario = StringField()
    volume = StringField()
    vendedor = SelectField(coerce=str, choices=['TODOS','ANA','KARENINA'])
    transportadora = SelectField(coerce=str, choices=['TODOS','INTECOM','TJB','TECMAR'])
    data_de = DateField()
    data_ate = DateField()

from hello import app
@app.route('/base_tracking', methods=['GET','POST'])
def trk_pesquisa():
    form_teste = Teste()
    empresa = Teste()
    empresa = empresa.empresa
    uf = Teste()
    uf = uf.uf
    status = Teste()
    status = status.status
    regiao = Teste()
    regiao = regiao.regiao
    agend = Teste()
    agend = agend.agend
    macro_canal = Teste()
    macro_canal = macro_canal.macro_canal
    data_de = Teste()
    data_de = data_de.data_de
    data_ate = Teste()
    data_ate = data_ate.data_ate
    danfe = Teste()
    danfe = danfe.danfe
    pedido = Teste()
    pedido = pedido.pedido
    cod_cli = Teste()
    cod_cli = cod_cli.cod_cli
    destinatario = Teste()
    destinatario = destinatario.destinatario
    volume = Teste()
    volume = volume.volume
    vendedor = Teste()
    vendedor = vendedor.vendedor
    transportadora = Teste()
    transportadora = transportadora.transportadora
    print(f'teste----{uf.data}')

    cnx = mysql.connector.connect(user='admin',
                                  password='204619',
                                  host='localhost',
                                  database='logistica')
    cursor = cnx.cursor()

    query = f"select * from base_tracking where UF = '{uf.data}'"
    print(query)

    cursor.execute(query)
    result = cursor.fetchall()

    if form_teste.validate_on_submit():
        cursor.fetchall()
        # result = cursor.fetchone()
        cursor.close()
        cnx.close()
    return render_template("base_tracking.html",

                           relato=result,
                           form_teste=form_teste,
                           danfe=danfe,
                           vendedor=vendedor,
                           transportadora=transportadora,
                           pedido=pedido,
                           cod_cli=cod_cli,
                           destinatario=destinatario,
                           volume=volume,
                           empresa=empresa,
                           uf=uf, status=status,
                           regiao=regiao,
                           agend=agend,
                           macro_canal=macro_canal,
                           data_de=data_de,
                           data_ate=data_ate)
