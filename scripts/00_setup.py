#!/usr/bin/env python3
"""
Setup Verification Script

This script checks that your Python environment is properly configured
for this course/workshop.

Run this script after completing the setup instructions in SETUP.md
If all checks pass, you're ready to start!

Usage:
    uv run python scripts/00_setup.py
"""

import sys
import os
import platform
import subprocess
from pathlib import Path


def print_header(text):
    """Print a formatted header."""
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print(f"{'=' * 60}\n")


def print_check(passed, message, details=None):
    """Print a check result with appropriate symbol."""
    symbol = "✓" if passed else "✗"
    print(f"  {symbol} {message}")
    if details:
        print(f"    {details}")


def print_info(message, details=None):
    """Print an informational message."""
    print(f"  ℹ {message}")
    if details:
        print(f"    {details}")


def print_warning(message, details=None):
    """Print a warning message."""
    print(f"  ⚠ {message}")
    if details:
        print(f"    {details}")


def check_python_version():
    """Check if Python version meets minimum requirements."""
    print("Checking Python version...")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    min_version = (3, 10)
    
    if version >= min_version:
        print_check(True, f"Python {version_str} detected")
        return True
    else:
        print_check(False, f"Python {version_str} is too old")
        print(f"    Please install Python {min_version[0]}.{min_version[1]} or higher")
        print("    Download from: https://www.python.org/downloads/")
        return False


def check_in_venv():
    """Check if running in a virtual environment."""
    print("\nChecking virtual environment...")
    
    in_venv = (
        hasattr(sys, 'real_prefix') or 
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )
    
    if in_venv:
        venv_path = sys.prefix
        print_check(True, "Running in a virtual environment")
        print(f"    Location: {venv_path}")
        return True
    else:
        print_warning("Not running in a virtual environment")
        print("    It's recommended to use: uv run python scripts/00_setup.py")
        return False


def check_uv_installed():
    """Check if uv is installed."""
    print("\nChecking uv package manager...")
    
    try:
        result = subprocess.run(
            ["uv", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        version = result.stdout.strip()
        print_check(True, f"uv is installed: {version}")
        return True
    except FileNotFoundError:
        print_check(False, "uv is not installed or not in PATH")
        print("    Install from: https://docs.astral.sh/uv/getting-started/installation/")
        return False
    except subprocess.CalledProcessError:
        print_warning("uv is installed but returned an error")
        return False


def check_project_structure():
    """Check if expected project folders exist."""
    print("\nChecking project structure...")
    
    # Get project root (assuming script is in scripts/ folder)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    expected_folders = ["data", "scripts", "lessons", "figures"]
    all_found = True
    
    for folder in expected_folders:
        folder_path = project_root / folder
        if folder_path.exists():
            print_check(True, f"Found folder: {folder}")
        else:
            print_check(False, f"Missing folder: {folder}")
            print("    Make sure you're running this from the project root")
            all_found = False
    
    # Check for pyproject.toml
    pyproject = project_root / "pyproject.toml"
    if pyproject.exists():
        print_check(True, "Found pyproject.toml")
    else:
        print_warning("pyproject.toml not found")
        all_found = False
    
    return all_found


def check_required_packages():
    """Check if required packages are installed and can be imported."""
    print("\nChecking required packages...")
    
    # Modify this list based on your course requirements
    required_packages = {
        "numpy": "NumPy - Numerical computing",
        "pandas": "Pandas - Data manipulation",
        "matplotlib": "Matplotlib - Plotting",
        "jupyter": "Jupyter - Interactive notebooks"
    }
    
    optional_packages = {
        "seaborn": "Seaborn - Statistical visualization",
        "scipy": "SciPy - Scientific computing",
        "requests": "Requests - HTTP library"
    }
    
    missing_required = []
    missing_optional = []
    
    # Check required packages
    for package, description in required_packages.items():
        try:
            __import__(package)
            print_check(True, package)
        except ImportError:
            print_check(False, f"{package} (REQUIRED)")
            missing_required.append(package)
    
    # Check optional packages
    if optional_packages:
        print("\nChecking optional packages...")
        for package, description in optional_packages.items():
            try:
                __import__(package)
                print_check(True, package)
            except ImportError:
                print_info(f"{package} (optional)", description)
                missing_optional.append(package)
    
    return missing_required, missing_optional


def test_package_functionality():
    """Test that key packages work correctly."""
    print("\nTesting key functionality...")
    
    all_passed = True
    
    # Test NumPy
    print("  Testing NumPy...")
    try:
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        result = np.mean(arr)
        if result == 3.0:
            print_check(True, "NumPy works correctly")
        else:
            print_check(False, f"NumPy test failed: expected 3.0, got {result}")
            all_passed = False
    except Exception as e:
        print_check(False, f"NumPy test failed: {str(e)}")
        all_passed = False
    
    # Test Pandas
    print("  Testing Pandas...")
    try:
        import pandas as pd
        df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
        result = len(df[df["x"] > 1])
        if result == 2:
            print_check(True, "Pandas works correctly")
        else:
            print_check(False, f"Pandas test failed: expected 2 rows, got {result}")
            all_passed = False
    except Exception as e:
        print_check(False, f"Pandas test failed: {str(e)}")
        all_passed = False
    
    # Test Matplotlib
    print("  Testing Matplotlib...")
    try:
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 4, 9])
        print_check(True, "Matplotlib works correctly")
        plt.close(fig)
    except Exception as e:
        print_check(False, f"Matplotlib test failed: {str(e)}")
        all_passed = False
    
    return all_passed


