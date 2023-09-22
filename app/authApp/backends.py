# from django.core.mail.backends.base import BaseEmailBackend
# from aiosmtplib import SMTP

# class AsyncEmailBackend(BaseEmailBackend):
#     async def send_messages(self, email_messages):
#         for message in email_messages:
#             await self._send(message)

#     async def _send(self, email_message):
#         # Implement your asynchronous email sending logic here
#         async with SMTP(
#             hostname='smtp.example.com', port=587
#         ) as client:
#             await client.starttls()
#             await client.login('your_username', 'your_password')
#             await client.sendmail(
#                 email_message.from_email,
#                 email_message.recipients(),
#                 email_message.message().as_string(),
#             )
