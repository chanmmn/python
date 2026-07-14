#!/usr/bin/env python3
"""
RTX 2060 GPU Test Script
Tests GPU detection, information retrieval, and basic performance benchmarks.
"""

import subprocess
import sys
import time

def check_nvidia_smi():
    """Check GPU using nvidia-smi command."""
    print("=" * 60)
    print("NVIDIA-SMI GPU Information")
    print("=" * 60)
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print("nvidia-smi failed:", result.stderr)
            return False
    except FileNotFoundError:
        print("nvidia-smi not found. NVIDIA drivers may not be installed.")
        return False

def check_nvidia_smi_query():
    """Get detailed GPU info using nvidia-smi query."""
    print("=" * 60)
    print("Detailed GPU Query")
    print("=" * 60)
    try:
        result = subprocess.run([
            'nvidia-smi', '--query-gpu=name,memory.total,memory.free,memory.used,temperature.gpu,utilization.gpu,driver_version,cuda_version',
            '--format=csv,noheader,nounits'
        ], capture_output=True, text=True)
        if result.returncode == 0:
            values = result.stdout.strip().split(', ')
            if len(values) >= 8:
                print(f"GPU Name:        {values[0]}")
                print(f"Total Memory:    {values[1]} MB")
                print(f"Free Memory:     {values[2]} MB")
                print(f"Used Memory:     {values[3]} MB")
                print(f"Temperature:     {values[4]} °C")
                print(f"GPU Utilization: {values[5]} %")
                print(f"Driver Version:  {values[6]}")
                print(f"CUDA Version:    {values[7]}")
            return True
    except Exception as e:
        print(f"Query failed: {e}")
    return False

def test_pytorch():
    """Test GPU with PyTorch."""
    print("\n" + "=" * 60)
    print("PyTorch GPU Test")
    print("=" * 60)
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        
        if torch.cuda.is_available():
            print(f"CUDA version: {torch.version.cuda}")
            print(f"cuDNN version: {torch.backends.cudnn.version()}")
            print(f"GPU count: {torch.cuda.device_count()}")
            print(f"Current device: {torch.cuda.current_device()}")
            print(f"Device name: {torch.cuda.get_device_name(0)}")
            
            # Memory info
            total_mem = torch.cuda.get_device_properties(0).total_memory / (1024**3)
            print(f"Total GPU memory: {total_mem:.2f} GB")
            
            # Simple computation benchmark
            print("\nRunning matrix multiplication benchmark...")
            sizes = [1000, 2000, 4000]
            for size in sizes:
                # Warmup
                a = torch.randn(size, size, device='cuda')
                b = torch.randn(size, size, device='cuda')
                torch.cuda.synchronize()
                
                # Benchmark
                start = time.time()
                for _ in range(10):
                    c = torch.matmul(a, b)
                torch.cuda.synchronize()
                elapsed = time.time() - start
                
                gflops = (2 * size**3 * 10) / (elapsed * 1e9)
                print(f"  Matrix size {size}x{size}: {elapsed:.3f}s, {gflops:.1f} GFLOPS")
                
                del a, b, c
                torch.cuda.empty_cache()
            
            return True
        else:
            print("CUDA not available in PyTorch")
            return False
    except ImportError:
        print("PyTorch not installed. Install with: pip install torch")
        return False
    except Exception as e:
        print(f"PyTorch test failed: {e}")
        return False

def test_tensorflow():
    """Test GPU with TensorFlow."""
    print("\n" + "=" * 60)
    print("TensorFlow GPU Test")
    print("=" * 60)
    try:
        import os
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF warnings
        import tensorflow as tf
        
        print(f"TensorFlow version: {tf.__version__}")
        gpus = tf.config.list_physical_devices('GPU')
        print(f"GPUs detected: {len(gpus)}")
        
        if gpus:
            for gpu in gpus:
                print(f"  - {gpu.name}")
            
            # Simple computation benchmark
            print("\nRunning TensorFlow matrix multiplication benchmark...")
            with tf.device('/GPU:0'):
                size = 2000
                a = tf.random.normal([size, size])
                b = tf.random.normal([size, size])
                
                # Warmup
                _ = tf.matmul(a, b)
                
                start = time.time()
                for _ in range(10):
                    c = tf.matmul(a, b)
                elapsed = time.time() - start
                
                gflops = (2 * size**3 * 10) / (elapsed * 1e9)
                print(f"  Matrix size {size}x{size}: {elapsed:.3f}s, {gflops:.1f} GFLOPS")
            
            return True
        else:
            print("No GPU detected by TensorFlow")
            return False
    except ImportError:
        print("TensorFlow not installed. Install with: pip install tensorflow")
        return False
    except Exception as e:
        print(f"TensorFlow test failed: {e}")
        return False

