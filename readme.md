# Executing the Code
## Pre-Requisite 
1. Compiled Binary for vertex_approx for your platform. Pre-compiled is available for Ubuntu, stored at `./build/vertex_approx`. Refer [Setting Up](#setting-up)
2. Python Environment. Refer [Setting Up](#setting-up)
3. Output from P1. Stored in following  directory structure. (Already present in the project)
```
resources
├── graphs
│   ├── graph_10.graph
│   ├── graph_15.graph
│   ├── graph_20.graph
│   ├── graph_25.graph
│   ├── graph_30.graph
│   ├── graph_35.graph
│   ├── graph_40.graph
│   └── graph_45.graph
└── vertex
    ├── graph_10.vertex_cover
    ├── graph_15.vertex_cover
    ├── graph_20.vertex_cover
    ├── graph_25.vertex_cover
    ├── graph_30.vertex_cover
    ├── graph_35.vertex_cover
    ├── graph_40.vertex_cover
    └── graph_45.vertex_cover
```

## Execution
If running on unix like operating system, run the following, from the root directory (i.e. same directory as this file)
```
python python/automation.py --executable ./build/vertex_approx --resources ./resources
```

Output would be available in 
- `./resources/approx` directory, it would contain approximation of vertex cover along with accounting information
- `./resources/images` directory, it would contain all the image file representing Optimal Vertex Cover, Maximal Matching, and Approximated Vertex Cover. 
- `./resources/table_data.csv`, it contains required data from Program 1 and Program 2 in tabular format. 

# Setting Up
## Dependencies
- CMake (Version 3.16+)
- GNU C Compiler (C++ Std 17)
- Python (Version 3.9+)


## C++ Project
Run these commands in root directory of project (i.e. problem1) to compile c++ project.
```bash
mkdir build
cd ./build
cmake ..
cmake --build .
```


## Python Project
In the root directory of project (i.e. problem1), run following commands to setup python 
```bash
python -m venv venv
source venv/bin/activate
pip install -r ./python/requirement.txt
```