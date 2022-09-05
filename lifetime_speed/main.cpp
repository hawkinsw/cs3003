#include <bits/stdint-uintn.h>
#include <iostream>
#include <chrono>

using namespace std::chrono_literals;

uint64_t empty() {
  return 0;
}

uint64_t local() {
  uint64_t a;
  uint64_t b;
  empty();
  return a + b;
}

uint64_t static_() {
  static uint64_t a;
  static uint64_t b;
  empty();
  return a + b;
}

int main() {

  uint64_t iterations{6000000};
  uint64_t counter{0};

  auto before = std::chrono::high_resolution_clock::now();
  auto after = std::chrono::high_resolution_clock::now();
  decltype(after - before) accumulated_time{};

  for (counter = 0; counter<iterations; counter++) {
    before = std::chrono::high_resolution_clock::now();
    empty();
    after = std::chrono::high_resolution_clock::now();
    accumulated_time += (after - before);
  }
  auto empty_time = accumulated_time;

  accumulated_time = 0ns;
  for (counter = 0; counter<iterations; counter++) {
    before = std::chrono::high_resolution_clock::now();
    local();
    after = std::chrono::high_resolution_clock::now();
    accumulated_time += (after - before);
  }
  auto local_time = accumulated_time;

  accumulated_time = 0ns;
  for (counter = 0; counter<iterations; counter++) {
    before = std::chrono::high_resolution_clock::now();
    static_();
    after = std::chrono::high_resolution_clock::now();
    accumulated_time += (after - before);
  }
  auto static_time = accumulated_time;

  // empty, local and static
  std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(empty_time).count() << ", ";
  std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(local_time).count() << ", ";
  std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(static_time).count() << "\n";
  return 0;
}