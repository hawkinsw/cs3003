#include <iostream>

bool do_write(std::string filename, std::string contents) {
    //
    return true;
}

bool check_permissions(std::string username) {
    if (username == "root") {
        return true;
    }
    return false;
}

bool debug_operation = true;

bool write_to_file(std::string filename,
  std::string contents,
  std::string username) {
    if (debug_operation) {
        std::cout << "Checking the permissions of the writer.\n";
    }
    if (check_permissions(username)) {
        return do_write(filename, contents);
    }
    return false;
}

int main() {
    write_to_file("C:\MyResume.docx", "", "hawkinsw", true);
    return 0;
}