import sqlite3
import time

# A lista de "notas" que o sistema vai processar instantaneamente
notas_para_processar = [
    {"item": "Tela iPhone 13", "qtd": 45},
    {"item": "Bateria S22", "qtd": 30},
    {"item": "Cabo Lightning", "qtd": 100},
    {"item": "Tela iPhone 13", "qtd": 10}, 
    {"item": "Bateria S22", "qtd": 5},
    {"item": "Carregador 20W", "qtd": 50},
]

def processar_automacao():
    print("\n🚀 [SISTEMA CATATECH] Iniciando Automação de Processamento...")
    print("----------------------------------------------------------")
    
    conn = sqlite3.connect('estoque_real.db')
    cursor = conn.cursor()
    
    # Criar a tabela de estoque
    cursor.execute('CREATE TABLE IF NOT EXISTS estoque (item TEXT PRIMARY KEY, qtd INTEGER)')
    
    tempo_inicial = time.time()
    
    # O loop que faz o trabalho de "horas" em segundos
    for nota in notas_para_processar:
        item = nota['item']
        qtd_adicional = nota['qtd']
        
        # Se o item já existe, soma. Se não, insere novo.
        cursor.execute('''
            INSERT INTO estoque (item, qtd) 
            VALUES (?, ?) 
            ON CONFLICT(item) DO UPDATE SET qtd = qtd + ?
        ''', (item, qtd_adicional, qtd_adicional))
        
        print(f"📦 Importando Nota Fiscal: {item.ljust(15)} | +{qtd_adicional} unidades")
        time.sleep(0.3) # Simulação visual do processamento

    conn.commit()
    
    # Gerando o relatório consolidado
    print("\n--- RELATÓRIO FINAL DE ESTOQUE ATUALIZADO ---")
    cursor.execute("SELECT * FROM estoque")
    for linha in cursor.fetchall():
        print(f"Item: {linha[0].ljust(15)} | Total em Estoque: {linha[1]}")
    
    conn.close()
    
    tempo_final = time.time()
    print("----------------------------------------------------------")
    print(f"✅ Automação Concluída em {round(tempo_final - tempo_inicial, 2)} segundos.")
    print("O que levaria 4 horas de conferência manual foi feito agora.")

if __name__ == "__main__":
    processar_automacao()