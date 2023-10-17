import datetime
from datetime import datetime
from datetime import date
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField
import mysql.connector
from workadays import workdays as wd
from datetime import timedelta
import plotly.express as px


app = Flask(__name__)
# secret key
# no terminal, python / import secrets / secrets.token_hex(25)

app.config['SECRET_KEY'] = "f92ed5835155e99cc60e347de2cce349830e28984c160aa3e2"


# informações de acesso ao mysql
cnx = mysql.connector.connect(user='admin',
                              password='204619',
                              host='localhost',
                              database='logistica')
cursor = cnx.cursor()


@app.route('/')
def index():
    stuff =  '<strong>MEGA DASH EM ANDAMENTO </strong>'
    first_name = 'jean'
    equipe = 'Jean', 'Andreia', 'Daiane', 'Debora', 'Luana', 'Gisele', 'Fernanda'
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff, equipe=equipe)


class Teste(FlaskForm): # configura os botoes do html 'tracking'
    processa = SubmitField("Processa")
    empresa = SelectField(coerce=str, choices=['EXTREMA', 'ALHANDRA'])
    uf = SelectField(coerce=str, choices=['TODOS', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF'])
    status = SelectField(coerce=str, choices=['TODOS', 'ENTREGUE', 'EM TRANSITO', 'SEM DEFINICAO DE AGENDA', 'DEVOLUCAO'])
    regiao = SelectField(coerce=str, choices=['TODOS', '01 NORTE', '02 NORDESTE', '03 LESTE', '04 FARMA BRASIL', '05 SP/SUL ALIMENTAR DIRETO', '06 SP/SUL ALIMENTAR INDIRETO', '07 CENTRO OESTE'])
    agend = SelectField(coerce=str, choices=['TODOS', 'S', 'N'])
    macro_canal = SelectField(coerce=str, choices=['TODOS', 'ATACADO', 'CASH CARY', 'DEMAIS CANAIS', 'DISTRIBUIDOR PARCEIRO', 'FARMA', 'VAREJO'])
    danfe = StringField()
    pedido = StringField()
    cod_cli = StringField()
    destinatario = StringField()
    volume = StringField()
    ocorrencia = TextAreaField()
    vendedor = SelectField(coerce=str, choices=['TODOS','000685 ALEX','000686 LUANA','000697 TAIRO AUGUSTO B','000502 CLEBER','000641 LUCIA', '000671 MARLEI', '000508 JEANY','000595 GUALTER'])
    transportadora = SelectField(coerce=str, choices=['TODOS','INTECOM','TJB','TECMAR','4a', 'pacifico','circulo','mosca','total minas','translovato','evivdencia','mira','transpaese'])
    data_de = DateField()
    data_ate = DateField()



@app.route('/teste', methods=['GET','POST'])
def add_ocorrencia():
    title = 'pagina teste'
    if request.method == 'POST':
        insert_text = request.form['name']
        # nf = request.form['id']
        print(insert_text)

        # send_info = f"update base_tracking set obs = " \
        #             f"concat(obs, {insert_text}) where doc = {} "
        #
        # cursor.execute(send_info)
        # updated_info = cursor.fetchall()


        return insert_text
    else:
        return render_template('add_ocorrencia.html')


@app.route('/tracking', methods=['GET', 'POST']) # configura a pagina as informações da pagina tracking.html
def tracking():
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
    ocorrencia = Teste()
    ocorrencia = ocorrencia.ocorrencia

    # configura as entradas dos botoes da pagina tracking para evitar o erro na requisicao do mysql
    # AJUSTA CAMPOS DA TELA PRINCIPAL, CASO O USUARIO NAO ENTRE NENHUMA OPCAO

    if empresa.data == 'TODOS':  # ok
        empresa.data = ''
    else:
        empresa.data = f'{empresa.data}'

    if uf.data == 'TODOS':  # ok
        uf.data = ''
    else:
        uf.data = f'{uf.data}'

    if agend.data == 'TODOS': # ok
        agend.data = ''
    else:
        agend.data = f'{agend.data}'

    if danfe.data == '': # ok
        danfe.data = ''
    else:
        danfe.data = f'{danfe.data}'

    if pedido.data == '':
        pedido.data = ''
    else:
        pedido.data = f'{pedido.data}'

    if cod_cli.data == '':
        cod_cli.data = ''
    else:
        cod_cli.data = f'{cod_cli.data}'

    if destinatario.data == '':
        destinatario.data = ''
    else:
        destinatario.data = f'{destinatario.data}'

    if regiao.data == 'TODOS': # ok
        regiao.data = ''
    else:
        regiao.data = f"{regiao.data}"

    if vendedor.data == 'TODOS':
        vendedor.data = ''
    else:
        vendedor.data = f'{vendedor.data}'

    if macro_canal.data == 'TODOS':
        macro_canal.data = ''
    else:
        macro_canal.data = f'{macro_canal.data}'

    if transportadora.data == 'TODOS':
        transportadora.data = ''
    else:
        transportadora.data = f'{transportadora.data}'

    if status.data == 'TODOS':
        status.data = 'false'
    else:
        status.data = f'"{status.data}"'

    if data_ate.data == None:
        data_ate.data = date.today()
    else:
        pass
        # print('verificar')
    if data_de.data == None:
        data_de.data = data_ate.data - timedelta(30)

    empresa.data = empresa.data.replace('None', '')
    danfe.data = danfe.data.replace('None', '')
    pedido.data = pedido.data.replace('None', '')
    agend.data = agend.data.replace('None', '')
    vendedor.data = vendedor.data.replace('None', '')
    regiao.data = regiao.data.replace('None', '')
    cod_cli.data = cod_cli.data.replace('None', '')
    destinatario.data = destinatario.data.replace('None', '')
    danfe.data = danfe.data.replace('"', '')
    danfe.data = danfe.data.replace('None', '')
    danfe.data = danfe.data.replace('is true', '')
    danfe.data = danfe.data.replace('=', '')
    pedido.data = pedido.data.replace('"', '')
    pedido.data = pedido.data.replace('None', '')
    pedido.data = pedido.data.replace('=', '')
    cod_cli.data = cod_cli.data.replace('"', '')
    cod_cli.data = cod_cli.data.replace("'", '')
    cod_cli.data = cod_cli.data.replace('None', '')
    cod_cli.data = cod_cli.data.replace('=', '')
    cod_cli.data = cod_cli.data.replace('0', '')
    destinatario.data = destinatario.data.replace('"', '')
    destinatario.data = destinatario.data.replace('None', '')
    regiao.data = regiao.data.replace('"', '')
    regiao.data = regiao.data.replace('None', '')
    agend.data = agend.data.replace('"', '')
    agend.data = agend.data.replace('None', '')
    vendedor.data = vendedor.data.replace('"', '')
    vendedor.data = vendedor.data.replace('None', '')

    # query da tabela principal
    query = f"select * from base_tracking where distr like '%{empresa.data}%' and " \
            f"pedido like '%{pedido.data}%' and " \
            f"doc like '%{danfe.data}%' and " \
            f"agend like '%{agend.data}%' and " \
            f"uf like '%{uf.data}%' and " \
            f"transp like '%{transportadora.data}%' and " \
            f"macro_can like '%{macro_canal.data}%' and " \
            f"vend like '%{vendedor.data}%' and " \
            f"nome_regiao like '%{regiao.data}%' and " \
            f"cliente like '%{cod_cli.data}%' and " \
            f"destinatário like '%{destinatario.data}%'and " \
            f"dt_nf between '{data_de.data}' and '{data_ate.data}'"

    cursor.execute(query)
    result = cursor.fetchall()
    hoje = date.today() # data atual

    def analisa_prazo():
        # INICIALIZA AS VARIAVEIS UTILIZADAS NO RESUMO SUPERIOR
        d4 = 0
        d3 = 0
        d2 = 0
        d1 = 0
        d0 = 0
        em_atraso = 0
        cont_entregue = 0
        cont_em_aberto = 0
        cont_dev = 0
        cont_s_def_agenda = 0
        cont_agendado = 0

        # variaveis do painel de resumo

        cont_doc_agnd = 0
        cont_doc_s_dt_agnd = 0
        cont_doc_reagnd = 0
        cont_doc_transit = 0
        cont_doc_ent = 0
        cont_doc_dev = 0

        soma_vol_doc_agnd = 0
        soma_vol_s_dt_agnd = 0
        soma_vol_reagnd = 0
        soma_vol_transit = 0
        soma_vol_ent = 0
        soma_vol_dev = 0

        soma_vlr_doc_agnd = 0
        soma_vlr_s_dt_agnd = 0
        soma_vlr_reagnd = 0
        soma_vlr_transit = 0
        soma_vlr_ent = 0
        soma_vlr_dev = 0
        perc_vlr_transit = 0
        perc_vlr_dev = 0
        perc_vlr_s_dt_agnd = 0
        perc_vlr_agnd = 0
        perc_vlr_reagnd = 0
        perc_vlr_entregue = 0
        otd = 0
        cont_no_prazo = 0
        cont_fora_prazo = 0

        for i in result:
            prev_entrega = i[21] # i[21] ´> previsao de entrega
            tp_agend = i[22]

            dt_exp = i[19]
            dt_agenda = i[23]
            dt_reagenda = i[24]
            st_entrega = i[26] # ENTREGUE, EM TRANSITO, ETC
            prazo = i[27]


            # FORMATACAO DAS DATAS

            if prev_entrega == " " or prev_entrega == "":
                pass
            else:
                prev_entrega = datetime.strptime(prev_entrega, '%Y-%m-%d')  # converte para datetime
                prev_entrega = prev_entrega.date()

            if dt_reagenda == " " or dt_reagenda == "":
                pass
            else:
                dt_reagenda = datetime.strptime(dt_reagenda, '%Y-%m-%d')  # converte para datetime
                dt_reagenda = dt_reagenda.date()

            if dt_agenda == " " or dt_agenda == "":
                pass
            else:
                dt_agenda = datetime.strptime(dt_agenda, '%Y-%m-%d')  # converte para datetime
                dt_agenda = dt_agenda.date()

            # CONTAGEM RESUMO
            vlr_doc_total = 0
            if st_entrega == 'ENTREGUE':
                cont_doc_ent += 1
                soma_vol_ent += i[15]
                soma_vlr_ent += i[17]


            if st_entrega == 'EM TRÂNSITO':
                cont_doc_transit += 1
                soma_vol_transit += i[15]
                soma_vlr_transit += i[17]

            if st_entrega == 'REAGENDADO':
                cont_doc_reagnd += 1
                soma_vol_reagnd += i[15]
                soma_vlr_reagnd += i[17]

            if st_entrega == 'AGENDADO':
                cont_doc_agnd += 1
                soma_vol_doc_agnd += i[15]
                soma_vlr_doc_agnd += i[17]

            if st_entrega == 'SEM DEFINIÇÃO DE AGENDA':
                cont_doc_s_dt_agnd += 1
                soma_vol_s_dt_agnd += i[15]
                soma_vlr_s_dt_agnd += i[17]

            if st_entrega == 'DEVOLUÇÃO':
                cont_doc_dev += 1
                soma_vol_dev += i[15]
                soma_vlr_dev += i[17]

            vlr_doc_total += soma_vlr_dev
            vlr_doc_total = soma_vlr_s_dt_agnd
            vlr_doc_total += soma_vlr_ent
            vlr_doc_total += soma_vlr_doc_agnd
            vlr_doc_total += soma_vlr_reagnd
            vlr_doc_total += soma_vlr_transit

            try:
                perc_vlr_transit = (soma_vlr_transit/vlr_doc_total)*100
                perc_vlr_dev = (soma_vlr_dev/vlr_doc_total)*100
                perc_vlr_s_dt_agnd = (soma_vlr_s_dt_agnd/vlr_doc_total)*100
                perc_vlr_agnd = (soma_vlr_doc_agnd/vlr_doc_total)*100
                perc_vlr_reagnd = (soma_vlr_reagnd/vlr_doc_total)*100
                perc_vlr_entregue = (soma_vlr_ent/vlr_doc_total)*100

            except:
                pass
            # CONTAGEM GERAL

            if st_entrega == 'ENTREGUE':
                cont_entregue += 1
            if st_entrega == 'DEVOLUÇÃO':
                cont_dev += 1
            if st_entrega != 'DEVOLUÇÃO' and st_entrega != 'ENTREGUE':
                cont_em_aberto += 1
            if dt_exp != " " and st_entrega == 'SEM DEFINIÇÃO DE AGENDA':
                cont_s_def_agenda += 1
            if dt_exp != " " and st_entrega == 'AGENDADO':
                cont_agendado += 1

            # CONTAGEM DOS PRAZOS

            if st_entrega == 'ENTREGUE' and prazo == 'NO PRAZO':
                cont_no_prazo += 1
            if st_entrega == 'ENTREGUE' and prazo == 'FORA DO PRAZO':
                cont_fora_prazo += 1
            # teste
            try:

                otd = (cont_no_prazo/(cont_no_prazo+cont_fora_prazo))*100
            except:
                pass

            # PRAZO DE ENTREGAS NAO AGENDADAS OU AGENDADAS AINDA SEM DATA DE AGENDA
            if prev_entrega == "" or prev_entrega == " ":
                pass
            else:
                if st_entrega == "EM TRÂNSITO" or st_entrega == "SEM DEFINIÇÃO DE AGENDA":
                    a = wd.networkdays(hoje, prev_entrega, country='BR')


                    if a < 0:
                        em_atraso += 1
                    if a == 0:
                        d0 += 1
                    if a == 1:
                        d1 += 1
                    if a == 2:
                        d2 += 1
                    if a == 3:
                        d3 += 1
                    if a == 4:
                        d4 += 1

            # PRAZO DE ENTREGAS  AGENDADAS
            if dt_agenda == "" or dt_agenda == " ":
                pass
            else:

                if st_entrega == "AGENDADO":
                    a = wd.networkdays(hoje, dt_agenda, country='BR')

                    if a < 0:
                        em_atraso += 1
                    if a == 0:
                        d0 += 1
                    if a == 1:
                        d1 += 1
                    if a == 2:
                        d2 += 1
                    if a == 3:
                        d3 += 1
                    if a == 4:
                        d4 += 1

        return cont_doc_ent, cont_dev, cont_em_aberto, cont_s_def_agenda, cont_agendado, \
            d4, d3, d2, d1, d0, \
            em_atraso, cont_doc_agnd, cont_doc_s_dt_agnd, cont_doc_reagnd, cont_doc_transit, \
            cont_doc_ent, cont_doc_dev, soma_vol_doc_agnd, soma_vol_s_dt_agnd, soma_vol_reagnd, \
            soma_vol_transit, soma_vol_ent, soma_vol_dev, soma_vlr_doc_agnd, soma_vlr_s_dt_agnd, \
            soma_vlr_reagnd, soma_vlr_transit, soma_vlr_ent, soma_vlr_dev, perc_vlr_agnd, \
            perc_vlr_s_dt_agnd, perc_vlr_entregue, perc_vlr_reagnd, perc_vlr_transit, perc_vlr_dev, \
            otd
        # 0 A 4 / 5 A 9 / 10 A 14 / 15 A 19 / 20 A 24 / 25 A 29 / 30 A 34 / 35



    if form_teste.validate_on_submit():
        cursor.fetchall()
        cursor.close()
        cnx.close()


    return render_template("base_tracking.html",
                           relato=result,  # TABELA
                           analisa_prazo=analisa_prazo(),
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
                           data_ate=data_ate,
                           ocorrencia=ocorrencia)




@app.route('/dashboard', methods=['GET', 'POST'])
class Dash(FlaskForm):
    d_processa = SubmitField("Processa")
    d_empresa = SelectField(coerce=str, choices=['EXTREMA', 'ALHANDRA'])
    d_uf = SelectField(coerce=str,
                     choices=['TODOS', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA',
                              'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF'])

    d_regiao = SelectField(coerce=str, choices=['TODOS', '01 NORTE', '02 NORDESTE', '03 LESTE', '04 FARMA BRASIL', '05 SP/SUL ALIMENTAR DIRETO', '06 SP/SUL ALIMENTAR INDIRETO', '07 CENTRO OESTE'])
    d_agend = SelectField(coerce=str, choices=['TODOS', 'S', 'N'])
    d_macro_canal = SelectField(coerce=str, choices=['TODOS', 'ATACADO', 'CASH CARY', 'DEMAIS CANAIS', 'DISTRIBUIDOR PARCEIRO', 'FARMA', 'VAREJO'])
    d_vendedor = SelectField(coerce=str, choices=['TODOS','000685 ALEX','000686 LUANA','000697 TAIRO AUGUSTO B','000502 CLEBER','000641 LUCIA', '000671 MARLEI', '000508 JEANY','000595 GUALTER'])
    d_transportadora = SelectField(coerce=str, choices=['TODOS','INTECOM','TJB','TECMAR','4a', 'pacifico','circulo','mosca','total minas','translovato','evivdencia','mira','transpaese'])
    d_mes_nf = SelectField(coerce=str, choices=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'])
    d_mes_ind = SelectField(coerce=str, choices=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'])



    @app.route('/dashboard', methods=['GET', 'POST'])
    # BARRA DE PESQUISA
    def dashboard():
        d_processa = Dash()
        d_processa = d_processa.d_processa
        d_empresa = Dash()
        d_empresa = d_empresa.d_empresa
        d_uf = Dash()
        d_uf = d_uf.d_uf
        d_regiao = Dash()
        d_regiao = d_regiao.d_regiao
        d_agend = Dash()
        d_agend = d_agend.d_agend
        d_macro_canal = Dash()
        d_macro_canal = d_macro_canal.d_macro_canal
        d_vendedor = Dash()
        d_vendedor = d_vendedor.d_vendedor
        d_transportadora = Dash()
        d_transportadora = d_transportadora.d_transportadora
        d_mes_nf = Dash()
        d_mes_nf = d_mes_nf.d_mes_nf
        d_mes_ind = Dash()
        d_mes_ind = d_mes_ind.d_mes_ind


        # GRÁFICOS
        # PARA INSERIR NOVOS GRAFICOS:
        # 1 -
        def dados_dash():

            query_dash = 'select * from base_tracking'
            cursor.execute(query_dash)
            result_dash = cursor.fetchall()

            """
            # if d_processa.validate_on_submit():
            #     cursor.fetchall()
            #     cursor.close()
            #     cnx.close()

            # relaciona os itens de:

            # nome_regiao [5]
            # transp [6]
            # destinatario [10]
            # municipio [11]
            # uf [12]
            # macro_can [13]
            # curva [14]
            # volume [15]
            # peso_bruto [16]
            # val_doc [17]
            # agend [22]
            # status [26]
            # prazo [27]
            """

            canal = []
            uf = []
            transp = []
            regiao = []

            vol_uf = 0
            val_uf = 0
            peso_uf = 0

            for i in result_dash:
                if i[5] not in regiao:
                    regiao.append(i[5])
                else:
                    pass


            for i in result_dash:
                if i[12] not in uf:
                    uf.append(i[12])
                else:
                    pass

            g1_uf = []
            g1_num = []
            for a in uf:
                # baixa o somatorio do volume
                vol_uf = f'select sum(volume) from base_tracking where uf = "{a}"'
                g1_uf.append(a) # adicicona a uf à g1_uf
                cursor.execute(vol_uf)
                vol_uf = cursor.fetchall()
                # extrai o valor da lista e da tupla
                vol_uf = vol_uf[0][0] # acessa o primeiro item da lista, em seguida, o primeiro item da tupla
                vol_uf = int(vol_uf)
                # inclui o valor à lista
                g1_num.append(vol_uf)

            g2_regiao = []
            g2_num = []
            for i in regiao:
                vol_regiao =  f'select sum(volume) from base_tracking where nome_regiao = "{i}"'
                g2_regiao.append(i)
                cursor.execute(vol_regiao)
                vol_regiao = cursor.fetchall()
                vol_regiao = vol_regiao[0][0]
                vol_regiao = int(vol_regiao)
                g2_num.append(vol_regiao)


                # g2_regiao = ['junho', 'julho', 'agosto', 'setembro', 'outubro']
                # g2_num = [1, 5, 2, 7, 4]

            return g1_uf, g1_num, g2_regiao, g2_num
            # nfs emitidas mes / qtd / valor_nf
            # nfs entregues no prazo / fora do prazo / mes de entrega

        def graf1():
            g1_uf, g1_num, g2_regiao, g2_num = dados_dash()

            # otd = g1_num
            axis_x = []
            axis_y = []
            for i in g1_uf:
                axis_x.append(i)
            for i in g1_num:
                axis_y.append(i)

            titulo = 'VOL X UF'
            graf1 = px.bar(x=axis_x, y=axis_y, title=titulo)
            graf1 = graf1.to_html(full_html=False)
            return graf1

        def graf2():
            g1_uf, g1_num, g2_regiao, g2_num = dados_dash()

            axis_x = []
            axis_y = []
            for a in g2_regiao:
                axis_x.append(a)
            for a in g2_num:
                axis_y.append(a)
            titulo = 'VOL x REGIAO'
            graf2 = px.bar(x=axis_x, y=axis_y, title=titulo)
            graf2 = graf2.to_html(full_html=False)
            return graf2


        return render_template('dashboard.html', d_processa=d_processa, d_empresa=d_empresa,d_uf=d_uf, d_regiao=d_regiao, d_agend=d_agend, d_macro_canal=d_macro_canal, d_vendedor=d_vendedor, d_transportadora=d_transportadora, d_mes_nf=d_mes_nf,d_mes_ind=d_mes_ind, graf1=graf1(), graf2=graf2() )




if __name__ == "__main__":
    # app.run(HOST, PORT, DEBUG)
    app.run(debug=True)
