"""
Given a package, list its members
"""
import importlib


def list_package_members(package_name):
    """
    Given a package, list its members
    """
    try:
        print("-------------------------------------------------")
        package = importlib.import_module(package_name)
        package_members = sorted(dir(package), key=str.lower)
        print(
            f"{package} is a valid package, with {len(package_members)} members. Continuing...")
        for i in package_members:
            print(i)
        print(package_members)
    except ImportError:
        print(f"Package '{package_name}' not found.")


def main():
    """
        entry point
    """

    # Example usage:
    list_package_members("os")
    list_package_members("io")
    list_package_members("barf")


if __name__ == "__main__":
    main()
