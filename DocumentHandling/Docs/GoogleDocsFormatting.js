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
    
  }
}

