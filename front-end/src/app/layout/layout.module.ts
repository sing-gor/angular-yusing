import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RouterModule, Router } from '@angular/router';
import { ShareModule } from '../share/share.module';
import { LayoutComponent } from './components/layout/layout.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { SidebarModule } from 'primeng/sidebar';
@NgModule({
  declarations: [LayoutComponent, HeaderComponent, FooterComponent],
  imports: [RouterModule, ShareModule, SidebarModule, RouterModule],
  exports: [SidebarModule],
})
export class LayoutModule {}
