import nltk
from nltk.chat.util import Chat, reflections
import random
from datetime import datetime

# Download NLTK data silently
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# Enhanced chatbot patterns
pairs = [
    # Greetings
    [
        r"(hi|hello|hey|greetings|hai|what's up)",
        ["Hello! How can I assist you today?", "Hi there!", "Greetings!"]
    ],

    # Name
    [
        r"(what is your name|who are you|your name)",
        ["I'm ChattyPro, your AI assistant!", "You can call me ChattyPro."]
    ],

    # Time
    [
        r"(what('s| is) the time|current time|tell me the time|time please|what time is it)",
        [f"The current time is {datetime.now().strftime('%H:%M')}"]
    ],

    # Date
    [
        r"(what('s| is) (today|the) date|current date|tell me the date|date please)",
        [f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"]
    ],

    # New Technologies
    [
        r"(what are|tell me about|explain|suggest|recommend)( me)?( some| any)?( new| emerging)?( tech| technologies| technology)",
        ["Here are some exciting new technologies:\n"
         "1. AI-Powered Healthcare Diagnostics\n"
         "2. Self-Healing Materials\n"
         "3. Brain-Computer Interfaces\n"
         "4. Carbon Capture Technologies\n"
         "Would you like details about any specific one?"]
    ],

    # Andhra Food
    [
        r"(andhra|andhra pradesh)( people's|)( favorite|favourite) food|(what do andhra people like to eat)",
        ["The favorite foods of Andhra people include:\n"
         "1. Hyderabadi Biryani (spicy rice dish)\n"
         "2. Gongura Pachadi (sorrel leaves chutney)\n"
         "3. Pesarattu (green gram dosa)\n"
         "4. Andhra Chicken Curry (extremely spicy)\n"
         "Andhra cuisine is famous for its fiery heat and bold flavors!"]
    ],

    # Birthday
    [
        r"(today is|it's|celebrating)( my)?( birthday|bday|birth day)",
        ["Happy Birthday! 🎉🎂",
         "Wishing you a wonderful birthday!",
         "Happy Birthday! May your day be special!",
         "Many happy returns of the day!"]
    ],

    # Fallback
    [
        r"(.*)",
        [
            'I understand you\'re asking about: "{}". Could you rephrase that?',
            "Interesting question! I'm still learning about that.",
            "I'm not sure I understand. Could you ask differently?"
        ]
    ]
]


class PerfectChatbot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)
        self.name = "ChattyPro"

    def get_response(self, user_input):
        """Get response using the chat pairs"""
        response = self.chatbot.respond(user_input)

        if response:
            if '{}' in response:
                return response.format(user_input)
            return response

        return random.choice([
            "I'm still learning. Could you try asking differently?",
            "Interesting question! Let me think about that...",
            "I'm not sure I understand. Could you rephrase?"
        ])

    def converse(self):
        print(f"{self.name}: Hi! I'm your AI assistant. Ask me anything!")
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue

                if user_input.lower() in ['quit', 'bye', 'exit']:
                    print(f"{self.name}: Goodbye! Have a great day!")
                    break

                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
            except Exception as e:
                print(f"{self.name}: Oops! Something went wrong. Let's try again.")


if __name__ == "__main__":
    PerfectChatbot().converse()
