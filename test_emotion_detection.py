#  Import the function emotion_detector for testing.
from EmotionDetection.emotion_detection import emotion_detector
import unittest

#  Create the unit test class.
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        #  Test case dominant emotion "joy".
        result1 = emotion_detector("I am glad this happened.")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        #  Test case dominant emotion "anger".
        result2 = emotion_detector("I am really mad about this.")
        self.assertEqual(result2['dominant_emotion'], 'anger')
 
        #  Test case dominant emotion "disgust".
        result3 = emotion_detector("I am disgusted just hearing about this.")
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        #  Test case dominant emotion "sadness".
        result4 = emotion_detector("I am so sad about this.")
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        #  Test case dominant emotion "fear".
        result5 = emotion_detector("I am really afraid this will happen.")
        self.assertEqual(result5['dominant_emotion'], 'fear')

#  Call the unit tests.
unittest.main()
