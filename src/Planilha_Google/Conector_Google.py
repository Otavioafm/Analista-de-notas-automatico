import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging

def conectar_planilhas():
    try:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        scope = ['', '']
        json_path = os.path.join('src','Planilha_Google', 'Jason', 'Conector_Google.json')

        creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
        client = gspread.authorize(creds)

        planilhas = client.openall() 
        logging.info('Conectado às planilhas com sucesso.')
        return planilhas

    except Exception as e:
        logging.error(f'Erro ao conectar às planilhas: {e}')
        return None
