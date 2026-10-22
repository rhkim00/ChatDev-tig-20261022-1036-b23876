import ast
import json
import logging
import re
from time import sleep
from typing import Union

# =============================
# Singleton Decorator
# =============================
def Singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


# =============================
# JSON Formatter Class
# =============================
class JsonFormat:
    def __init__(self, query_func):
        self.query_func = query_func

    def _extract_json_candidates(self, text: str) -> list[str]:
        text = str(text or "").strip()
        if not text:
            return []

        candidates = [text]

        stack = []
        start_idx = None
        for idx, char in enumerate(text):
            if char == "{":
                if start_idx is None:
                    start_idx = idx
                stack.append(char)
            elif char == "}":
                if stack:
                    stack.pop()
                    if not stack and start_idx is not None:
                        candidates.append(text[start_idx : idx + 1])
                        start_idx = None

        fenced_matches = re.findall(r"```(?:json)?\s*([\s\S]*?)```", text, flags=re.IGNORECASE)
        candidates.extend(match.strip() for match in fenced_matches if match.strip())

        return candidates

    def _load_python_dict(self, text: str) -> dict:
        parsed = ast.literal_eval(text.strip())
        if isinstance(parsed, dict):
            return parsed
        raise ValueError("Parsed object is not a dict")

    def _normalize_action_dict(self, parsed: dict) -> tuple[bool, Union[dict, str]]:
        if not isinstance(parsed, dict):
            return False, ""

        action = parsed.get("action")
        parameter = parsed.get("parameter", "")

        if action in (None, ""):
            return False, ""

        if isinstance(parameter, (list, tuple)):
            parameter = [str(item).strip() for item in parameter if str(item).strip()]
        elif isinstance(parameter, dict):
            for key in ("parameter", "query", "url", "file", "filename", "code"):
                value = parameter.get(key)
                if value not in (None, ""):
                    parameter = value
                    break
            else:
                parameter = json.dumps(parameter, ensure_ascii=False)
        elif parameter is None:
            parameter = ""
        else:
            parameter = str(parameter).strip()

        return True, {"action": str(action).strip(), "parameter": parameter}

    def load_json_with_invalid_escape(self, json_str: str) -> dict:
        """Handle invalid JSON escape sequences."""
        json_str = json_str.strip()
        json_str = re.sub(r'(?<!\\)\n', ' ', json_str)

        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            try:
                json_str = re.sub(r'\$begin:math:text$?!["\\\\/bfnrtu])', r'\\\\\\\\', json_str)
                json_str = re.sub(r'(?<!\\$end:math:text$"', '\\"', json_str)
                json_str = f'"{json_str}"'
                return json.loads(json_str)
            except json.JSONDecodeError:
                return {'action': 'Error', 'parameter': 'Invalid JSON format'}

    def json_check(self, text: str) -> tuple[bool, Union[dict, str]]:
        for candidate in self._extract_json_candidates(text):
            try:
                d = self.load_json_with_invalid_escape(candidate)
                valid, normalized = self._normalize_action_dict(d)
                if valid and normalized.get("action") != "Error":
                    return True, normalized
            except Exception:
                pass

            try:
                d = self._load_python_dict(candidate)
                valid, normalized = self._normalize_action_dict(d)
                if valid and normalized.get("action") != "Error":
                    return True, normalized
            except Exception:
                pass
        return False, ""

    def json_reformat(self, text: str, max_try_times: int = 3) -> dict:
        """Reformat GPT text to strict JSON object."""
        prompt_template = """
        Please reformat the given text strictly according to the specified JSON format.
        The given text is: {}.
        The specified JSON format is: {{"action": "", "parameter": ""}}, presented in plain text.
        Only return one JSON object.
        """
        for _ in range(max_try_times):
            text = text.replace("null", '"Error"').replace("None", '"Error"').replace("```json", "").replace("```", "")
            valid, json_obj = self.json_check(text)
            if valid:
                return json_obj
            logging.info(f"Error format:\n{text}")
            text, _ = self.query_func(prompt_template.format(text))
            sleep(1)
        return {'action': 'Error', 'parameter': 'Error'}
