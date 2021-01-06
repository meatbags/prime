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

//int count_digits(cpp_int n) {}

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

// generate the number
cpp_int generate_number(int exp1, int exp2) {
  cpp_int n(1);
  cpp_int m(1);
  return (n << exp1) - (m << exp2) - 1;
}

int main() {
  // sieve 10K primes ~ 0.27s
  std::vector<int> primes = ESieve(1000);

  // set exponent, candidates
  int exponent = 332192812;
  std::vector<int> candidates;
  for (int i=1; i<=1000; i++) {
    candidates.push_back(i);
  }
  int index_start = 1;
  int index_stop = primes.size();

  // start timer
  uint64_t time_start = time_now();

  // check against primes
  for (int i=index_start; i<index_stop; i++) {
    int prime = primes[i];
    cout << "Testing candidates against prime #" << i << ": " << prime << "\n";

    for (int j=candidates.size()-1; j>=0; j--) {
      int candidate = candidates[j];
      // get number
      cpp_int n(1);
      cpp_int m(1);
      n = (n << exponent) - (m << candidate) - 1;
      if (n % prime == 0) {
        cout << j << " Failed % " << prime << "\n";
        candidates.erase(candidates.begin() + j);
      }
    }

    cout << "Candidates remaining:" << candidates.size() << "\n";
    for (int j=0; j<candidates.size(); j++) {
      cout << j << " ";
    }
    cout << "\n\n";
  }

  // timer
  cout << (time_now() - time_start)/1000. << "\n";

  // exit
  return 0;
}
