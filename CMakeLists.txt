cmake_minimum_required(VERSION 3.16)
project(problem2 CXX)
set(CXX_STANDARD_REQUIRED 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(FILES 
    "cpp/src/graph.cpp"
    "cpp/src/vertex_approx.cpp"
)

include_directories(
    "cpp/include"
)

add_executable(vertex_approx ${FILES})

