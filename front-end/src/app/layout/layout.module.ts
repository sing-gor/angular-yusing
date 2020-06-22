import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RouterModule, Router } from '@angular/router';
import { ShareModule } from '../share/share.module';
import { LayoutComponent } from './components/layout/layout.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';

import { SidebarLeftComponent } from './components/siderbar/sidebar-left/sidebar-left.component';
import { SidebarRightComponent } from './components/siderbar/sidebar-right/sidebar-right.component';
import { SidebarTopComponent } from './components/siderbar/sidebar-top/sidebar-top.component';
import { SidebarBottomComponent } from './components/siderbar/sidebar-bottom/sidebar-bottom.component';
import { SidebarMobileComponent } from './components/siderbar/sidebar-mobile/sidebar-mobile.component';
import { InlineSVGModule } from 'ng-inline-svg';
import { SafeHtmlPipe } from '../safe-html.pipe';

@NgModule({
  declarations: [
    LayoutComponent,
    HeaderComponent,
    FooterComponent,
    SidebarLeftComponent,
    SidebarRightComponent,
    SidebarTopComponent,
    SidebarBottomComponent,
    SidebarMobileComponent,
    SafeHtmlPipe,
  ],
  imports: [RouterModule, ShareModule],
  exports: [],
})
export class LayoutModule {}
