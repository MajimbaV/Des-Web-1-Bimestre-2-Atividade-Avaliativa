#Importando tudo do módulo "model"
from model.model_1 import *

#Classes associativas:

#Classe JogoDev

class JogoDev(Tabela):
    def __init__(self) -> None :
        super().__init__()
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS JogoDev(
            id_game INTEGER,
            id_developer INTEGER,
            PRIMARY KEY (id_game, id_developer),
            FOREIGN KEY (id_game) REFERENCES Jogos(id_jogo) ON DELETE CASCADE,
            FOREIGN KEY (id_developer) REFERENCES Desenvolvedores(id_dev) ON DELETE CASCADE
            );
        """)
        conn.close()
        
    def add_Jogo_Dev(self, id_game: int, id_developer: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
                INSERT INTO JogoDev(id_game, id_developer)
                VALUES({id_game}, {id_developer});
                """)
        self.conn.commit()
        self.conn.close()
            
    def select_associacoesJD(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM JogoDev;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_game': registro[0],
                'id_dev': registro[1]
            })
        self.conn.close()
        return registros
    
    def select_registrosJD(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT j.*, d.*
        FROM Jogos AS j
        INNER JOIN JogoDev AS jd ON j.id_jogo = jd.id_game
        INNER JOIN Desenvolvedores AS d ON d.id_dev = jd.id_developer;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                
                "id_jogo": registro[0],
                "nome_jogo": registro[1],
                "descricao": registro[2],
                "D_lancamento": registro[3],
                "C_etaria": registro[4],
                "precoR$": registro[5],
                "quantidade_players": registro[6],
                "id_dev": registro[7],
                "nome_dev": registro[8]
            })
        self.conn.close()
        return registros
#Classe JogoPlata

class JogoPlata(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS JogoPlata(
            id_game INTEGER,
            id_plataforma INTEGER,
            PRIMARY KEY (id_game, id_plataforma),
            FOREIGN KEY (id_game) REFERENCES Jogos(id_jogo) ON DELETE CASCADE,
            FOREIGN KEY (id_plataforma) REFERENCES Plataformas(id_plata) ON DELETE CASCADE
            );
        """)
        self.conn.close()
        
    def add_Jogo_Plata(self, id_game: int, id_plataforma) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
                INSERT INTO JogoPlata(id_game, id_plataforma)
                VALUES({id_game}, {id_plataforma});
                """)
        self.conn.commit()
        self.conn.close()
            
    def select_associacoesJP(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM JogoPlata;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_game': registro[0],
                'id_plataforma': registro[1]
            })
        self.conn.close()
        return registros
    
    def select_registrosJP(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT j.*, p.*
        FROM Jogos AS j
        INNER JOIN JogoPlata AS jp ON j.id_jogo = jp.id_game
        INNER JOIN Plataformas AS p ON p.id_plata = jp.id_plataforma;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                
                "id_jogo": registro[0],
                "nome_jogo": registro[1],
                "descricao": registro[2],
                "D_lancamento": registro[3],
                "C_etaria": registro[4],
                "precoR$": registro[5],
                "quantidade_players": registro[6],
                "id_plata": registro[7],
                "nome_plata": registro[8],
                "fabricante": registro[9]
            })
        self.conn.close()
        return registros
    
#Classe JogoGen

class JogoGen(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS JogoGen(
            id_game INTEGER,
            id_genero INTEGER,
            PRIMARY KEY (id_game, id_genero),
            FOREIGN KEY (id_game) REFERENCES Jogos(id_jogo) ON DELETE CASCADE,
            FOREIGN KEY (id_genero) REFERENCES Generos(id_gen) ON DELETE CASCADE
            );
        """)
        self.conn.close()
    
    def add_Jogo_Gen(self, id_game: int, id_genero: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
                INSERT INTO JogoGen(id_game, id_genero)
                VALUES({id_game}, {id_genero});
                """)
        self.conn.commit()
        self.conn.close()
    
    def select_associacoesJGEN(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM JogoGen;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id_game': registro[0],
                'id_genero': registro[1]
            })
        self.conn.close()
        return registros
    
    def select_registrosJGEN(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        SELECT j.*, g.*
        FROM Jogos AS j
        INNER JOIN JogoGen AS jgen ON j.id_jogo = jgen.id_game
        INNER JOIN Generos AS g ON g.id_gen = jgen.id_genero;
        """)
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                
                "id_jogo": registro[0],
                "nome_jogo": registro[1],
                "descricao": registro[2],
                "D_lancamento": registro[3],
                "C_etaria": registro[4],
                "precoR$": registro[5],
                "quantidade_players": registro[6],
                "id_gen": registro[7],
                "nome_gen": registro[8]
            })
        self.conn.close()
        return registros


#Objetos de cada tabela:

Obj_JDEV = JogoDev()
Obj_JPLATA = JogoPlata()
Obj_JGEN = JogoGen()

#Inserindo dados (relações) em cada associação:

#Obj_JDEV.add_Jogo_Dev(1,2)
# Obj_JPLATA.add_Jogo_Plata(1,1)
# Obj_JGEN.add_Jogo_Gen(1,1)

#Selecionando os dados de cada associação:

# print(Obj_JDEV.select_associacoesJD())
# print(Obj_JPLATA.select_associacoesJP())
# print(Obj_JGEN.select_associacoesJGEN())

#Selecionando os registros (JOIN) de cada associação:

# print(Obj_JDEV.select_registrosJD())
# print(Obj_JPLATA.select_registrosJP())
# print(Obj_JGEN.select_registrosJGEN())