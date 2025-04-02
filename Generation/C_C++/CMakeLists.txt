cmake_minimum_required(VERSION 3.15)
project(md5_poco_example)

set(CMAKE_CXX_STANDARD 17)

find_package(Poco REQUIRED COMPONENTS Foundation Crypto)

add_executable(md5_poco_example main.cpp)
target_link_libraries(md5_poco_example Poco::Foundation Poco::Crypto)
