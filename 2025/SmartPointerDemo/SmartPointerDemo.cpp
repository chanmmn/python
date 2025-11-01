// demp.cpp
// Minimal example of a reference-counted smart pointer (SharedPtr)
// Not a production replacement for std::shared_ptr, but demonstrates core ideas.

#include <iostream>
#include <atomic>
#include <utility>

// A very small thread-friendly reference-counted smart pointer.
template <typename T>
class SharedPtr {
    T* ptr = nullptr;
    std::atomic<long>* ref = nullptr;

    void release() {
        if (ref && --(*ref) == 0) {
            delete ptr;
            delete ref;
            ptr = nullptr;
            ref = nullptr;
        }
    }

public:
    // default ctor -> empty pointer
    SharedPtr() noexcept = default;

    // construct from raw pointer
    explicit SharedPtr(T* p) noexcept : ptr(p), ref(new std::atomic<long>(1)) {}

    // copy ctor
    SharedPtr(const SharedPtr& other) noexcept : ptr(other.ptr), ref(other.ref) {
        if (ref) ++(*ref);
    }

    // move ctor
    SharedPtr(SharedPtr&& other) noexcept : ptr(other.ptr), ref(other.ref) {
        other.ptr = nullptr;
        other.ref = nullptr;
    }

    // copy assignment
    SharedPtr& operator=(const SharedPtr& other) noexcept {
        if (this != &other) {
            release();
            ptr = other.ptr;
            ref = other.ref;
            if (ref) ++(*ref);
        }
        return *this;
    }

    // move assignment
    SharedPtr& operator=(SharedPtr&& other) noexcept {
        if (this != &other) {
            release();
            ptr = other.ptr;
            ref = other.ref;
            other.ptr = nullptr;
            other.ref = nullptr;
        }
        return *this;
    }

    ~SharedPtr() {
        release();
    }

    // accessors
    T* get() const noexcept { return ptr; }
    T& operator*() const noexcept { return *ptr; }
    T* operator->() const noexcept { return ptr; }
    explicit operator bool() const noexcept { return ptr != nullptr; }

    long use_count() const noexcept { return ref ? static_cast<long>(*ref) : 0; }

    void reset() noexcept {
        release();
    }

    void reset(T* p) noexcept {
        release();
        if (p) {
            ptr = p;
            ref = new std::atomic<long>(1);
        }
    }

    void swap(SharedPtr& other) noexcept {
        std::swap(ptr, other.ptr);
        std::swap(ref, other.ref);
    }
};

// helper to create a SharedPtr (similar to std::make_shared but simpler)
template <typename T, typename... Args>
SharedPtr<T> make_shared_simple(Args&&... args) {
    return SharedPtr<T>(new T(std::forward<Args>(args)...));
}

// Example usage
struct Foo {
    int v;
    Foo(int x) : v(x) { std::cout << "Foo(" << v << ") constructed\n"; }
    ~Foo() { std::cout << "Foo(" << v << ") destroyed\n"; }
    void show() const { std::cout << "Foo value: " << v << '\n'; }
};

int main() {
    // create a SharedPtr
    SharedPtr<Foo> p1 = make_shared_simple<Foo>(42);
    std::cout << "p1 use_count: " << p1.use_count() << '\n'; // 1

    {
        SharedPtr<Foo> p2 = p1; // copy, share ownership
        std::cout << "after copy, p1 use_count: " << p1.use_count() << '\n'; // 2
        p2->show();

        SharedPtr<Foo> p3 = std::move(p2); // move ownership to p3
        std::cout << "after move, p3 use_count: " << p3.use_count() << '\n'; // 2
        // p2 is empty now
        std::cout << "p2 is " << (p2 ? "non-empty" : "empty") << '\n';
    } // p3 goes out of scope, ref count decreases

    std::cout << "after inner scope, p1 use_count: " << p1.use_count() << '\n'; // 1

    p1.reset(); // releases the managed object -> Foo destroyed
    std::cout << "after reset, p1 use_count: " << p1.use_count() << '\n'; // 0

    return 0;
}