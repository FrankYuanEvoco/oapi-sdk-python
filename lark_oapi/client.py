# Code generated by Lark OpenAPI.

from .api.acs.service import AcsService
from .api.admin.service import AdminService
from .api.application.service import ApplicationService
from .api.approval.service import ApprovalService
from .api.attendance.service import AttendanceService
from .api.auth.service import AuthService
from .api.authen.service import AuthenService
from .api.baike.service import BaikeService
from .api.bitable.service import BitableService
from .api.block.service import BlockService
from .api.calendar.service import CalendarService
from .api.contact.service import ContactService
from .api.corehr.service import CorehrService
from .api.document_ai.service import DocumentAiService
from .api.docx.service import DocxService
from .api.drive.service import DriveService
from .api.ehr.service import EhrService
from .api.event.service import EventService
from .api.gray_test_open_sg.service import GrayTestOpenSgService
from .api.helpdesk.service import HelpdeskService
from .api.hire.service import HireService
from .api.human_authentication.service import HumanAuthenticationService
from .api.im.service import ImService
from .api.lingo.service import LingoService
from .api.mail.service import MailService
from .api.mdm.service import MdmService
from .api.meeting_room.service import MeetingRoomService
from .api.okr.service import OkrService
from .api.optical_char_recognition.service import OpticalCharRecognitionService
from .api.passport.service import PassportService
from .api.personal_settings.service import PersonalSettingsService
from .api.report.service import ReportService
from .api.search.service import SearchService
from .api.security_and_compliance.service import SecurityAndComplianceService
from .api.sheets.service import SheetsService
from .api.speech_to_text.service import SpeechToTextService
from .api.task.service import TaskService
from .api.tenant.service import TenantService
from .api.translation.service import TranslationService
from .api.vc.service import VcService
from .api.verification.service import VerificationService
from .api.wiki.service import WikiService
from .api.workplace.service import WorkplaceService
from .core import logger, JSON
from .core.const import UTF_8, APPLICATION_JSON
from .core.http import Transport
from .core.model import *
from .core.token import TokenManager, verify
from .core.utils.files import Files


class Client(object):
    def __init__(self) -> None:
        self._config: Optional[Config] = None
        self.tenant: Optional[TenantService] = None
        self.translation: Optional[TranslationService] = None
        self.acs: Optional[AcsService] = None
        self.bitable: Optional[BitableService] = None
        self.contact: Optional[ContactService] = None
        self.human_authentication: Optional[HumanAuthenticationService] = None
        self.personal_settings: Optional[PersonalSettingsService] = None
        self.mdm: Optional[MdmService] = None
        self.verification: Optional[VerificationService] = None
        self.workplace: Optional[WorkplaceService] = None
        self.admin: Optional[AdminService] = None
        self.approval: Optional[ApprovalService] = None
        self.authen: Optional[AuthenService] = None
        self.ehr: Optional[EhrService] = None
        self.event: Optional[EventService] = None
        self.baike: Optional[BaikeService] = None
        self.document_ai: Optional[DocumentAiService] = None
        self.im: Optional[ImService] = None
        self.wiki: Optional[WikiService] = None
        self.application: Optional[ApplicationService] = None
        self.gray_test_open_sg: Optional[GrayTestOpenSgService] = None
        self.mail: Optional[MailService] = None
        self.passport: Optional[PassportService] = None
        self.search: Optional[SearchService] = None
        self.calendar: Optional[CalendarService] = None
        self.corehr: Optional[CorehrService] = None
        self.helpdesk: Optional[HelpdeskService] = None
        self.lingo: Optional[LingoService] = None
        self.sheets: Optional[SheetsService] = None
        self.meeting_room: Optional[MeetingRoomService] = None
        self.optical_char_recognition: Optional[OpticalCharRecognitionService] = None
        self.report: Optional[ReportService] = None
        self.task: Optional[TaskService] = None
        self.attendance: Optional[AttendanceService] = None
        self.hire: Optional[HireService] = None
        self.security_and_compliance: Optional[SecurityAndComplianceService] = None
        self.speech_to_text: Optional[SpeechToTextService] = None
        self.vc: Optional[VcService] = None
        self.auth: Optional[AuthService] = None
        self.block: Optional[BlockService] = None
        self.docx: Optional[DocxService] = None
        self.drive: Optional[DriveService] = None
        self.okr: Optional[OkrService] = None

    @staticmethod
    def builder() -> "ClientBuilder":
        return ClientBuilder()

    def request(self, request: BaseRequest, option: Optional[RequestOption] = None) -> BaseResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self._config, request, option)

        # 发起请求
        raw_resp = Transport.execute(self._config, request, option)

        # 返回结果
        resp = BaseResponse()
        content_type = raw_resp.headers.get(CONTENT_TYPE)
        if content_type is not None and content_type.startswith(APPLICATION_JSON):
            resp = JSON.unmarshal(str(raw_resp.content, UTF_8), BaseResponse)
        elif 200 <= raw_resp.status_code < 300:
            resp.code = 0
        resp.raw = raw_resp

        return resp

    async def arequest(self, request: BaseRequest, option: Optional[RequestOption] = None) -> BaseResponse:
        if option is None:
            option = RequestOption()

        # 鉴权、获取token
        verify(self._config, request, option)

        # 解析文件
        request.files = Files.extract_files(request.body)

        # 发起请求
        raw_resp = await Transport.aexecute(self._config, request, option)

        # 返回结果
        resp = BaseResponse()
        content_type = raw_resp.headers.get(CONTENT_TYPE)
        if content_type is not None and content_type.startswith(APPLICATION_JSON):
            resp = JSON.unmarshal(str(raw_resp.content, UTF_8), BaseResponse)
        elif 200 <= raw_resp.status_code < 300:
            resp.code = 0
        resp.raw = raw_resp

        return resp


