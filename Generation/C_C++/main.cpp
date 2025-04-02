#include <iostream>
#include <Poco/MD5Engine.h>
#include <Poco/DigestStream.h>

int main() {
    std::string input;
    std::cout << "Enter a string to hash with MD5: ";
    std::getline(std::cin, input);

    Poco::MD5Engine md5;
    Poco::DigestOutputStream ds(md5);
    ds << input;
    ds.close();

    std::string md5hash = Poco::DigestEngine::digestToHex(md5.digest());
    std::cout << "MD5 Hash: " << md5hash << std::endl;

    return 0;
}
