"""Prompt templates for the three tasks in the mini project."""

def get_prompt(task: str, user_text: str, improved: bool = True) -> str:
    if task == "Q&A":
        if improved:
            return (
                "You are a helpful educational assistant. Answer in simple English. "
                "Be accurate, organize the answer clearly, give one short example when useful, "
                "and say when you are unsure. Do not invent facts.\n\n"
                f"User question:\n{user_text}"
            )
        return f"Answer this question:\n{user_text}"

    if task == "Text Summarization":
        if improved:
            return (
                "Summarize the text in simple English using 3–5 bullet points. "
                "Keep the main ideas and important facts. Do not add information that is not in the text.\n\n"
                f"Text:\n{user_text}"
            )
        return f"Summarize this text:\n{user_text}"

    if task == "Text Classification":
        if improved:
            return (
                "Classify the text sentiment as exactly one of these labels: Positive, Negative, Neutral. "
                "Return the label first, followed by one short reason. If the sentiment is unclear, choose Neutral.\n\n"
                f"Text:\n{user_text}"
            )
        return f"Classify the sentiment of this text:\n{user_text}"

    return user_text
