#Importando o módulo que fornece uma DB-API

import sqlite3

#Criando as classes:

#Classe Tabela (superclasse):

class Tabela:
    def __init__(self) -> None:
        self.module = sqlite3
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        


#Classe Jogos:

class Jogos(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Jogos(
            id_jogo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_jogo VARCHAR(60) NOT NULL,
            descricao VARCHAR(255) NOT NULL,
            D_lancamento VARCHAR(30) NOT NULL,
            C_etaria VARCHAR(30) NOT NULL,
            precoR$ REAL NOT NULL,
            quant_players INTEGER NOT NULL
            );
        """)
        self.conn.close()
        
    def add_game(self, nome: str, descricao: str, DL: str, CE: str, preco: float, quant_players: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Jogos(nome_jogo, descricao, D_lancamento, C_etaria, precoR$, quant_players)
        VALUES('{nome}','{descricao}', '{DL}', '{CE}', {preco}, {quant_players});
        """)
        self.conn.commit()
        self.conn.close()
        
    def select_games(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Jogos;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_jogo': registro[1],
                'descricao': registro[2],
                'data_lancamento': registro[3],
                'classificacao_etaria': registro[4],
                'precoR$': registro[5],
                'quantidade_players': registro[6]
            })
        self.conn.close()
        return registros
    
    def del_game(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Jogos WHERE id_jogo = {id};")
        self.conn.commit()
        self.conn.close()
        
    def update_game(self, id: int, nome: str, descricao: str, DL: str, CE: str, preco: float, quant_players: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Jogos SET nome_jogo = '{nome}', descricao = '{descricao}', D_lancamento = '{DL}', C_etaria = '{CE}', precoR$ = {preco}, quant_players =  {quant_players}
            WHERE  id_jogo = {id};
            """)
        self.conn.commit()
        self.conn.close()
        
    
#Classe Desenvolvedores:

class Desenvolvedores(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Desenvolvedores(
            id_dev INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_dev VARCHAR(30) NOT NULL
            );
        """)
        self.conn.close()
        
    def add_dev(self, nome: str) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Desenvolvedores(nome_dev)
        VALUES('{nome}');
        """)
        self.conn.commit()
        self.conn.close()
        
    def select_devs(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Desenvolvedores;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_dev': registro[1]
            })
        self.conn.close()
        return registros
    
    def del_dev(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor() 
        self.cursor.execute(f"DELETE FROM Desenvolvedores WHERE id_dev = {id};")
        self.conn.commit()
        self.conn.close()
    
    def update_dev(self, id: int, nome: str) -> None:
        conn = sqlite3.connect("meuDB.db")
        cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE Desenvolvedores SET nome_dev = '{nome}'
            WHERE  id_dev = {id};
            """)
        conn.commit()
        conn.close()

#Classe Plataformas:

class Plataformas(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Plataformas(
            id_plata INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_plata VARCHAR(30) NOT NULL,
            fabricante VARCHAR(30) NOT NULL
            );
        """)
        self.conn.close()
        
    def add_plata(self, nome: str, fabricante: str) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Plataformas(nome_plata, fabricante)
        VALUES('{nome}', '{fabricante}');
        """)
        self.conn.commit()
        self.conn.close()
        
    def select_plata(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Plataformas;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_plata': registro[1],
                'fabricante': registro[2]
            })
        self.conn.close()
        return registros
    
    def del_plata(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Plataformas WHERE id_plata = {id};")
        self.conn.commit()
        self.conn.close()
    
    def update_plata(self, id: int, nome: str, fabricante: str) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Plataformas SET nome_plata = '{nome}', fabricante = '{fabricante}'
            WHERE  id_plata = {id};
            """)
        self.conn.commit()
        self.conn.close()
        
#Classe Gêneros:

class Generos(Tabela):
    def __init__(self) -> None:
        super().__init__()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS Generos(
            id_gen INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome_gen VARCHAR(30) NOT NULL
            );
        """)
        self.conn.close()
        
    def add_gen(self, nome: str) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        INSERT INTO Generos(nome_gen)
        VALUES('{nome}');
        """)
        self.conn.commit()
        self.conn.close()
    
    def select_gen(self) -> list:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM Generos;")
        registros = []
        for registro in self.cursor.fetchall():
            registros.append({
                'id': registro[0],
                'nome_gen': registro[1]
            })
        self.conn.close()
        return registros
    
    def del_gen(self, id: int) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"DELETE FROM Generos WHERE id_gen = {id};")
        self.conn.commit()
        self.conn.close()
        
    def update_gen(self, id: int, nome: str) -> None:
        self.conn = self.module.connect("meuDB.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Generos SET nome_gen = '{nome}'
            WHERE  id_gen = {id};
            """)
        self.conn.commit()
        self.conn.close()
        

#Objetos de cada tabela:

Obj_Jogo = Jogos()
Obj_Dev = Desenvolvedores()
Obj_Plata = Plataformas()
Obj_Gen = Generos()

#Inserido dados em cada tabela:

# Obj_Jogo.add_game("SotC","Soliário","27/10/2005","TEEN",25,1)
# Obj_Dev.add_dev("Team Ico")
# Obj_Plata.add_plata("PS2", "SCE")
# Obj_Gen.add_gen("Ação e Aventura")

#Deletando registros em cada tabela:

# Obj_Jogo.del_game(2)
# Obj_Dev.del_dev(2)
# Obj_Plata.del_plata(2)
# Obj_Gen.del_gen(2)

#Atualizando os registros em cada tabela:

# Obj_Jogo.update_game(2, "ICO", "Amor na mão", "24/07/2001", "TEEN", 15, 1)
# Obj_Dev.update_dev(2, "Team ICO")
# Obj_Plata.update_plata(2, "PS3", "SCE")
# Obj_Gen.update_gen(2, "Puzzle")

#Selecionando registros em cada tabela:

# print(Obj_Jogo.select_games())
# print(Obj_Dev.select_devs())
# print(Obj_Plata.select_plata())
# print(Obj_Gen.select_gen())