class ClientBuilder(object):
    def __init__(self) -> None:
        self._config = Config()

    def app_id(self, app_id: str) -> "ClientBuilder":
        self._config.app_id = app_id
        return self

    def app_secret(self, app_secret: str) -> "ClientBuilder":
        self._config.app_secret = app_secret
        return self

    def domain(self, domain: str) -> "ClientBuilder":
        self._config.domain = domain
        return self

    def timeout(self, timeout: float) -> "ClientBuilder":
        self._config.timeout = timeout
        return self

    def app_type(self, app_type: AppType) -> "ClientBuilder":
        self._config.app_type = app_type
        return self

    def app_ticket(self, app_ticket: str) -> "ClientBuilder":
        self._config.app_ticket = app_ticket
        return self

    def enable_set_token(self, enable_set_token: bool) -> "ClientBuilder":
        self._config.enable_set_token = enable_set_token
        return self

    def cache(self, cache: ICache) -> "ClientBuilder":
        self._config.cache = cache
        return self

    def log_level(self, log_level: LogLevel) -> "ClientBuilder":
        self._config.log_level = log_level
        return self

    def build(self) -> Client:
        client: Client = Client()
        client._config = self._config

        # 初始化缓存
        self._init_cache()

        # 初始化日志
        self._init_logger()

        # 初始化 服务
        client.tenant = TenantService(self._config)
        client.translation = TranslationService(self._config)
        client.acs = AcsService(self._config)
        client.bitable = BitableService(self._config)
        client.contact = ContactService(self._config)
        client.human_authentication = HumanAuthenticationService(self._config)
        client.personal_settings = PersonalSettingsService(self._config)
        client.mdm = MdmService(self._config)
        client.verification = VerificationService(self._config)
        client.workplace = WorkplaceService(self._config)
        client.admin = AdminService(self._config)
        client.approval = ApprovalService(self._config)
        client.authen = AuthenService(self._config)
        client.ehr = EhrService(self._config)
        client.event = EventService(self._config)
        client.baike = BaikeService(self._config)
        client.document_ai = DocumentAiService(self._config)
        client.im = ImService(self._config)
        client.wiki = WikiService(self._config)
        client.application = ApplicationService(self._config)
        client.gray_test_open_sg = GrayTestOpenSgService(self._config)
        client.mail = MailService(self._config)
        client.passport = PassportService(self._config)
        client.search = SearchService(self._config)
        client.calendar = CalendarService(self._config)
        client.corehr = CorehrService(self._config)
        client.helpdesk = HelpdeskService(self._config)
        client.lingo = LingoService(self._config)
        client.sheets = SheetsService(self._config)
        client.meeting_room = MeetingRoomService(self._config)
        client.optical_char_recognition = OpticalCharRecognitionService(self._config)
        client.report = ReportService(self._config)
        client.task = TaskService(self._config)
        client.attendance = AttendanceService(self._config)
        client.hire = HireService(self._config)
        client.security_and_compliance = SecurityAndComplianceService(self._config)
        client.speech_to_text = SpeechToTextService(self._config)
        client.vc = VcService(self._config)
        client.auth = AuthService(self._config)
        client.block = BlockService(self._config)
        client.docx = DocxService(self._config)
        client.drive = DriveService(self._config)
        client.okr = OkrService(self._config)

        return client

    def _init_cache(self):
        if self._config.cache is not None:
            TokenManager.cache = self._config.cache

    def _init_logger(self):
        logger.setLevel(int(self._config.log_level.value))
