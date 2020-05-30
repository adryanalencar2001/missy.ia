import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
from playsound import playsound

class VoiceModule():
	"""Module as work with voice recognition and play voice sounds"""
	def __init__(self, language="pt-br", translate=False, language_out="en"):
		self.language="pt-br"
		self.translate = translate
		self.language_out = language_out
		self.translator = Translator()

	""" Get string from phrase parameter and transform in voice audio"""
	def create_audio(self, phrase):
		language = self.language

		if self.translate:
			phrase = self.translator.translate(phrase, dest=str(self.language_out)).text
			language = self.language_out
		
		tts = gTTS(phrase, lang=language)
		tts.save("temp/audio.mp3")

		playsound("temp/audio.mp3")


	def play_custom(self, path="temp/audio.mp3"):
		playsound(path)

	"""Hear the microphone and transform a string text"""
	def hear_mic(self):
		language = self.language
		phrase = "Erro no reconhecimento de fala"
		error = True

		mic = sr.Recognizer()

		if self.translate:
			phrase = self.translator.translate(phrase, dest=str(self.language_out)).text
			language = self.language_out
		
		try:
			with sr.Microphone() as source:
				mic.adjust_for_ambient_noise(source)
				audio = mic.listen(source)

			phrase = mic.recognize_google(audio, language=language)
			error = False

			return error, phrase
		except:
			return error, phrase