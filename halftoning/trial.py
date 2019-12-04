import halftone
h = halftone.Halftone('jc2.jpg')
h.make(style= 'grayscale', scale= 2, sample= 7, angles=[45])
