# myapp/custom_email_backend.py
from django.core.mail.backends.smtp import EmailBackend
from asgiref.sync import sync_to_async

class CustomEmailBackend(EmailBackend):
    async def async_send_messages(self, email_messages):
        # Call the original send_messages method to actually send emails
        return await sync_to_async(super().send_messages)(email_messages)

    async def send_messages(self, email_messages):
        # You can perform some pre-processing here before sending messages

        # Use asyncio to send the emails asynchronously
        await self.async_send_messages(email_messages)


from django.core.mail import EmailMessage