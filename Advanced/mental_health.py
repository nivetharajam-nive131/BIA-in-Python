import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you with your mental health today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a mental health chatbot", "My name is mental health chatbot, How can I help you today?"]
    ],
    [
        r"how can you help me?",
        ["I am here to listen and provide support for any issues you may be facing related to your mental health. Is there something specific you would like to talk about?",
         "I can also provide resources and information on different mental health topics and connect you with professional help if needed."]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"I am feeling (.*)",
        ["I am sorry to hear that you are feeling %1. Can you tell me more about how you are feeling?",
         "It is important to talk about our emotions and how we are feeling. How can I support you right now?"]
    ],
    [
        r"quit",
        ["Thank you for chatting with me. I hope I was able to provide some help and support. Take care of yourself."]
    ],
    [
        r"I need help with (.*)",
        ["I'm here to help. %1 is a common concern and there are many resources available to help you. Can you tell me more about what you're going through? I can provide information and connect you with professionals who can provide additional support if needed."]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
