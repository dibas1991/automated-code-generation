import os
from jinja2 import Environment, FileSystemLoader

class CodeGenerator:
    def __init__(self, template_dir='templates'):
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def generate_code(self, template_name, output_file, context):
        template = self.env.get_template(template_name)
        code = template.render(context)
        with open(output_file, 'w') as f:
            f.write(code)
        print(f"Code generated and saved to {output_file}")


if __name__ == "__main__":
    generator = CodeGenerator()

    context = {
        "docstring": "This is a generated class template with detailed comments.",
        "class_name": "MyClass",
        "init_params": "param1, param2"
    }

    generator.generate_code('python_boilerplate.py.j2', 'output/MyClass.py', context)
