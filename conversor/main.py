from GeraTxt import GeraTxt
from GeraAudio import GeraAudio

def main():
  doc = GeraTxt('C:\/Users\/conta\/Desktop\/Python\/Convert_Txt_Audio\/images\/')
  adic = doc.convert()
  audio = GeraAudio(adic)
  audio.convert()

if __name__ == "__main__":
  main()