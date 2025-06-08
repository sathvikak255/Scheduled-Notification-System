from django.core.management.base import BaseCommand
from django.utils import timezone
from reports.models import Subscription, ReportHistory
from reports.utils import generate_pdf_report, generate_html_report, send_email_with_attachment

class Command(BaseCommand):
    help = 'Send daily reports to subscribed emails'

    def handle(self, *args, **kwargs): 
        today = timezone.now().date()
        subs = Subscription.objects.filter(is_active=True, start_date__lte=today, end_date__gte=today)

        self.stdout.write(f"Sending reports for {today}...")

        if not subs.exists():
            print("No active subscriptions to send reports to.")
            return
        for sub in subs:
            email = sub.email
            formats = sub.formats.lower()

            if 'pdf' == formats.strip():
                pdf_path = generate_pdf_report(email)
                send_email_with_attachment(email, f"Daily PDF Report - {today}", "See attached PDF", pdf_path)
                ReportHistory.objects.create(subscription=sub, date_sent=today, format='pdf', status='sent')
                self.stdout.write("Your message here")

            if 'html' == formats.strip():
                html_path = generate_html_report(email)
                send_email_with_attachment(email, f"Daily HTML Report - {today}", "See attached HTML", html_path)
                ReportHistory.objects.create(subscription=sub, date_sent=today, format='html', status='sent')
                self.stdout.write("Your message here")

            if 'both' == formats.strip():
                pdf_path = generate_pdf_report(email)
                send_email_with_attachment(email, f"Daily PDF Report - {today}", "See attached PDF", pdf_path)
                ReportHistory.objects.create(subscription=sub, date_sent=today, format='pdf', status='sent')

                html_path = generate_html_report(email)
                send_email_with_attachment(email, f"Daily HTML Report - {today}", "See attached HTML", html_path)
                ReportHistory.objects.create(subscription=sub, date_sent=today, format='html', status='sent')

