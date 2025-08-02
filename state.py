from typing import TypedDict, List, Optional

class GraphState(TypedDict):
    messages: List[dict]
    inbox_email: Optional[str]
    email_result: Optional[str]
    calendar_result: Optional[str]
    file_result: Optional[str]
    whatsapp_result: Optional[str]
    call_result: Optional[str]
    web_result: Optional[str]
