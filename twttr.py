def main():
    tweet = get_tweet()
    short_tweet = shorten_tweet(tweet)
    print("Output:", short_tweet)


def get_tweet():
    user_input = input("Input: ")
    return user_input


def shorten_tweet(tweet):
    vowels = ["a", "e", "i", "o", "u"]
    for i in tweet:
        if i in vowels:
            tweet = tweet.replace(i, "")
    return tweet


main()
