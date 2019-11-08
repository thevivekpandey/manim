from manimlib.imports import *

class Code(VGroup):
   def __init__(self, *lines, **kwargs):
      super().__init__(**kwargs)
      text = "\\normalfont\\texttt{"
      for line in lines:
         line = line.replace("SPACE", "\\hspace*{0.56cm}")
         text += line + "\\newline "
      text += "}"
      self.code = TexMobject(text)
      self.add(self.code)
