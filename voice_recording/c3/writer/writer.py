from loguru import logger
from boto3 import Session


from voice_recording.settings import Settings

class Writer:

    def __init__(self, config: Settings):
        self._api_key = config.api_key.get_secret_value()
        self._secret_key = config.secret_key.get_secret_value()
        self._endpoint_url = config.endpoint_url
        self._bucket = config.bucket

        self._session = None


    def __enter__(self):
        session = Session().client(
            's3',
            aws_access_key_id=self._api_key,
            aws_secret_access_key=self._secret_key,
            endpoint_url=self._endpoint_url,
        )
        self._session = session
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            logger.error(f'Было вызвано исключение {exc_type} {exc_val} {exc_tb}')
            raise exc_val


    def write_frame(self, data: bytes):
        self._session.put_object(
            Bucket=self._bucket,
            Key='test.mp4',
            Body=data,
        )



