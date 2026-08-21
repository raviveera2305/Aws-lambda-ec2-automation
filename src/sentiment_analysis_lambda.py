import boto3

comprehend = boto3.client("comprehend")


def lambda_handler(event, context):

    review = event.get("review", "").strip()

    if not review:
        print("ERROR: No review provided in the event.")
        return {
            "statusCode": 400,
            "message": "Please provide a review."
        }

    print(f"Review: {review}")

    response = comprehend.detect_sentiment(
        Text=review,
        LanguageCode="en"
    )

    sentiment = response["Sentiment"]
    sentiment_score = response["SentimentScore"]

    print(f"Sentiment: {sentiment}")
    print(f"Sentiment Scores: {sentiment_score}")

    return {
        "statusCode": 200,
        "review": review,
        "sentiment": sentiment,
        "sentiment_scores": sentiment_score
    }