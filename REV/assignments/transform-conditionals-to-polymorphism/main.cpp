#include <optional>

namespace nc {
  extern void* get_ptr();
  extern void* use_ptr(void* ptr);
  extern void* reuse_ptr(void* ptr);

  void* foo() {
    void* ptr = get_ptr();
    if (ptr == nullptr) {
      return nullptr;
    }

    ptr = use_ptr(ptr);
    if (ptr == nullptr) {
      return nullptr;
    }

    return reuse_ptr(ptr);
  }
}

namespace monads {
  extern std::optional<void*> get_ptr();
  extern std::optional<void*> use_ptr(void* ptr);
  extern std::optional<void*> reuse_ptr(void* ptr);

  std::optional<void*> foo() {
    return get_ptr()
          .and_then(use_ptr)
          .and_then(reuse_ptr);
  }
}
