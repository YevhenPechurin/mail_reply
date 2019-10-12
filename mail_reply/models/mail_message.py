from odoo import models, fields, api, _


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.multi
    def reply_context(self):
        self.ensure_one()

        body = (_(
            "<div font-style=normal;><br/></div><blockquote>----- Original message ----- <br/> Date: %s <br/> From: %s <br/> Subject: %s <br/><br/>%s</blockquote>") %
                (str(self.date), self.author_id.name, self.subject, self.body))

        ctx = {
            'default_res_id': self.res_id,
            'default_parent_id': self.id,
            'default_model': self.model,
            'default_body': body,
            'default_m_id': self.id,
        }
        return ctx
