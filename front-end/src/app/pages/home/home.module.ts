import { NgModule } from '@angular/core';

import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home.component';
import { LayoutModule } from 'src/app/layout/layout.module';
import { ShareModule } from 'src/app/share/share.module';

@NgModule({
  declarations: [HomeComponent],
  imports: [HomeRoutingModule, ShareModule],
})
export class HomeModule {}
