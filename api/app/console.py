from . import app
import click
import os

MODELS_FILE = os.getcwd() + '/app/models.py'

def format_str(text, space = False):
    text += '\n\n' if space else '\n'
    return text

@app.cli.command("make:model")
@click.argument('model', nargs=1)
def make_model(model = None):
    if not os.path.exists(MODELS_FILE):
        model_f = open(MODELS_FILE, 'w')
        model_f.write(
            format_str("from sqlalchemy import Integer, String, DateTime") +
            format_str("from datetime import datetime") +
            format_str("from dataclasses import dataclass") +
            format_str("from .. import db", True)
        )

    with open(MODELS_FILE, 'a') as model_f:
        model_f.write(
            format_str("@dataclass") +
            format_str(f"class {model}(db.Model):") +
            format_str(f"    __tablename__ = '{model.lower() + 's'}'", True) +
            
            format_str("    id = db.Column(Integer(), primary_key=True)") +
            format_str("    created_at = db.Column(DateTime(), default=datetime.now())") +
            format_str("    updated_at = db.Column(DateTime(), default=None)", True) +
            
            format_str("    def to_dict(self):") +
            format_str("        data = { 'id': self.id 'created_at': self.created_at, 'updated_at': self.updated_at }") +
            format_str("        return data", True) +
            
            format_str("    def __repr__(self):") +
            format_str(f"        return f\"<{model} >\"", True) + '\n'
        )
        print(f"Model \"{model}\" created successfully!")