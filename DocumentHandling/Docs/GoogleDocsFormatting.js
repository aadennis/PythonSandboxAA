// reference:
// https://developers.google.com/apps-script/reference/document/body#getchildindexchild
// https://developers.google.com/apps-script/reference/document/body#getattributes
// https://stackoverflow.com/questions/8273047/javascript-function-similar-to-python-range
// Only interested in paragraphs...isParagraph(element)
// Headings are...
// H1 - 1-2 digits followed by space
// H2 - 1-2 digits followed by 1-2 digits followed by space

const re = /^\d{1,2}\.(\d{1,2})* .+/;
const checkit = re.exec()


function log(message) {
  //Logger.log(message)
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

function isHeading2(paragraph) {
  const re = /^\d{1,2}\.(\d{1,2}) .+/;
  let chk1 = re.exec(paragraph)
  if (chk1 === null) {
    return false
  }
  return true
}

function testHeading2() {
  ret = isHeading2('12. blah')
  log(ret)
}

function isHeading1(paragraph) {
  const re = /^\d{1,2}\. .+/;
  log(paragraph)
  let chk1 = re.exec(paragraph)
  if (chk1 === null) {
    return false
  }
  return true
}

function testHeading1() {
  ret = isHeading1('12. blah')
  log(ret)
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
  var nt_style = {};
  
  h1_style[DocumentApp.Attribute.FONT_FAMILY] = 'Ubuntu';
  h1_style[DocumentApp.Attribute.BOLD] = true;
  h1_style[DocumentApp.Attribute.FONT_SIZE] = 18;
  h2_style[DocumentApp.Attribute.FONT_FAMILY] = 'Ubuntu';
  h2_style[DocumentApp.Attribute.BOLD] = true;
  h2_style[DocumentApp.Attribute.FONT_SIZE] = 14;
  nt_style[DocumentApp.Attribute.FONT_FAMILY] = 'Ubuntu';
  nt_style[DocumentApp.Attribute.BOLD] = false;
  nt_style[DocumentApp.Attribute.FONT_SIZE] = 10;

  var searchResult = null;

  while (searchResult = body.findElement(searchType, searchResult)) {
    var par = searchResult.getElement().asParagraph();
    if (isHeading1(par.getText())) {
      par.setHeading(H1)
      par.setAttributes(h1_style);
      continue
    }
     if (isHeading2(par.getText())) {
      par.setHeading(H2)
      par.setAttributes(h2_style);
      continue
    }
    
    par.setHeading(NT)
    par.setAttributes(nt_style);
    continue
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
