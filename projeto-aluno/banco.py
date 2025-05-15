import oracledb

def obter_conexao():
    try:
        conexao = oracledb.connect(
            user='rm561178',
            password='200905',
            dsn='oracle.fiap.com.br/orcl'
        )
        print(f'Conectado com o banco de dados! {conexao.version}')

        return conexao
    
    except oracledb.DatabaseError as e:
        erro = e.args
        print(f'Erro ao conectar com o banco de dados: {erro.code} - {erro.message}')
        return None
    
def inserir_professor(nome, pf, senha):
    conexao = obter_conexao()
    if conexao is None:
        print("Falha ao obter conexão com banco de dados.")
        return
    
    try:
        with conexao.cursor() as cur:
            pf = pf.lower()

            cur.execute("SELECT COUNT(*) FROM t_professor WHERE LOWER(pf) = :1", [pf])
            result = cur.fetchone()

            if result[0] > 0:
                print("Erro: o PF fornecido já existe. Tente fazer login.")
                return
            
            id_professor = cur.var(oracledb.NUMBER)
            
            sql = """
                INSERT INTO t_professor (nome, pf, senha) VALUES (:1, :2, :3) RETURNING id INTO :4
            """

            cur.execute(sql, [nome, pf, senha, id_professor])
            conexao.commit()
            print("Professor cadastrado com sucesso!")
            return int(id_professor.getvalue())
        
    except oracledb.IntegrityError as e:
        print(f'Errode integridade: {e}')
    except oracledb.DatabaseError as e:
        print(f'Erro de conexão com o banco de dados: {e}')
    finally:
        if conexao:
            conexao.close()

