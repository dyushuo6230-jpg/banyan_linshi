from .models import ActionRequest, ActionResult, ExecutionScope

__all__ = ["RuntimeAPI", "ActionRequest", "ActionResult", "ExecutionScope"]


def __getattr__(name):
    if name == "RuntimeAPI":
        from .api import RuntimeAPI
        return RuntimeAPI
    raise AttributeError(name)
