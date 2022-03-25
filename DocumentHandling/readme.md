As an editor  
Given I have an unformatted document that includes shorter lines that can be inferred as Headings  
I want to apply rules that result in those Headings being numbered as Level 1 or Level 2  
So that I can pass it to a Document api (e.g. Google Docs API) to apply Styles  

The project has:
a part to update the content - Python which receives and outputs text with the numbered headings
a part to update the presentation - upload the document from the previous step into Google Docs, and apply the GDocs API JavaScript

Example  
_Before:_
```
The Title

First Header
Header Two

Some body and then some repeat all that until more than max for header
2 First Header
2 Header Two

And then some body and then some repeat all that until more than max for header
```
_After:_
```
The Title
1. First Header
1.1 Header Two
Some body and then some repeat all that until more than max for header
2. First Header
2.1 Header Two
2.2 Header again
2 And then some body and then some repeat all that until more than max for header
```

In "After", note that:






