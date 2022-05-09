from pdf2image import convert_from_path
import os
import pytesseract

class GeraTxt:
  def __init__(self, _pathFile):
    self.pathFile = _pathFile

  def convertPdf2Image(self):
    images = convert_from_path(self.pathFile)
 
    aname = []
    for i in range(len(images)):
      aname.append('page' + str(i) + '.jpg')
      images[i].save(aname[i], 'JPEG')

    return aname

  def convert(self):
    afileExt = os.path.splitext(self.pathFile)[1]
    
    aname = []
    adic = {}
    if afileExt.lower() == '.pdf':
      aname = self.convertPdf2Image()
    else:
      for item in os.listdir(self.pathFile):
        aname.append(str(item))

    #tesseract-ocr-w32-setup-v5.0.1.20220118.exe
    pytesseract.pytesseract.tesseract_cmd = 'D:\/Tesseract\/tesseract.exe'
    for item in aname:      
      afile = pytesseract.image_to_string(image = str(self.pathFile) + str(item), lang = 'por')
      temp = open('C:\/Users\/conta\/Desktop\/Python\/Convert_Txt_Audio\/Texto\/' + str(item) + '.txt', 'w')
      temp.writelines(afile)
      temp.close()
      adic[str(item)] = afile

    return adic