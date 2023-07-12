# Code generated by Lark OpenAPI.

from typing import *
from typing import IO
from lark_oapi.core.construct import init
from .speech import Speech
from .file_config import FileConfig


class FileRecognizeSpeechRequestBody(object):
    _types = {
        "speech": Speech,
        "config": FileConfig,
    }

    def __init__(self, d):
        self.speech: Optional[Speech] = None
        self.config: Optional[FileConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FileRecognizeSpeechRequestBodyBuilder":
        return FileRecognizeSpeechRequestBodyBuilder()


class FileRecognizeSpeechRequestBodyBuilder(object):
    def __init__(self, file_recognize_speech_request_body: FileRecognizeSpeechRequestBody = FileRecognizeSpeechRequestBody({})) -> None:
        self._file_recognize_speech_request_body: FileRecognizeSpeechRequestBody = file_recognize_speech_request_body
    
    def speech(self, speech: Speech) -> "FileRecognizeSpeechRequestBodyBuilder":
        self._file_recognize_speech_request_body.speech = speech
        return self
    
    def config(self, config: FileConfig) -> "FileRecognizeSpeechRequestBodyBuilder":
        self._file_recognize_speech_request_body.config = config
        return self
    
    def build(self) -> "FileRecognizeSpeechRequestBody":
        return self._file_recognize_speech_request_body