// src/app/app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { SubscriptionFormComponent } from './components/subscription-form/subscription-form.component';
import { SubscriptionsListComponent } from './components/subscriptions-list/subscriptions-list.component';

const routes: Routes = [
    { path: 'subscribe', component: SubscriptionFormComponent },
    { path: 'subscriptions', component: SubscriptionsListComponent },
    { path: '', redirectTo: '/subscribe', pathMatch: 'full' },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
