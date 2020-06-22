import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LayoutComponent } from './layout/components/layout/layout.component';
import { HomeComponent } from './pages/home/home.component';

const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      // { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      {
        path: '',
        loadChildren: () =>
          import('./pages/home/home.module').then((m) => m.HomeModule),
      },
      {
        path: 'blog',
        loadChildren: () =>
          import('./pages/blog/blog.module').then((m) => m.BlogModule),
      },
      {
        path: 'about',
        loadChildren: () =>
          import('./pages/about/about.module').then((m) => m.AboutModule),
      },
      // {
      //   path: 'css',
      //   loadChildren: () =>
      //     import('./feature/css-design/css-design.module').then(
      //       (m) => m.CssDesignModule
      //     ),
      // },
      // {
      //   path: 'charts',
      //   loadChildren: () =>
      //     import('./feature/charts/charts.module').then((m) => m.ChartsModule),
      // },
      { path: '**', component: HomeComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
