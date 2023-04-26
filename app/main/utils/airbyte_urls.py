class URLs:
    '''
    Clase que contiene los endpoints de la Config API de Airbyte.

    Más información sobre la API: https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
    '''
    BASE_URL = 'https://senz-airbyte.kemok.io/api/v1'

    # INICAR SYNC
    START_SYNC = BASE_URL + '/connections/sync'

    # JOBS
    GET_JOB = BASE_URL + '/jobs/get'
    RECENT_JOBS = BASE_URL + '/jobs/list'
    GET_PARTIAL_JOB = BASE_URL + '/jobs/get_light'
    LAST_REPLICATION_JOB = BASE_URL + '/jobs/get_last_replication_job'
    CANCEL_JOB = BASE_URL + '/jobs/cancel'