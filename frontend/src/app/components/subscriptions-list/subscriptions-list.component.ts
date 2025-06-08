import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-subscriptions-list',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './subscriptions-list.component.html',
  styleUrls: ['./subscriptions-list.component.css']
})
export class SubscriptionsListComponent implements OnInit {
  subscriptions: any[] = [];
  email = '';
  message = '';

  constructor(private http: HttpClient) { }

  ngOnInit(): void { }

  loadSubscriptions() {
    if (!this.email) return;
    this.http.get(`http://localhost:8000/api/subscriptions/?email=${this.email}`).subscribe({
      next: (res: any) => {
        this.subscriptions = res;
        this.message = res.length ? '' : 'No subscriptions found.';
      },
      error: err => {
        this.message = 'Failed to load subscriptions.';
        console.error(err);
      }
    });
  }

  unsubscribe() {
    const body = { email: this.email };
    this.http.post('http://localhost:8000/api/unsubscribe/', body).subscribe({
      next: () => {
        this.message = 'Unsubscribed successfully.';
        // this.loadSubscriptions(); 
      },
      error: err => {
        this.message = 'Unsubscribe failed.';
        console.error(err);
      }
    });
  }


}
