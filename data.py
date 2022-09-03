import requests
import html

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
question_data = [{"text": html.unescape(data["question"]), "answer":data["correct_answer"]}
                 for data in response.json()["results"]]


# question_data = [
    # {
    #     "text": "The common software-programming acronym &quot;I18N&quot; comes from the "
    #             "term &quot;Inter localization&quot;.",
    #     "answer": "False"
    # },
    # {
    #     "text": "FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;",
    #     "answer": "False"
    # },
    # {
    #     "text": "The very first recorded computer &quot;bug&quot; was a moth "
    #             "found inside a Harvard Mark II computer.",
    #     "answer": "True", "incorrect_answers": ["False"]
    # },
    # {
    #     "text": "Linus Torvalds created Linux and Git.",
    #     "answer": "True",
    # },
    # {
    #     "text": "MacOS is based on Linux.",
    #     "answer": "False",
    # },
    # {
    #     "text": "The open source program Redis is a relational database server.",
    #     "answer": "False"
    # },
    # {
    #     "text": "Time on Computers is measured via the EPOX System.",
    #     "answer": "False"
    # },
    # {
    #     "text": "The first dual-core CPU was the Intel Pentium D.",
    #     "answer": "False"
    # },
    # {
    #     "text": "It&#039;s not possible to format a write-protected DVD-R Hard Disk.",
    #     "answer": "True"
    # },
    # {
    #     "text": "A Boolean value of &quot;0&quot; represents which of these words?",
    #     "answer": "False"
    # }
# ]
