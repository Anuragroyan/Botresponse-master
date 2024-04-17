import random

R_EATING = "I don't like eating anything because I'm a bot obviously"
R_ADVICE = "If I were you, I would go to the Internet and type exactly what you wrote there!"

def unknown():
    response = ["could you please re-phrase that?",
               "...",
               "Sounds about right.",
               "what does that mean?"][random.randrange(4)]
    return response       