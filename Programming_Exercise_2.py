# Programming Exercise 2
# Spam Message Checker


def get_message():
    """Gets an email message from the user."""
    print("Enter an email message:")
    message = input()
    return message


def check_spam(message, spam_words):
    """Checks the message for spam words."""
    found_words = []
    message = message.lower()

    for word in spam_words:
        if word.lower() in message:
            found_words.append(word)

    return found_words


def get_likelihood(score):
    """Determines likelihood of spam."""
    if score <= 2:
        return "Low likelihood of spam"
    elif score <= 5:
        return "Medium likelihood of spam"
    else:
        return "High likelihood of spam"


def display_results(score, likelihood, found_words):
    """Displays results."""
    print("\nSpam Score:", score)
    print("Likelihood:", likelihood)

    print("\nWords/Phrases Found:")
    if len(found_words) == 0:
        print("No spam words or phrases were found.")
    else:
        for word in found_words:
            print("-", word)


def main():
    spam_words = [
        "free",
        "winner",
        "cash",
        "money",
        "urgent",
        "limited time",
        "buy now",
        "click here",
        "guaranteed",
        "risk free",
        "act now",
        "congratulations",
        "claim",
        "prize",
        "exclusive",
        "offer",
        "deal",
        "discount",
        "save big",
        "earn money",
        "no cost",
        "credit card",
        "selected",
        "bonus",
        "investment",
        "miracle",
        "cheap",
        "order now",
        "subscribe",
        "special promotion"
    ]

    message = get_message()
    found_words = check_spam(message, spam_words)
    score = len(found_words)
    likelihood = get_likelihood(score)

    display_results(score, likelihood, found_words)


main()