def test_file_paths():
    """Test that file path handling works correctly."""
    print("  Testing file path management...")
    
    try:
        from pathlib import Path
        
        # Get project root
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        
        # Test that we can construct paths
        data_dir = project_root / "data"
        
        print_check(True, "File path management works")
        print(f"    Project root: {project_root}")
        return True
    except Exception as e:
        print_check(False, f"File path test failed: {str(e)}")
        return False


def create_test_plot():
    """Create a simple test plot to verify graphics work."""
    print("\nCreating a test plot...")
    
    try:
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend
        import matplotlib.pyplot as plt
        import numpy as np
        from pathlib import Path
        
        # Get project root and figures directory
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        figures_dir = project_root / "figures"
        
        # Create figures directory if it doesn't exist
        figures_dir.mkdir(exist_ok=True)
        
        # Generate test plot
        x = np.linspace(0, 10, 100)
        y = x ** 2
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, linewidth=2, color='steelblue')
        plt.title('Setup Test Plot', fontsize=14, fontweight='bold')
        plt.xlabel('X values')
        plt.ylabel('Y values')
        plt.grid(True, alpha=0.3)
        
        output_path = figures_dir / "setup_test_plot.png"
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print_check(True, f"Test plot saved to: {output_path}")
        print("    Open this file to verify that graphics work correctly")
        return True
        
    except Exception as e:
        print_warning(f"Could not create test plot: {str(e)}")
        return False


def get_system_info():
    """Get and display system information."""
    print("\nSystem Information:")
    
    info = {
        "Operating System": f"{platform.system()} {platform.release()}",
        "Platform": platform.platform(),
        "Python Version": sys.version.split()[0],
        "Python Implementation": platform.python_implementation(),
        "Architecture": platform.machine(),
    }
    
    for key, value in info.items():
        print(f"  {key}: {value}")


def print_summary(checks_passed, missing_required, missing_optional):
    """Print summary and recommendations."""
    print_header("Summary")
    
    if checks_passed and not missing_required:
        print("✓ All required packages are installed!\n")
        print("You're ready to start the course!")
        print("Next steps:")
        print("  1. Review the README.md for course information")
        print("  2. Check the course schedule")
        print("  3. Start with lessons/lesson-01/\n")
        
        if missing_optional:
            print("Optional: Install additional packages for enhanced functionality:")
            print(f"  uv pip install {' '.join(missing_optional)}\n")
    else:
        print("✗ Setup incomplete\n")
        
        if missing_required:
            print("Please install missing required packages:")
            print(f"  uv pip install {' '.join(missing_required)}\n")
            print("Or run:")
            print("  uv sync\n")
            print("After installing packages, run this script again to verify.\n")
    
    print("If you encounter any issues:")
    print("  1. See SETUP.md for detailed troubleshooting")
    print("  2. Check the course discussion forum")
    print("  3. Contact the instructor\n")
    
    print("=" * 60 + "\n")


def main():
    """Run all setup checks."""
    print_header("Course Setup Verification")
    
    # Run checks
    python_ok = check_python_version()
    venv_ok = check_in_venv()
    uv_ok = check_uv_installed()
    structure_ok = check_project_structure()
    
    missing_required, missing_optional = check_required_packages()
    
    # Only run functionality tests if packages are installed
    if not missing_required:
        functionality_ok = test_package_functionality()
        path_ok = test_file_paths()
        plot_ok = create_test_plot()
    else:
        functionality_ok = False
        path_ok = False
        plot_ok = False
    
    get_system_info()
    
    # Determine overall pass/fail
    all_checks_passed = (
        python_ok and 
        structure_ok and 
        functionality_ok and 
        path_ok
    )
    
    print_summary(all_checks_passed, missing_required, missing_optional)
    
    # Print session info note
    print("Detailed package information:")
    print("Run 'uv pip list' to see all installed packages\n")
    
    # Exit with appropriate code
    sys.exit(0 if (all_checks_passed and not missing_required) else 1)


if __name__ == "__main__":
    main()