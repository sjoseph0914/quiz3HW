pic = makeEmptyPicture(200,200) 

def color4row(row):
  r=red4row(row) 
  g=green4row(row) 
  b=blue4row(row) 
  return makeColor(r,g,b) 

def red4row(row):
  return -230/200.0*row+230 

def green4row(row):
  return -206/200.0*row+206

def blue4row(row): 
  return -177/200.0*row+177 
  
for row in range(200):
  for col in range(200): 
    p=getPixel(pic,col,row)
    c=color4row(row) 
    setColor(p,c)
  show(pic)  
    
