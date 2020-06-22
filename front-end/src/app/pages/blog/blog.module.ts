import { NgModule } from '@angular/core';

import { BlogRoutingModule } from './blog-routing.module';
import { BlogDetailComponent } from './blog-detail/blog-detail.component';
import { BlogListComponent } from './blog-list/blog-list.component';
import { ShareModule } from 'src/app/share/share.module';

@NgModule({
  declarations: [BlogDetailComponent, BlogListComponent],
  imports: [BlogRoutingModule, ShareModule],
})
export class BlogModule {}
