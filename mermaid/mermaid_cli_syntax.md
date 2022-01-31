### some stuff
https://github.com/mermaid-js/mermaid-cli
cd 'C:\Program Files\nodejs'
npm install @mermaid-js/mermaid-cli
 ./node_modules/.bin/mmdc -i C:\temp\diagram.md -o c:\temp\xdiagram.md
Found 1 mermaid charts in Markdown input
c:\temp\xdiagram-1.svg
c:\temp\xdiagram.md 

```mermaid
graph
  R[(root)] --> S1(src)
    R --> T1(test)
    R --> D1(data)
    R --> Tp1(templates)
    S1 --> C1[rest.py]
    S1 --> C2[model.py]
    S1 --> C3[tidetimes.py]
    S1 --> C4[utilities.py]
    T1 --> ToDo
    D1 --> D2[holds runtime data files]
    Tp1 --> TpTT[tidetimes.html]
```

