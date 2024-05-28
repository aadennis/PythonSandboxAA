<h1>"Mark" photo indexer</h1>
The user's entry point is <code>index_photos_by_month.py</code> .

Perhaps as a 1-off, the user will also edit <code>config.py</code>, which records the source (where the original photos are to be found) and target (where the copied/converted photos are to be saved) folders, and removes the need for the user to enter run-time parameters.

```mermaid
%% conventions: folders-F-blue, modules-M-black,methods-m-white
graph TD
%% Classes
    classDef blueFill fill:#01f,stroke:#white,stroke-width:2px,color:#FFFFFF;
    classDef blackFill fill:#000000,stroke:#FFFFFF,stroke-width:1px,color:#FFFFFF;
    classDef whiteFill fill:#FFFFFF,stroke:#000000,stroke-width:2px,color:#000000;

%% Nodes
    F1(ImageHandling):::blueFill
    F2(src):::blueFill
    M1[index_photos_by_month.py]:::blackFill
    M2[config.py]:::blackFill
    M3[ImageHandler.py - IH]:::blackFill
    m1[IH.ctor]:::whiteFill
    m2[IH.process_files]:::whiteFill
%% Node connections
    F1 --> F2
    F2 --> M1
    F2 --> M2
    F2 --> M3
    M2 --> M1
    M3 --> M1
    M1 --> m1
    M1 --> m2 
    
```

The full command for <code>index_photos_by_month.py</code> is   
<code> python.exe index_photos_by_month.py</code>  
, and indeed even that assumes that (a) python is on the path, and (b) python.exe is the name of the python executable, as this differs between OSes.

You start <code>index_photos_by_month.py</code>. This pulls in the configuration data from <code>config.py</code>, and imports <code>ImageHandler.py</code>. This latter file holds all of the functionality. <code>index_photos_by_month.py</code>, is "just" the route into the stuff inside <code>ImageHandler.py</code>.

