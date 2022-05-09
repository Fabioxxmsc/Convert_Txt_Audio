from gtts import gTTS

class GeraAudio:
  def __init__(self, data, name = 'audio.mp3'):
    self.data = data
    self.name = name
    self.language = 'pt-br'

  def convert(self):
    for chave in self.data:
      sp = gTTS(text = self.data[chave], lang = self.language)
      sp.save('C:\/Users\/conta\/Desktop\/Python\/Convert_Txt_Audio\/Audio\/' + str(chave) + '_' + self.name)