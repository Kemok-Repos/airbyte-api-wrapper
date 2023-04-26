import requests
import json
from base64 import b64encode
from model import SyncJobResponse, Job
from utils.airbyte_urls import URLs
from utils.errors import AirbyteAPIError

class AirbyteWrapper:
    '''Clase que maneja las conexiones con la Config API de Airbyte'''

    def __init__(self, airbyte_user: str = None, airbyte_password: str = None):
        self.auth_headers = self.get_airbyte_headers(airbyte_user, airbyte_password)

    def get_airbyte_headers(self, airbyte_user: str, airbyte_password: str):
        ''''Realiza el parsing del user:password de airbyte para generar el auth token'''
        if not airbyte_user or not airbyte_password:
            raise Exception('Usuario y contraseña de Airbyte son requeridos')

        auth_header = 'Basic ' + str(b64encode(bytes(airbyte_user + ':' + airbyte_password, 'utf-8')), 'utf-8')
        headers = {
            'Authorization': auth_header,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        return headers

    def start_sync(self, connection_id: str = None):
        '''Inicia un nuevo sync para la conexión indicada'''
        url = URLs.START_SYNC
        body = {
            'connectionId': connection_id
        }

        try:
            response = requests.post(url, headers=self.auth_headers, data=json.dumps(body))
            response.raise_for_status()
            res_obj = json.loads(response.text)
            parsed_sync_job = SyncJobResponse.from_dict(res_obj)
        except requests.exceptions.HTTPError as err:
            raise AirbyteAPIError(f"Error iniciando Airbyte sync: {err}") from err
        
        return parsed_sync_job

    def get_job(self, job_id: int = None):
        '''Retorna la información de 1 job dado su ID'''
        url = URLs.GET_JOB
        body = {
            'id': job_id
        }

        try:
            response = requests.post(url, headers=self.auth_headers, data=json.dumps(body))
            response.raise_for_status()
            res_obj = json.loads(response.text)
            parsed_job = SyncJobResponse.from_dict(res_obj)
        except requests.exceptions.HTTPError as err:
            raise AirbyteAPIError(f"Error recuperando info del job: {err}") from err
        
        return parsed_job
    
    def get_partial_job(self, job_id: int = None):
        '''Retorna la información de 1 job (excluyendo attempts info y logs) dado su ID '''
        url = URLs.GET_PARTIAL_JOB
        body = {
            'id': job_id
        }

        try:
            response = requests.post(url, headers=self.auth_headers, data=json.dumps(body))
            response.raise_for_status()
            res_obj = json.loads(response.text)
            parsed_job = Job.parse_obj(res_obj.get('job', None))
        except requests.exceptions.HTTPError as err:
            raise AirbyteAPIError(f"Error recuperando info del job: {err}") from err
        
        return parsed_job
    
    def get_last_replication_job(self, connection_id: str = None):
        '''Retorna la información del último job realizado para una conexión específica dado su ID'''
        url = URLs.LAST_REPLICATION_JOB
        body = {
            'connectionId': connection_id
        }

        try:
            response = requests.post(url, headers=self.auth_headers, data=json.dumps(body))
            response.raise_for_status()
            res_obj = json.loads(response.text)
            parsed_job = Job.parse_obj(res_obj.get('job', None))
        except requests.exceptions.HTTPError as err:
            raise AirbyteAPIError(f"Error recuperando último job: {err}") from err
        
        return parsed_job
