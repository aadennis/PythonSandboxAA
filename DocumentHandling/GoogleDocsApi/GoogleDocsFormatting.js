// reference:
// https://developers.google.com/apps-script/reference/document/body#getchildindexchild
// https://developers.google.com/apps-script/reference/document/body#getattributes
// https://stackoverflow.com/questions/8273047/javascript-function-similar-to-python-range
// Only interested in paragraphs...isParagraph(element)
// Headings are...
// H1 - 1-2 digits followed by dot and space
// H2 - 1-2 digits followed by dot followed by 1-2 digits followed by space

function log(message) {
  //Logger.log(message)
}

function isParagraph(element) {
  return element.getType() === DocumentApp.ElementType.PARAGRAPH
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

function isHeading2(paragraph) {
  const re = /^\d{1,2}\.(\d{1,2}) .+/;
  let chk1 = re.exec(paragraph)
  if (chk1 === null) {
    return false
  }
  return true
}


/* MAIN
Run this after the (Python) script that updates the content to 
include heading numbering.
Then, this walks each paragraph and applies the correct style 
to Headings level 1 (h1_style), and level 2 (h2_style).
Any remaining paragraphs are taken to be normal text, which
has its own style (nt_style)
*/
function formatHeadings() {
  var body = DocumentApp.getActiveDocument().getBody();

  var searchType = DocumentApp.ElementType.PARAGRAPH;
  var H1 = DocumentApp.ParagraphHeading.HEADING1;
  var H2 = DocumentApp.ParagraphHeading.HEADING2;
  var NT = DocumentApp.ParagraphHeading.NORMAL;
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
    
  }
}

// -----------------
// Tests

function testHeading1() {
  ret = isHeading1('12. blah')
  log(ret)
}

function testHeading2() {
  ret = isHeading2('12.3 blah')
  log(ret)
}

