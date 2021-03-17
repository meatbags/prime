/** Rabin Miller primality test */

#define BOOST_MP_DISABLE_DEPRECATE_03_WARNING

#include <vector>
#include <stdio.h>
#include <chrono>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

// get time in milliseconds
uint64_t time_now() {
  using namespace std::chrono;
  return duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
}

// get number of digits
int count_digits(cpp_int n) {
  int size = 0;
  while (n > 0) {
    size++;
    n /= 10;
  }
  return size;
}

// multiplication with mod
cpp_int mulmod(cpp_int a, cpp_int b, cpp_int m) {
  cpp_int x = 0;
  cpp_int y = a % m;
  while (b > 0) {
    if (b % 2 == 1) {
      x = (x + y) % m;
    }
    y = (y * 2) % m;
    b /= 2;
  }
  return x % m;
}

// mod
cpp_int modulo(cpp_int base, cpp_int e, cpp_int m) {
  cpp_int x = 1;
  cpp_int y = base;
  while (e > 0) {
    if (e % 2 == 1) {
      x = (x * y) % m;
    }
    y = (y * y) % m;
    e = e / 2;
  }
  return x % m;
}

// Rabin-Miller test
bool Miller(cpp_int p, int reps) {
  if (p < 2 || (p != 2 && p % 2 == 0)) {
    return false;
  }
  cpp_int s = p - 1;
  cout << "Calculating S...\n";
  while (s % 2 == 0) {
    s /= 2;
  }
  for (int i=0; i<reps; i++) {
    cout << "REP: " << i+1 << "\n";
    cpp_int a = rand() % (p - 1) + 1;
    cpp_int temp = s;
    cout << "modulo\n";
    cpp_int mod = modulo(a, temp, p);
    cout << "mulmod\n";
    while (temp != p-1 && mod != 1 && mod != p-1) {
      mod = mulmod(mod, mod, p);
      temp *= 2;
    }
    if (mod != p - 1 && temp % 2 == 0) {
      return false;
    }
  }
  return true;
}

// sieve n primes or primes < limit
std::vector<int> ESieve(int n, int lim=0) {
  std::vector<int> primes;
  primes.push_back(2);
  int found = 1;
  int p = 3;
  while ((!n || primes.size() < n) && (!lim || p < lim)) {
    bool ok = true;
    for (int i=0; i<primes.size(); i++) {
      if (p % primes[i] == 0) {
        ok = false;
        break;
      }
    }
    if (ok) {
      primes.push_back(p);
    }
    p += 2;
  };
  return primes;
}

// is prime in array
bool contains(cpp_int n, std::vector<int> arr) {
  for (int i=0; i<arr.size(); i++) {
    if (arr[i] == n) {
      return true;
    }
  }
  return false;
}

// generate number
cpp_int generate_number(int exp1, int exp2) {
  cpp_int n(1);
  cpp_int m(1);
  return (n << exp1) - (m << exp2) - 1;
}

int main() {
  uint64_t time_start = time_now();

  // sieve 10K primes ~ 0.27s
  // std::vector<int> primes = ESieve(10000);

  // candidate numbers
  int exponent = 332192812; // 8;
  int max_exponents = 100; // exponent;
  std::vector<int> exponents;
  std::vector<cpp_int> candidates;
  std::vector<cpp_int> results;
  cout << "Generating candidates...\n";
  for (int i=1; i<max_exponents; i++) {
    cpp_int num = generate_number(exponent, i);
    exponents.push_back(i);
    candidates.push_back(num);
  }
  cout << "Done.\n";

  // digits
  cout << "Counting digits...\n";
  cout << count_digits(candidates[0]);

  // check results
  int reps = 10;
  for (int i=0; i<candidates.size(); i++) {
    bool res = Miller(candidates[i], reps);
    bool found = false;
    if (res) {
      //results.push_back(exponents[i]);
      //results.push_back(candidates[i]);
      // found = contains(candidates[i], primes);
    }
    std::cout << "2^" << exponent << " - 2^" << exponents[i] << " - 1 = ";// << candidates[i];
    std::cout << " Miller: " << res;//<< ", Sieve: " << found;
    std::cout << "\n";
  }

  // print
  /*
  std::cout << "\nRESULTS\n";
  for (int i=0; i<results.size(); i+=2) {
    std::cout << "2^" << exponent << " - 2^" << results[i] << " - 1 = " << results[i+1] << "\n";
  }
  std::cout << "\n";
  */

  // log time
  cout << (time_now() - time_start)/1000.0 << "\n";
  return 0;
}
