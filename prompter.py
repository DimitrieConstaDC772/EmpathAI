# File: app/modules/prompter.py

def generate_empathy_response(text, analysis):
    """
    Generates a tailored communication suggestion based on the emotional tone analysis.
    
    Args:
        text (str): The original input message.
        analysis (dict): Output from analyzer.py including emotion, tone, and empathy_score.
    
    Returns:
        str: Suggested empathetic improvement to the message.
    """

    emotion = analysis.get("emotion", "neutral")
    tone = analysis.get("tone", "neutral")
    empathy_score = analysis.get("empathy_score", 5)

    # Smart logic for tailored feedback
    if tone == "aggressive" or empathy_score < 4:
        return "Try softening your message and acknowledging the other person's point of view."
    elif tone == "formal" and emotion == "sad":
        return "Consider adding a supportive statement to show understanding."
    elif tone == "neutral" and emotion == "nervous":
        return "You might help the other person feel at ease by expressing reassurance."
    elif tone == "friendly" and empathy_score >= 8:
        return "Your message already shows strong empathy — well done!"
    else:
        return "Try to rephrase with a bit more warmth or clarity to improve connection."
