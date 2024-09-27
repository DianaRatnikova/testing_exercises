from functions.level_1_5.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
"text, good_words, bad_words, expected_result",
[
   ('text_1', 'good_words_1', 'bad_words_1', None), 
   ('text_2', 'good_words_1', 'bad_words_1', None),
   ('text_3', 'good_words_1', 'good_words_1', None),
   ('text_4', 'good_words_2', 'good_words_1','GOOD'),
   ('text_5', 'good_words_3', 'bad_words_2', 'BAD'),
   ('text_6', 'good_words_2', 'good_words_1', None),
   ('text_7', 'good_words_1', 'good_words_2','BAD'),
   ('text_8', 'good_words_3', 'good_words_2', 'BAD'),
   ('text_8', 'good_words_3', 'good_words_3', None),
   ('text_9', 'good_words_3', 'good_words_3', None),
    ('text_10', 'good_words_4', 'bad_words_3', None),
]
)
def test__check_tweet_sentiment__is_valid(text, good_words, bad_words, expected_result, request):
    text = request.getfixturevalue(text)
    good_words = request.getfixturevalue(good_words)
    bad_words = request.getfixturevalue(bad_words)
    assert check_tweet_sentiment(text, good_words, bad_words) is expected_result


def test__check_tweet_sentiment__attribute_error(text_11, good_words_3, bad_words_2):
    with pytest.raises(AttributeError):
        check_tweet_sentiment(text_11, good_words_3, bad_words_2)

