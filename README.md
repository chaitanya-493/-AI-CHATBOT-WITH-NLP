# AI-CHATBOT-WITH-NLP
*COMPANY* : CODTECH IT SOLUTIONS
*NAME* : KOLUSU CHAITANYA VARMA
*INTERN ID* : CT08DF1081
*DOMAIN* : PYTHON PROGRAMMING
*DURATION* : 8 WEEKS
*MENTOR* : NEELA SANTHOSH

**DESCRIPTION** :
AI Chatbot with NLP using Python and NLTK (ChattyPro)
As part of this project, I developed a conversational AI chatbot named ChattyPro using Python. The core aim was to simulate a natural conversation between a user and the computer, leveraging basic Natural Language Processing (NLP) concepts. The chatbot is structured as a rule-based system built with the help of NLTK (Natural Language Toolkit).

The bot works by identifying key patterns in user input through regular expressions. These input patterns are mapped to predefined responses. The project includes a variety of conversation patterns such as greetings, queries about the current date or time, questions about trending technologies, regional food preferences (like Andhra cuisine), birthday wishes, and fallback responses for unknown queries.

To build this, I used NLTK’s Chat utility, which makes it easy to define interaction rules using pattern-response pairs. The chat logic is encapsulated in a PerfectChatbot class, which manages the conversation loop, handles user input, and generates appropriate responses. The chatbot was designed and tested entirely within PyCharm.
While this chatbot currently uses a rule-based architecture, it still incorporates foundational NLP elements. 
For example:It applies tokenization and string matching using regular expressions.
It handles context-aware responses by detecting keywords (like "birthday", "food", "time", etc.).
It dynamically formats responses using Python’s datetime module to provide real-time output like the current date or time.
However, this project also serves as a prototype for more advanced AI chatbots. In its current form, it does not rely on machine learning or deep NLP models, but it is structured in a way that can easily be extended using:
spaCy for named entity recognition or part-of-speech tagging.
Intent classification models built using Scikit-learn or transformers.
Integration with Rasa or Hugging Face Transformers for creating context-aware, learning-based conversational agents.

**Applications**:
This chatbot lays the groundwork for building more intelligent, NLP-driven applications. Possible real-world applications include:
Customer service bots for websites and apps.
Voice assistant prototypes.
FAQ bots in educational, healthcare, or e-commerce domains.
Language learning tools for interactive vocabulary practice.
