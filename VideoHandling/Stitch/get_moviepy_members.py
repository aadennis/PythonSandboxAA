"""
Given a package, list its members
This version is for finding what is available in
the depths of MoviePy
https://moviepy.readthedocs.io/en/latest/ref/ref.html#
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
        print(f"End of [{package_name}] breakdown")
        print("-------------------------------------------------")
    except ImportError:
        print(f"Package '{package_name}' not found.")


def main():
    """
        entry point
    """

    # Example usage:
    list_package_members("os")
    list_package_members("moviepy")
    list_package_members("moviepy.editor")
    list_package_members("moviepy.video")
    list_package_members("moviepy.video.fx")
    list_package_members("moviepy.video.tools.credits")
    list_package_members("moviepy.Clip")
    list_package_members("moviepy.video.VideoClip")
    list_package_members("moviepy.video.fx.all")

    
    

    
    
    

if __name__ == "__main__":
    main()
