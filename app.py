from flask import Flask, request, render_template, redirect

from model.model_2 import *

app = Flask(__name__)

#Função p/ selecionar um item da array de dicionários
def pickItem(lista: list, id: int) -> dict:
    for i in lista:
        if i['id'] == id:
            return i
    raise Exception("Item Não Encontrado!!")

#Função p/ registrar as relações entre o Jogo registrado e todas as outras tabelas
def registrar_relações(idDev: int, idPlata: int, idGen: int):
    last_gameID = Obj_Jogo.select_games()[-1]['id']
    Obj_JDEV.add_Jogo_Dev(last_gameID, idDev)
    Obj_JGEN.add_Jogo_Gen(last_gameID, idGen)
    Obj_JPLATA.add_Jogo_Plata(last_gameID, idPlata)

#Página Índice Inicial

@app.route('/')
def index():
    return render_template('index.html')


#Páginas da Entidade Jogos

#View da Tabela Jogos
@app.route('/jogos')
def list_games():
    all_games = Obj_Jogo.select_games()
    Jdevs = Obj_JDEV.select_registrosJD()
    Jgens = Obj_JGEN.select_registrosJGEN()
    Jplats = Obj_JPLATA.select_registrosJP()
    return render_template('viewjogos.html', jogos=all_games, Jdevs=Jdevs, Jgens=Jgens, Jplats=Jplats)

#Adcionar novo Jogo
@app.route('/jogos/novo', methods=['GET', 'POST'])
def add_game():
    devs = Obj_Dev.select_devs()
    plats = Obj_Plata.select_plata()
    gens = Obj_Gen.select_gen()
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Jogo.add_game(data['nome'], data['desc'], data['D_L'], data['C_E'], float(data['preco']), int(data['quant_player']))
        registrar_relações(int(data['dev']), int(data['plat']), int(data['gen']))
        return redirect('/jogos')
    return render_template('formjogos.html', title="Adicionar Novo Jogo", jogo=None, devs=devs, plataformas=plats, generos=gens)

#Editar um Jogo Já Existente
@app.route('/jogos/editar/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    devs = Obj_Dev.select_devs()
    plats = Obj_Plata.select_plata()
    gens = Obj_Gen.select_gen()
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Jogo.update_game(id, data['nome'], data['desc'], data['D_L'], data['C_E'], float(data['preco']), int(data['quant_player']))
        return redirect('/jogos')
    game = pickItem(Obj_Jogo.select_games(), id)
    return render_template('formjogos.html', title="Editar Jogo Registrado", jogo=game, devs=devs, plataformas=plats, generos=gens)
    
#Deletar um Jogo da Tabela
@app.route('/jogos/remover/<int:id>', methods=['GET'])
def delete_game(id):
        Obj_Jogo.del_game(id)
        return redirect('/jogos')


#Páginas da Entidade Desenvolvedores

#View da Tabela Desenvolvedores
@app.route('/devs')
def list_devs():
    all_devs = Obj_Dev.select_devs()
    return render_template('viewdevs.html', devs=all_devs)

#Adcionar novo Desenvolvedor
@app.route('/devs/novo', methods=['GET', 'POST'])
def add_dev():
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Dev.add_dev(data['nome'])
        return redirect('/devs')
    return render_template('formdevs.html', title="Adicionar Novo Desenvolvedor", dev=None)

#Editar um Desenvolvedor já existente
@app.route('/devs/editar/<int:id>', methods=['GET', 'POST'])
def edit_dev(id):
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Dev.update_dev(id, data['nome'])
        return redirect('/devs')
    dev = pickItem(Obj_Dev.select_devs(), id)
    return render_template('formdevs.html', title="Editar um Desenvolvedor Registrado", dev=dev)
    
#Deletar um Desenvolvedor da Tabela
@app.route('/devs/remover/<int:id>', methods=['GET'])
def delete_dev(id):
        Obj_Dev.del_dev(id)
        return redirect('/devs')

    
#Páginas da Entidade Plataformas

#View da Tabela Plataformas
@app.route('/plataformas')
def list_plats():
    plats = Obj_Plata.select_plata()
    return render_template('viewplata.html', plataformas = plats)

#Adcionar nova Plataforma
@app.route('/plataformas/novo', methods=['GET', 'POST'])
def add_plat():
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Plata.add_plata(data['nome'], data['fabricante'])
        return redirect('/plataformas')
    return render_template('formplata.html', title="Adicionar Nova Plataforma", plataforma=None)

#Editar uma Plataforma já existente
@app.route('/plataformas/editar/<int:id>', methods=['GET', 'POST'])
def edit_plat(id):
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Plata.update_plata(id, data['nome'], data['fabricante'])
        return redirect('/plataformas')
    plataforma = pickItem(Obj_Plata.select_plata(), id)
    return render_template('formplata.html', title="Editar uma Plataforma Registrada", plataforma=plataforma)
    
#Deletar uma Plataforma da Tabela
@app.route('/plataformas/remover/<int:id>', methods=['GET'])
def delete_plat(id):
        Obj_Plata.del_plata(id)
        return redirect('/plataformas')
    
#Páginas da Entidade Gêneros

#View da Tabela Gêneros
@app.route('/generos')
def list_gens():
    gens = Obj_Gen.select_gen()
    return render_template('viewgens.html', generos = gens)

#Adcionar novo Gênero
@app.route('/generos/novo', methods=['GET', 'POST'])
def add_gen():
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Gen.add_gen(data['nome'])
        return redirect('/generos')
    return render_template('formgens.html', title="Adicionar Novo Gênero", genero=None)

#Editar um Gênero já existente
@app.route('/generos/editar/<int:id>', methods=['GET', 'POST'])
def edit_gen(id):
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Gen.update_gen(id, data['nome'])
        return redirect('/generos')
    gen = pickItem(Obj_Gen.select_gen(), id)
    return render_template('formgens.html', title="Editar um Gênero Registrado", genero=gen)
    
#Deletar um Jogo da Tabela
@app.route('/generos/remover/<int:id>', methods=['GET'])
def delete_gen(id):
        Obj_Gen.del_gen(id)
        return redirect('/generos')
    

if __name__ == "__main__":
    app.run()