def test_pycuda():
    """Test GPU with PyCUDA."""
    print("\n" + "=" * 60)
    print("PyCUDA GPU Test")
    print("=" * 60)
    try:
        import pycuda.driver as cuda
        import pycuda.autoinit
        
        print(f"PyCUDA version: {pycuda.VERSION_TEXT}")
        print(f"CUDA driver version: {cuda.get_driver_version()}")
        
        device = cuda.Device(0)
        print(f"\nDevice: {device.name()}")
        print(f"Compute capability: {device.compute_capability()}")
        print(f"Total memory: {device.total_memory() / (1024**3):.2f} GB")
        
        attrs = device.get_attributes()
        print(f"Multiprocessors: {attrs[cuda.device_attribute.MULTIPROCESSOR_COUNT]}")
        print(f"Max threads per block: {attrs[cuda.device_attribute.MAX_THREADS_PER_BLOCK]}")
        print(f"Max block dimensions: ({attrs[cuda.device_attribute.MAX_BLOCK_DIM_X]}, "
              f"{attrs[cuda.device_attribute.MAX_BLOCK_DIM_Y]}, "
              f"{attrs[cuda.device_attribute.MAX_BLOCK_DIM_Z]})")
        print(f"Max grid dimensions: ({attrs[cuda.device_attribute.MAX_GRID_DIM_X]}, "
              f"{attrs[cuda.device_attribute.MAX_GRID_DIM_Y]}, "
              f"{attrs[cuda.device_attribute.MAX_GRID_DIM_Z]})")
        
        return True
    except ImportError:
        print("PyCUDA not installed. Install with: pip install pycuda")
        return False
    except Exception as e:
        print(f"PyCUDA test failed: {e}")
        return False

def stress_test(duration_seconds=10):
    """Run a short GPU stress test using PyTorch."""
    print("\n" + "=" * 60)
    print(f"GPU Stress Test ({duration_seconds} seconds)")
    print("=" * 60)
    try:
        import torch
        if not torch.cuda.is_available():
            print("CUDA not available, skipping stress test")
            return False
        
        print("Running stress test... (monitor temperature with nvidia-smi)")
        size = 4096
        a = torch.randn(size, size, device='cuda')
        b = torch.randn(size, size, device='cuda')
        
        start_time = time.time()
        iterations = 0
        
        while time.time() - start_time < duration_seconds:
            c = torch.matmul(a, b)
            torch.cuda.synchronize()
            iterations += 1
        
        elapsed = time.time() - start_time
        print(f"Completed {iterations} iterations in {elapsed:.1f}s")
        print(f"Average: {iterations/elapsed:.1f} iterations/second")
        
        # Check temperature after stress test
        result = subprocess.run([
            'nvidia-smi', '--query-gpu=temperature.gpu',
            '--format=csv,noheader,nounits'
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Final GPU temperature: {result.stdout.strip()} °C")
        
        del a, b, c
        torch.cuda.empty_cache()
        return True
    except ImportError:
        print("PyTorch not installed, skipping stress test")
        return False
    except Exception as e:
        print(f"Stress test failed: {e}")
        return False

def main():
    print("RTX 2060 GPU Test Suite")
    print("=" * 60)
    print()
    
    results = {}
    
    # Basic NVIDIA driver test
    results['nvidia-smi'] = check_nvidia_smi()
    if results['nvidia-smi']:
        check_nvidia_smi_query()
    
    # Deep learning framework tests
    results['pytorch'] = test_pytorch()
    results['tensorflow'] = test_tensorflow()
    results['pycuda'] = test_pycuda()
    
    # Optional stress test
    print("\n" + "=" * 60)
    run_stress = input("Run GPU stress test? (y/N): ").strip().lower()
    if run_stress == 'y':
        results['stress_test'] = stress_test(duration_seconds=10)
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    for test, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"  {test}: {status}")
    
    # Only consider critical tests for success (tensorflow and pycuda are optional)
    critical_tests = ['nvidia-smi', 'pytorch', 'stress_test']
    return all(results.get(test, False) for test in critical_tests if test in results)

if __name__ == "__main__":
    success = main()
    # Don't use sys.exit() to avoid SystemExit in debugger
    print(f"\nOverall: {'SUCCESS' if success else 'FAILED'}")
