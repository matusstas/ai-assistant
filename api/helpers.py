from typing import Optional, List


def trim_history(
    encoding,
    history,
    threshold_history_max_tokens,
) -> Optional[List[dict]]:
    """
    Trim history.
    """
    tokens_count = 0
    history_trimmed = []

    for message in reversed(history):        
        tokens_message = len(encoding.encode(message.get("content")))

        if tokens_message > threshold_history_max_tokens:
            continue

        if tokens_count + tokens_message <= threshold_history_max_tokens:
            history_trimmed.insert(0, message)
            tokens_count += tokens_message
        else:
            break

    return history_trimmed