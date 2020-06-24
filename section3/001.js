var combineMe = []

app.findObjectPreferences = null;
app.findObjectPreferences.appliedObjectStyles = 'text';
found_list = app.activeDocument.findObject(true);
for (a=0; a<found_list.length; a++) {
  if (found_list[a] instanceof TextFrame)
    combineMe.push(found_list[a]);
  }

//alert(combineMe.length)

combineMe.sort (function (a,b) {
  return (a.geometricBounds[0] < b.geometricBounds[0]) || (a.geometricBounds[0] == b.geometricBounds[0] && a.geometricBounds[1] < b.geometricBounds[1]) ? -1 : 1; } );


for (i=0; i<combineMe.length-1; i++) {
  if (combineMe[i].nextTextFrame == null) {
    nextFree = i+1;
    while (nextFree < combineMe.length && combineMe[nextFree].previousTextFrame != null)
      nextFree++;
      combineMe[i].nextTextFrame = combineMe[nextFree];
    }
  }