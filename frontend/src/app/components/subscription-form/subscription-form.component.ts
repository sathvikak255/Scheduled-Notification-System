// src/app/components/subscription-form/subscription-form.component.ts
import { Component } from '@angular/core';
import { HttpClient, provideHttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';


@Component({
  selector: 'app-subscription-form',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './subscription-form.component.html',
  styleUrls: ['./subscription-form.component.css'],
})
export class SubscriptionFormComponent {
  email = '';
  start_date = '';
  end_date = '';

  formatOptions = ['pdf', 'html', 'both'];
  selectedFormat = 'pdf';

  message = '';

  constructor(private http: HttpClient) { }

  subscribe() {
    const body = {
      email: this.email,
      start_date: this.start_date,
      end_date: this.end_date,
      formats: this.selectedFormat
    };

    this.http.post('http://localhost:8000/api/subscribe/', body).subscribe({
      next: () => {
        this.message = 'Subscribed successfully!';
        this.email = this.start_date = this.end_date = '';
        this.selectedFormat = 'pdf';
      },
      error: err => {
        this.message = 'Subscription failed. Check your input or try again later.';
        console.error(err);
      }
    });
  }
}
