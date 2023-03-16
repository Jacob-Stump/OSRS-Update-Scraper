import ScrapeDeez


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!update':
        return ScrapeDeez.updates
