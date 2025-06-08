import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SubscriptionService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  subscribeToReports(data: any) {
    return this.http.post(`${this.apiUrl}/subscribe/`, data);
  }

  unsubscribeFromReports() {
    return this.http.post(`${this.apiUrl}/unsubscribe/`, {});
  }

  getSubscriptions() {
    return this.http.get(`${this.apiUrl}/subscriptions/`);
  }
}
