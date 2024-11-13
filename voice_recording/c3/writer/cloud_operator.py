from boto3 import Session

from voice_recording.c3.writer.base import Operator, log_decorator, BaseOverridesOperator
from voice_recording.settings import Settings, S3Settings, LocalSettings


class S3Operator(Operator, BaseOverridesOperator):

    def __init__(self, settings: S3Settings):
        super().__init__(settings)
        self._session = Session().client(
            's3',
            aws_access_key_id=self.api_key,
            aws_secret_access_key=self.secret_key,
            endpoint_url=self.endpoint_url,
        )

    @log_decorator
    def write_bytes(self, file_name: str, data: bytes) -> str:
        request = self._session.put_object(
            Bucket=self.bucket,
            Key=file_name,
            Body=data,
        )

        return request['Key']

    @log_decorator
    def read_bytes(self, file_name: str) -> bytes:
        request = self._session.get_object(
            Bucket=self.bucket,
            Key=file_name,
        )
        return request['Body']

