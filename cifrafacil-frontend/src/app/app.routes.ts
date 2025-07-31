import { Routes } from '@angular/router';
import { CifraFormComponent } from './cifra-form/cifra-form.component';
import { AppComponent } from './app.component';
export const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'cifra', component: CifraFormComponent }
];