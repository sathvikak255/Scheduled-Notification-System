import { Routes } from '@angular/router';

import { SubscriptionFormComponent } from './components/subscription-form/subscription-form.component';
import { SubscriptionsListComponent } from './components/subscriptions-list/subscriptions-list.component';

export const routes: Routes = [
    { path: '', redirectTo: 'subscribe', pathMatch: 'full' },
    { path: 'subscribe', component: SubscriptionFormComponent },
    { path: 'subscriptions', component: SubscriptionsListComponent },
];
