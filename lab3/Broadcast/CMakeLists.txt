cmake_minimum_required(VERSION 3.17)
project(Broadcast)

set(CMAKE_CXX_STANDARD 14)

add_executable(Broadcast receiver.cpp sender/sender.cpp)