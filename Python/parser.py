
from __future__ import print_function
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
sys.path.extend(['.', '..'])

from pycparser import parse_file, c_generator


def translate_to_c(filename):
    """ Simply use the c_generator module to emit a parsed AST.
    """
    ast = parse_file(filename,use_cpp=True)
    generator = c_generator.CGenerator()
    print(generator.visit(ast))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        translate_to_c(r"D:\Drive\3.sınıf\Second Semester\Karantina\Microprocessor Systems\Ödevler\Ödevler-1\Python\deneme.cpp")
    else:
        print("Please provide a filename as argument")