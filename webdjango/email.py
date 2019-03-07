from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address
from requests.exceptions import HTTPError
from rest_framework.fields import empty
from webdjango.models.Core import CoreConfig
from webdjango.transports.EmailConfig import EmailCoreConfig
from webdjango.utils import build_absolute_uri
from webdjango.Tools import Tools
from webdjango.exceptions import ServiceUnavailable, ValidationError
from webdjango.models.Core import Website
from webdjango.models.Email import Email
email_config = EmailCoreConfig()
from django.template import Context
from django.template import Template


def get_email_base_context(request=None):
    site = Website.get_current_website(request)
    ## Get Default Logo on the Email Config
    default_logo = EmailCoreConfig.CONFIG_EMAIL_LOGO.value
    print(default_logo)
    logo_url = build_absolute_uri(default_logo)
    return {
        'domain': site.domain,
        'logo_url': logo_url,
        'site_name': site.domain
    }
        
class WebDjangoEmailBackend(BaseEmailBackend):
    """
    A wrapper that Uses our System Transport to send messages
    @sender is chield from AbstractTransport
    """
    sender = None

    def __init__(self, fail_silently=False, **kwargs):
        config = EmailCoreConfig.EMAIL_CONFIG_GROUP.value
        if config and EmailCoreConfig.CONFIG_EMAIL_TYPE.id in config:
            self.set_sender_config(config)

        super().__init__(fail_silently=fail_silently, **kwargs)

    def set_sender_config(self, config):
        className = config[EmailCoreConfig.CONFIG_EMAIL_TYPE.id]
        if className and className is not empty:
            classRef = Tools.getClassReference(
                "webdjango.transports.email.{}".format(str(className)),
                str(className)
            )
            if classRef:
                self.sender = classRef(**config)

    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects and return the number of email
        messages sent.
        """
        if not email_messages:
            return
        num_sent = 0
        for message in email_messages:
            sent = self._send(message)
            if sent:
                num_sent += 1
        return num_sent

    def send(self, email_message):
        """A method that send with email template method that does the actual sending."""
        if 'recipients' not in email_message:
            return False
        encoding = 'encoding' in email_message and email_message['encoding'] or settings.DEFAULT_CHARSET
        recipients = [sanitize_address(addr, encoding)
                      for addr in email_message['recipients']]
        if 'template' in email_message:
            template = Email.objects.get(pk=email_message['template'])
            context = Context(email_message,autoescape=False)
            subject = Template(template.subject).render(context)
            message = Template(template.content).render(context)
        else:
            message = email_message['message']
            subject = email_message['subject']
        if self.sender:
            return self.sender.send(to=recipients,
                                    subject=subject,
                                    body=message)
        raise ServiceUnavailable(
            "No Email SMTP or API Configurated to send email")
        
    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False
        encoding = email_message.encoding or settings.DEFAULT_CHARSET

        recipients = [sanitize_address(addr, encoding)
                      for addr in email_message.recipients()]
        message = email_message.message()
        subject = email_message.subject
        if self.sender:
            return self.sender.send(to=recipients,
                                    subject=subject,
                                    body=message)
        raise ServiceUnavailable(
            "No Email SMTP or API Configurated to send email")

    
    def test(self, email_to):
        if self.sender:
            self.sender.test(email_to)
            return True

        raise ValidationError("No Sender Configurated")
