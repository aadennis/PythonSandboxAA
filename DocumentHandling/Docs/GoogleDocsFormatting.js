// reference:
// https://developers.google.com/apps-script/reference/document/body#getchildindexchild
// https://developers.google.com/apps-script/reference/document/body#getattributes
// https://stackoverflow.com/questions/8273047/javascript-function-similar-to-python-range

function log(message) {
  Logger.log(message)
}

function countWordsInLine(textLine) {
  a = textLine.split(" ")

  log("array from line: [" + a + "]")
  b = a.length
  log("length of line/array is: [" + b + "]")
  return b
}

function isParagraph(element) {
  return element.getType() === DocumentApp.ElementType.PARAGRAPH
}

// Is the element a Heading?
// A Heading is a paragraph which has between 1 and 11 words. 
// Any larger, we judge it must be a paragraph "proper"
// Any smaller, continue
function isHeading(element) {
  this.element = element;
  if (!isParagraph(element)) {
    log("Not a heading as it is not a paragraph")
    return false;
  }
  paragraphText = element.getText()
  wordCount = countWordsInLine(paragraphText)
  if (wordCount > 0 && wordCount < 12) {
    log("It is a heading")
    return true
  }
  log("It is not a heading")
  return false
}

// Only paragraphs can have a heading set, and not, for
// example, table of contents
// Parameter "index" is for debugging, to keep a track of the current line
// in the body
function setHeading(element, index) {
  log("Set Heading - element [" + index + "]")
  if (!isParagraph(element)) {
    return
  }
  if (isHeading(element)) {
    log("Assigning HEADING2")
    element.setHeading(DocumentApp.ParagraphHeading.HEADING2)
  } else {
    log("Assigning NORMAL")
    element.setHeading(DocumentApp.ParagraphHeading.NORMAL)
  }

}

function setLists() {
  var body = DocumentApp.getActiveDocument().getBody();
  body.appendParagraph("Some junk.");
  body.insertHorizontalRule(0);
  body.appendHorizontalRule()
  body.appendParagraph("some more junk.");

  // Append a new list item to the body.
  var item1 = body.appendListItem('Item 1');
  // Log the new list item's list ID.
  Logger.log(item1.getListId());
  // Append a second list item with the same list ID.
  var item2 = body.appendListItem('Item 2');
  item2.setListId(item1);
}

/*
line 1
line 2
line 3
*/

function setA() {
  var body = DocumentApp.getActiveDocument().getBody();
  var numChildrenInBody = body.getNumChildren()
  log("xThere are " + body.getNumChildren() + " elements in the document body.");

  for (let i of Array(numChildrenInBody).keys()) {
    element = body.getChild(i);
    a = element.getText()
    a = "x" + a
    body.appendParagraph(element)
  }
}

function taskA() {

  var body = DocumentApp.getActiveDocument().getBody();
  var numChildrenInBody = body.getNumChildren()
  tempi = 0
  for (let i of Array(numChildrenInBody).keys()) {
    tempi += i
    element = body.getChild(tempi);
    a = element.getText();
    log("text [" + a + "]; tempi [" + tempi + "]; i [" + i + "]");
    log("tempi is " + tempi)
    //body.appendParagraph(a) // this goes to the back of the doc
    body.insertParagraph(tempi, a)

  }

}

function and2() {
  var body = DocumentApp.getActiveDocument().getBody();
  body.insertParagraph(0, "An editAsText sample.");
  body.insertHorizontalRule(0);
  body.insertParagraph(0, "An example.");
  body.editAsText().deleteText(12, 25);
  body.editAsText().insertText(12, "this is a thing")

}

function and3() {
  // Get the body section of the active document.
  var body = DocumentApp.getActiveDocument().getBody();
  // Define the search parameters.
  var searchType = DocumentApp.ElementType.PARAGRAPH;
  var searchHeading = DocumentApp.ParagraphHeading.HEADING1;
  var searchResult = null;
  // Search until the paragraph is found.
  while (searchResult = body.findElement(searchType, searchResult)) {
    var par = searchResult.getElement().asParagraph();
    if (par.getHeading() == searchHeading) {
      // Found one, update and stop.
      var a = par.getText()
      par.setText('This is a HEADING1.' + a);

    }
  }
}

/*
Run this after a) setHeadings, b) manually applying Heading1
*/
function setNumbering() {
  var body = DocumentApp.getActiveDocument().getBody();
  var searchType = DocumentApp.ElementType.PARAGRAPH;
  var H1 = DocumentApp.ParagraphHeading.HEADING1;
  var H2 = DocumentApp.ParagraphHeading.HEADING2;
  var NT = DocumentApp.ParagraphHeading.NORMAL;
  var h1_ctr = 0;
  var h2_ctr = 0;
  var h1_style = {};
  var h2_style = {};
  h1_style[DocumentApp.Attribute.FONT_FAMILY] = 'Ubuntu';
  h1_style[DocumentApp.Attribute.BOLD] = true;
  h1_style[DocumentApp.Attribute.FONT_SIZE] = 18;
  h2_style[DocumentApp.Attribute.FONT_FAMILY] = 'Ubuntu';
  h2_style[DocumentApp.Attribute.BOLD] = true;
  h2_style[DocumentApp.Attribute.FONT_SIZE] = 14;
  

  var searchResult = null;
  // Search until the paragraph is found.
  while (searchResult = body.findElement(searchType, searchResult)) {
    var par = searchResult.getElement().asParagraph();
    if (par.getHeading() == NT) {
      continue
    }
    if (par.getHeading() == H1) {
      // tick on to the next H1 number, set h2_ctr = 0
      h1_ctr += 1
      h2_ctr = 0;
      var a = par.getText()
      par.setText(h1_ctr + ". " + a);
      par.setAttributes(h1_style);

    }
    if (par.getHeading() == H2) {
      // tick on the H2 counter
      h2_ctr += 1
      var a = par.getText()
      par.setText(h1_ctr + "." + h2_ctr + " " + a);
      par.setAttributes(h2_style);
    }
  }
}

// main...
function setHeadings() {
  var body = DocumentApp.getActiveDocument().getBody();
  var numChildrenInBody = body.getNumChildren()
  log("There are " + body.getNumChildren() + " elements in the document body.");

  for (let i of Array(numChildrenInBody).keys()) {
    element = body.getChild(i);
    setHeading(element, i);
  }
}