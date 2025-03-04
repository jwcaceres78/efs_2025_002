from odoo import models, fields

class Book(models.Model):
    _name = 'book'
    _description = 'Book Model'

    name = fields.Char(string='Name', required=True)
    pages = fields.Integer(string='Number of Pages')
    publication_date = fields.Date(string='Publication Date')
    author = fields.Char(string='Author')

