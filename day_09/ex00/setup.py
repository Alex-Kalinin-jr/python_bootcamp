from distutils.core import setup, Extension

def main():
  setup(name="math_methods",
        version="0.1",
        description="Py iface for math methods",
        author="cursebow",
        author_email="cursebow@student.21-school.ru",
        ext_modules=[Extension("math_methods", ["calculator.c"])],
        )
  
if __name__ == "__main__":
  main()
